#!/usr/bin/env python3
"""
construir_libro.py — Genera las versiones descargables del libro.

Produce, en la carpeta descargas/:
  - libro-gf7-entrega-N.html      Un solo archivo HTML. Las soluciones están plegadas
                                  (se despliegan con un clic). Funciona sin conexión.
  - libro-gf7-entrega-N.pdf       Versión para imprimir o leer en el móvil/tableta.
                                  Las soluciones aparecen desplegadas en recuadros.
  - libro-gf7-entrega-N-fuentes.zip  Todo el repositorio (Markdown, código, HTML y PDF).

Uso (desde la raíz del repositorio):
    python3 herramientas/construir_libro.py --entrega 1

Requisitos: Python 3, pandoc (>= 3) y Chromium/Chrome (para el PDF).
La ruta de Chromium se puede indicar con --chrome; si no, se busca automáticamente.

Cómo funciona:
  1. Junta todos los documentos en el orden de lectura del libro.
  2. Reescribe los enlaces entre archivos para que apunten dentro del documento único.
  3. Convierte a HTML con pandoc (lector «gfm», el mismo dialecto que usa GitHub).
  4. Ajusta el tamaño de letra de cada bloque de código para que los diagramas
     de texto quepan en la página sin cortarse.
  5. Imprime el HTML a PDF con Chromium (con números de página y marcadores).
"""

import argparse
import glob
import html
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

RAIZ = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

# ---------------------------------------------------------------------------
# 1. Orden de lectura
# ---------------------------------------------------------------------------

def clave_capitulo(ruta):
    m = re.search(r"cap-(\d+)-(\d+)", os.path.basename(ruta))
    return (int(m.group(1)), int(m.group(2))) if m else (999, 999)


def documentos_en_orden():
    capitulos = sorted(glob.glob(os.path.join(RAIZ, "libro", "parte-*", "modulo-*", "cap-*.md")),
                       key=clave_capitulo)
    orden = (["README.md",
              "libro/00-como-estudiar-este-libro.md",
              "libro/00-indice-general.md",
              "libro/00-mapa-de-prerrequisitos.md"]
             + [os.path.relpath(c, RAIZ) for c in capitulos]
             + ["apendices/glosario.md",
                "apendices/hoja-de-formulas.md",
                "apendices/errores-frecuentes.md",
                "apendices/bibliografia.md",
                "PROGRESO.md",
                "codigo/README.md"])
    return [d for d in orden if os.path.exists(os.path.join(RAIZ, d))]


def archivos_de_codigo():
    return sorted(os.path.relpath(p, RAIZ)
                  for p in glob.glob(os.path.join(RAIZ, "codigo", "**", "*.py"), recursive=True))


def id_de(ruta):
    """Identificador de ancla para un archivo: 'libro/00-indice-general.md' -> 'doc-libro-00-indice-general'."""
    base = re.sub(r"\.(md|py)$", "", ruta)
    return "doc-" + re.sub(r"[^A-Za-z0-9_-]+", "-", base).strip("-")


# ---------------------------------------------------------------------------
# 2. Reescritura de enlaces y anclas
# ---------------------------------------------------------------------------

