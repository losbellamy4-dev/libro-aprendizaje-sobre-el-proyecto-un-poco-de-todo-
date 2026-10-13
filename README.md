# Matemáticas, programación y teoría de códigos

### Un curso-libro progresivo: de 3.º de ESO a la investigación sobre códigos lineales sobre GF(7)

Este repositorio contiene un **libro de estudio completo**, escrito por entregas, para aprender las matemáticas y la programación necesarias para **comprender, desarrollar, verificar y mejorar** una investigación sobre códigos lineales con parámetros [n, k, d] sobre el campo finito GF(7): calcular distancias mínimas, generar matrices, buscar mejores códigos y comprobar con rigor si un resultado es realmente nuevo.

El punto de partida es **3.º de ESO** (Andalucía). Cada concepto se explica desde cero, con ejemplos resueltos paso a paso, ejercicios de tres niveles con soluciones razonadas, pruebas de dominio y programas en Python que **verifican** los cálculos.

---

## Por dónde empezar

1. Lee **[Cómo estudiar este libro](libro/00-como-estudiar-este-libro.md)** (10 minutos): explica el sistema de aprendizaje y el criterio para avanzar.
2. Echa un vistazo al **[índice general](libro/00-indice-general.md)** y al **[mapa de prerrequisitos y orden de estudio](libro/00-mapa-de-prerrequisitos.md)**.
3. Empieza por el **[Capítulo 1.1 — Los conjuntos de números: ℕ, ℤ, ℚ y ℝ](libro/parte-1-fundamentos-eso/modulo-01-numeros-y-operaciones/cap-1-1-conjuntos-de-numeros.md)**.
4. Anota tu avance en **[PROGRESO.md](PROGRESO.md)**.

## Descargar el libro

En la carpeta [`descargas/`](descargas/) tienes todo lo escrito hasta ahora en tres formatos:

| Archivo | Para qué sirve |
|---|---|
| [`libro-gf7-entrega-1.pdf`](descargas/libro-gf7-entrega-1.pdf) | Leer en el móvil, la tableta o imprimir. Las soluciones aparecen desplegadas en recuadros (tápalas antes de intentar cada ejercicio). |
| [`libro-gf7-entrega-1.html`](descargas/libro-gf7-entrega-1.html) | Un solo archivo que se abre con cualquier navegador, sin conexión. Las soluciones están plegadas y se despliegan con un clic. |
| [`libro-gf7-entrega-1-fuentes.zip`](descargas/libro-gf7-entrega-1-fuentes.zip) | Todo el repositorio: textos en Markdown, programas de Python, PDF y HTML. |

Las descargas se regeneran con cada entrega mediante `python3 herramientas/construir_libro.py --entrega N --fecha DD/MM/AAAA` (necesita pandoc y Chromium).

## Estructura del libro

| Parte | Contenido | Módulos |
|---|---|---|
| I | Fundamentos matemáticos de ESO | 1–5 |
| II | Programación y pensamiento computacional (Python) | 6–9 |
| III | Matemáticas discretas y álgebra lineal (también sobre campos finitos) | 10–13 |
| IV | Teoría de números y polinomios; construcción de campos finitos | 14–16 |
| V | **Teoría de códigos desde cero** (prioridad central) | 17–23 |
| VI | Construir un buscador real de códigos | 24–28 |
| VII | Investigación matemática autónoma y proyecto final | 29–32 |

## Estado actual

**Entrega 1 (12/10/2026):** índice completo (286 capítulos), mapa de prerrequisitos, sistema de estudio, apéndices iniciales y **capítulo 1.1 completo**. El detalle está en [PROGRESO.md](PROGRESO.md).

## Organización del repositorio

```
README.md                  ← este archivo
PROGRESO.md                ← registro de redacción y de aprendizaje
libro/
  00-indice-general.md
  00-mapa-de-prerrequisitos.md
  00-como-estudiar-este-libro.md
  parte-1-fundamentos-eso/
    modulo-01-numeros-y-operaciones/
      cap-1-1-conjuntos-de-numeros.md
apendices/
  glosario.md · hoja-de-formulas.md · errores-frecuentes.md · bibliografia.md
codigo/
  README.md
  ejemplos/                ← pequeños programas que aparecen en los capítulos
  verificaciones/          ← programas que recalculan los resultados de cada capítulo
descargas/                 ← el libro en PDF, HTML y ZIP
herramientas/
  construir_libro.py       ← genera las descargas a partir de los textos
```

## Verificar los cálculos

Solo hace falta Python 3 (sin bibliotecas externas):

```
python3 codigo/verificaciones/verificar_cap_1_1.py
```

## Sobre la autoría y el uso de IA

El texto de este libro se ha redactado con ayuda de una IA (Claude, de Anthropic), siguiendo un plan pedagógico definido por el autor del repositorio. Todos los cálculos numéricos se comprueban con programas incluidos en `codigo/verificaciones/`, y cada referencia bibliográfica indica si se ha podido verificar. Si encuentras un error, anótalo: detectar errores (también los de una IA) es una de las habilidades que este libro quiere enseñar.