def reescribir(texto, ruta, incluidos):
    """Hace que los enlaces entre archivos apunten a anclas del documento único."""
    doc_id = id_de(ruta)
    carpeta = os.path.dirname(ruta)

    # Anclas propias <a id="x"> -> <a id="doc-...--x"> (evita choques entre capítulos)
    texto = re.sub(r'<a id="([^"]+)"></a>', lambda m: f'<a id="{doc_id}--{m.group(1)}"></a>', texto)

    def destino(m):
        etiqueta, enlace = m.group(1), m.group(2)
        if re.match(r"^[a-z]+:", enlace):           # http:, https:, mailto: ...
            return m.group(0)
        if enlace.startswith("#"):                  # ancla dentro del mismo archivo
            return f"[{etiqueta}](#{doc_id}--{enlace[1:]})"
        camino, _, frag = enlace.partition("#")
        objetivo = os.path.normpath(os.path.join(carpeta, camino))
        if objetivo in incluidos:
            ancla = id_de(objetivo) + (f"--{frag}" if frag else "")
            return f"[{etiqueta}](#{ancla})"
        if objetivo.startswith("codigo"):           # carpeta de código u otro archivo de código
            return f"[{etiqueta}](#{id_de('codigo/README.md')})"
        if objetivo.startswith("descargas"):        # las propias descargas: sin enlace dentro del libro
            return etiqueta
        print(f"  aviso: enlace sin destino en el libro: {ruta} -> {enlace}", file=sys.stderr)
        return etiqueta

    # Enlaces Markdown [texto](destino) — fuera de los bloques de código
    partes = re.split(r"(^```.*?^```)", texto, flags=re.S | re.M)
    for i in range(0, len(partes), 2):
        partes[i] = re.sub(r"\[([^\]]*)\]\(([^)\s]+)\)", destino, partes[i])
    return "".join(partes)


def construir_markdown(entrega):
    docs = documentos_en_orden()
    codigo = archivos_de_codigo()
    incluidos = set(docs) | set(codigo)
    trozos = []
    for d in docs:
        texto = open(os.path.join(RAIZ, d), encoding="utf-8").read()
        trozos.append(f'<a id="{id_de(d)}"></a>\n\n' + reescribir(texto, d, incluidos))
    # Apéndice con el código fuente completo
    listado = ["# Apéndice de código: programas del libro\n",
               "Copia íntegra de los programas incluidos en el repositorio, para poder "
               "leerlos sin conexión. Para ejecutarlos, usa los archivos `.py` del ZIP "
               "(no copies desde el PDF: los saltos de línea y espacios podrían alterarse).\n"]
    for c in codigo:
        contenido = open(os.path.join(RAIZ, c), encoding="utf-8").read().rstrip("\n")
        listado.append(f'<a id="{id_de(c)}"></a>\n\n## `{c}`\n\n```python\n{contenido}\n```\n')
    trozos.append("\n".join(listado))
    return "\n\n".join(trozos), docs, codigo


# ---------------------------------------------------------------------------
# 3. Portada y estilos
# ---------------------------------------------------------------------------

def contar_capitulos():
    indice = open(os.path.join(RAIZ, "libro", "00-indice-general.md"), encoding="utf-8").read()
    total = len(re.findall(r"^- \d+\.\d+ [★◇]", indice, re.M))
    hechos = len(re.findall(r"^- \d+\.\d+ [★◇] ✅", indice, re.M))
    return hechos, total


def portada(entrega, fecha, version_pdf):
    hechos, total = contar_capitulos()
    nota_soluciones = (
        "En esta versión <b>PDF</b> las soluciones aparecen <b>desplegadas</b> en recuadros "
        "titulados «▶ Ver solución». Tápalas con un papel y no las mires hasta haber "
        "intentado cada ejercicio."
        if version_pdf else
        "En esta versión <b>HTML</b> las soluciones están <b>plegadas</b>: pulsa «▶ Ver solución» "
        "solo después de intentar cada ejercicio. Funciona sin conexión a Internet."
    )
    return f"""
<section class="portada">
  <p class="portada-serie">Curso-libro de estudio</p>
  <h1 class="portada-titulo">Matemáticas, programación<br>y teoría de códigos</h1>
  <p class="portada-sub">De 3.º de ESO a la investigación sobre<br>códigos lineales sobre GF(7)</p>
  <div class="portada-caja">
    <p><b>Edición: Entrega {entrega}</b> · generada el {fecha}</p>
    <p><b>Estado del libro:</b> {hechos} de {total} capítulos redactados. Este documento contiene
       <b>todo lo escrito hasta ahora</b>: el plan completo del libro (índice de {total} capítulos),
       el mapa de prerrequisitos, el sistema de estudio, los capítulos redactados, los apéndices
       (glosario, fórmulas, errores frecuentes, bibliografía), el registro de progreso y el código
       de verificación. Los capítulos pendientes se añadirán en las próximas entregas.</p>
    <p>{nota_soluciones}</p>
  </div>
  <p class="portada-pie">Redactado con ayuda de una IA (Claude, de Anthropic). Todos los cálculos
     se comprueban con los programas del apéndice de código.</p>
</section>
"""


CSS = r"""
:root { --tinta:#1d2430; --suave:#5b6474; --acento:#1f5fa8; --fondo-codigo:#f4f6f9;
        --borde:#d5dbe3; --caja:#f3f7fd; --aviso:#fff8e6; }
html { font-size: 11pt; }
body { font-family: "DejaVu Sans", "Liberation Sans", Arial, sans-serif; color: var(--tinta);
       line-height: 1.5; max-width: 52em; margin: 0 auto; padding: 1.5em 1.2em 4em;
       background: #fff; hyphens: auto; }
h1, h2, h3, h4 { font-family: "DejaVu Serif", "Liberation Serif", Georgia, serif; color: #12355e;
       line-height: 1.25; break-after: avoid; }
h1 { font-size: 1.9em; border-bottom: 3px solid var(--acento); padding-bottom: .25em; margin-top: 1.6em; }
h2 { font-size: 1.4em; border-bottom: 1px solid var(--borde); padding-bottom: .15em; margin-top: 1.6em; }
h3 { font-size: 1.15em; margin-top: 1.3em; }
a { color: var(--acento); text-decoration: none; }
a:hover { text-decoration: underline; }
p, li { orphans: 3; widows: 3; }
blockquote { margin: 1em 0; padding: .55em 1em; background: var(--caja); color: var(--tinta);
       border-left: 4px solid var(--acento); border-radius: 0 6px 6px 0; break-inside: avoid; }
blockquote p { margin: .4em 0; }
code { font-family: "DejaVu Sans Mono", "Liberation Mono", monospace; font-size: .9em;
       background: var(--fondo-codigo); padding: .05em .25em; border-radius: 3px; }
pre { font-family: "DejaVu Sans Mono", "Liberation Mono", monospace; background: var(--fondo-codigo);
      border: 1px solid var(--borde); border-radius: 6px; padding: .7em .8em; line-height: 1.25;
      overflow-x: auto; white-space: pre; }
pre code { background: none; padding: 0; font-size: 1em; }
div.sourceCode { margin: 1em 0; }
pre a { color: inherit; }
table { border-collapse: collapse; margin: 1em 0; font-size: .92em; width: auto; max-width: 100%; }
th, td { border: 1px solid var(--borde); padding: .3em .55em; vertical-align: top; }
th { background: #e8eef7; }
tr:nth-child(even) td { background: #fafbfd; }
thead { display: table-header-group; }
tr { break-inside: avoid; }
details { border: 1px solid var(--borde); border-radius: 6px; margin: .8em 0; padding: .2em .9em;
          background: #fcfcfd; }
details[open] { padding-bottom: .6em; }
summary { cursor: pointer; font-weight: bold; color: var(--acento); padding: .35em 0; }
hr { border: none; border-top: 1px solid var(--borde); margin: 2em 0; }
nav#TOC { border: 1px solid var(--borde); border-radius: 8px; padding: .5em 1.2em 1em; background: #fbfcfe; }
nav#TOC > ul { padding-left: 1em; }
nav#TOC ul { list-style: none; }
nav#TOC li { margin: .15em 0; }
nav#TOC > ul > li > a { font-weight: bold; }
#TOC-title, #toc-title { border: none; }
.portada { text-align: center; padding: 3em 1em 2em; }
.portada-serie { text-transform: uppercase; letter-spacing: .2em; color: var(--suave); font-size: .9em; }
.portada-titulo { font-size: 2.6em; border: none; margin: .3em 0; color: #12355e; }
.portada-sub { font-size: 1.3em; color: var(--suave); font-family: "DejaVu Serif", serif; }
.portada-caja { text-align: left; margin: 2.5em auto 1.5em; max-width: 36em; background: var(--caja);
       border: 1px solid var(--borde); border-radius: 10px; padding: .6em 1.4em; }
.portada-pie { color: var(--suave); font-size: .85em; margin-top: 2em; }
.boton-soluciones { position: fixed; right: 1em; bottom: 1em; background: var(--acento); color: #fff;
       border: none; border-radius: 20px; padding: .6em 1em; font-size: .9em; cursor: pointer;
       box-shadow: 0 2px 6px rgba(0,0,0,.25); }

@media print {
  html { font-size: 10pt; }
  body { max-width: none; margin: 0; padding: 0; }
  pre { overflow: visible; }
  h1 { break-before: page; }
  .portada { break-after: page; padding-top: 6em; }
  .portada-titulo { break-before: avoid; }
  nav#TOC { break-after: page; border: none; background: none; padding: 0; }
  details { break-inside: auto; }
  summary { list-style: none; }
  summary::-webkit-details-marker { display: none; }
  .boton-soluciones { display: none; }
  a { color: var(--acento); }
}
@page { size: A4; margin: 16mm 16mm 18mm 16mm;
  @bottom-center { content: counter(page) " / " counter(pages);
                   font-family: "DejaVu Sans", sans-serif; font-size: 8pt; color: #5b6474; } }
@page :first { @bottom-center { content: none; } }
"""

BOTON_JS = """
<button class="boton-soluciones" id="boton-soluciones" type="button">Desplegar todas las soluciones</button>
<script>
(function () {
  var b = document.getElementById('boton-soluciones');
  var abiertas = false;
  b.addEventListener('click', function () {
    abiertas = !abiertas;
    document.querySelectorAll('details').forEach(function (d) { d.open = abiertas; });
    b.textContent = abiertas ? 'Plegar todas las soluciones' : 'Desplegar todas las soluciones';
  });
})();
</script>
"""


# ---------------------------------------------------------------------------
# 4. Ajustes posteriores del HTML
# ---------------------------------------------------------------------------

ANCHO_UTIL_PT = 470.0      # ancho disponible dentro de un bloque de código en A4 (aprox.)
AVANCE_MONO = 0.602        # ancho de un carácter de DejaVu Sans Mono, en «em»


def ajustar_bloques_de_codigo(html_texto):
    """Reduce la letra de cada bloque de código lo justo para que su línea más larga
    quepa en una página A4 (solo afecta a la impresión)."""
    reglas = []
    contador = [0]

    def cambiar(m):
        apertura, contenido = m.group(1), m.group(2)
        texto = html.unescape(re.sub(r"<[^>]+>", "", contenido))
        columnas = max((len(l) for l in texto.split("\n")), default=0)
        tam = min(9.0, ANCHO_UTIL_PT / (AVANCE_MONO * max(columnas, 1)))
        contador[0] += 1
        clase = f"pre-{contador[0]}"
        reglas.append(f"  pre.{clase} {{ font-size: {tam:.2f}pt; }}")
        if 'class="' in apertura:
            apertura = apertura.replace('class="', f'class="{clase} ', 1)
        else:
            apertura = apertura.replace("<pre", f'<pre class="{clase}"', 1)
        return apertura + contenido + "</pre>"

    nuevo = re.sub(r"(<pre[^>]*>)(.*?)</pre>", cambiar, html_texto, flags=re.S)
    estilo = "<style>\n@media print {\n" + "\n".join(reglas) + "\n}\n</style>\n</head>"
    return nuevo.replace("</head>", estilo, 1)


def abrir_soluciones(html_texto):
    return re.sub(r"<details>", "<details open>", html_texto)


# ---------------------------------------------------------------------------
# 5. Programa principal
# ---------------------------------------------------------------------------

def buscar_chrome(indicado):
    candidatos = [indicado] if indicado else []
    candidatos += glob.glob("/opt/pw-browsers/chromium-*/chrome-linux/chrome")
    candidatos += [shutil.which(n) for n in ("chromium", "chromium-browser", "google-chrome", "chrome")]
    for c in candidatos:
        if c and os.path.exists(c):
            return c
    return None


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--entrega", required=True, help="número de entrega (aparece en la portada y en los nombres)")
    ap.add_argument("--fecha", required=True, help="fecha que aparece en la portada, p. ej. 13/10/2026")
    ap.add_argument("--chrome", help="ruta de Chromium/Chrome")
    ap.add_argument("--salida", default=os.path.join(RAIZ, "descargas"))
    args = ap.parse_args()

    if not shutil.which("pandoc"):
        sys.exit("Falta pandoc (https://pandoc.org).")
    os.makedirs(args.salida, exist_ok=True)
    nombre = f"libro-gf7-entrega-{args.entrega}"
    md, docs, codigo = construir_markdown(args.entrega)

    with tempfile.TemporaryDirectory() as tmp:
        ruta_md = os.path.join(tmp, "libro.md")
        open(ruta_md, "w", encoding="utf-8").write(md)
        open(os.path.join(tmp, "estilo.html"), "w", encoding="utf-8").write(
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n<style>' + CSS + "</style>")

        salidas = {}
        for version_pdf in (False, True):
            open(os.path.join(tmp, "portada.html"), "w", encoding="utf-8").write(
                portada(args.entrega, args.fecha, version_pdf))
            ruta_html = os.path.join(tmp, "imprimible.html" if version_pdf else "interactivo.html")
            orden = ["pandoc", ruta_md, "-f", "gfm", "-t", "html5", "--standalone",
                     "--toc", "--toc-depth=2",
                     "-M", "pagetitle=Matemáticas, programación y teoría de códigos — Entrega " + args.entrega,
                     "-M", "toc-title=Índice de este documento", "-M", "lang=es",
                     "-H", os.path.join(tmp, "estilo.html"),
                     "-B", os.path.join(tmp, "portada.html"),
                     "-o", ruta_html]
            if not version_pdf:
                open(os.path.join(tmp, "boton.html"), "w", encoding="utf-8").write(BOTON_JS)
                orden += ["-A", os.path.join(tmp, "boton.html")]
            subprocess.run(orden, check=True)
            texto = open(ruta_html, encoding="utf-8").read()
            texto = ajustar_bloques_de_codigo(texto)
            if version_pdf:
                texto = abrir_soluciones(texto)
            open(ruta_html, "w", encoding="utf-8").write(texto)
            salidas[version_pdf] = ruta_html

        destino_html = os.path.join(args.salida, nombre + ".html")
        shutil.copy(salidas[False], destino_html)
        print("HTML:", os.path.relpath(destino_html, RAIZ))

        chrome = buscar_chrome(args.chrome)
        destino_pdf = os.path.join(args.salida, nombre + ".pdf")
        if chrome:
            subprocess.run([chrome, "--headless=new", "--no-sandbox", "--disable-gpu",
                            "--no-pdf-header-footer", "--generate-pdf-document-outline",
                            "--run-all-compositor-stages-before-draw", "--virtual-time-budget=20000",
                            f"--print-to-pdf={destino_pdf}", "file://" + salidas[True]],
                           check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print("PDF: ", os.path.relpath(destino_pdf, RAIZ))
        else:
            print("Aviso: no se encontró Chromium; no se ha generado el PDF.", file=sys.stderr)

    # ZIP con todo el repositorio (sin .git ni ZIP anteriores)
    destino_zip = os.path.join(args.salida, nombre + "-fuentes.zip")
    with zipfile.ZipFile(destino_zip, "w", zipfile.ZIP_DEFLATED) as z:
        for carpeta, subcarpetas, archivos in os.walk(RAIZ):
            subcarpetas[:] = [s for s in subcarpetas if s not in (".git", "__pycache__")]
            for a in archivos:
                ruta = os.path.join(carpeta, a)
                rel = os.path.relpath(ruta, RAIZ)
                if rel.endswith(".zip") or rel.endswith(".pyc"):
                    continue
                z.write(ruta, os.path.join(nombre, rel))
    print("ZIP: ", os.path.relpath(destino_zip, RAIZ))
    print(f"Documentos incluidos: {len(docs)} · programas: {len(codigo)}")


if __name__ == "__main__":
    main()
