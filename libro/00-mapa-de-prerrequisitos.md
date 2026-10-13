# Mapa de prerrequisitos y orden de estudio

> Este documento responde a tres preguntas: **¿qué necesito saber antes de cada módulo?**,
>
> **¿falta algún prerrequisito en el temario?** y **¿en qué orden conviene estudiar?**
>
> Vuelve a él cada vez que empieces un módulo nuevo.

---

## 1. Mapa general de módulos

Una flecha **A ──► B** significa «A es prerrequisito de B». Las líneas punteadas (┄) indican prerrequisitos recomendados pero no imprescindibles.

```
 PARTE I (ESO)                    PARTE II (PROGRAMACIÓN)
 ─────────────                    ───────────────────────
 M1 Números ──► M2 Divisibilidad ──────────────► M6 Python ──► M7 Prog. matemática
  │                │                                             │
  ▼                │                                             ▼
 M3 Álgebra ───────┼──► M4 Funciones y lógica ──► M5 Combinat. ──► M8 Algoritmos ──► M9 Investig.
  │                │          │                     │               ▲                computacional
  │                │          │                     └───────────────┘                    │
  │                │          ▼                                                          │
  │                │   PARTE III                                                         │
  │                │   M10 Lógica y demostraciones ──► M11 Conjuntos y relaciones        │
  │                │          │                               │                          │
  ▼                │          ▼                               ▼                          │
 (sistemas) ───────┼──► M12 Vectores y matrices ──────► M13 Álg. lineal sobre GF(p) ◄────┤ (M7)
                   │                                          │                          │
                   ▼        PARTE IV                          │                          │
            M14 Aritm. modular avanzada ──► M15 Polinomios ──► M16 Campos finitos        │
                                                              │        │                 │
 PARTE V (CÓDIGOS)                                            ▼        │                 │
 M17 Códigos correctores ──► M18 Códigos lineales ──► M19 Distancia y peso               │
   ▲ (M5, M11)                       │                        │        │                 │
                                     ▼                        ▼        ▼                 │
                              M20 Matrices G y H ──► M21 Cotas ──► M22 Familias          │
                                     │                                 │                 │
                                     └──────────► M23 Códigos sobre GF(7) ◄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘
                                                         │
 PARTE VI (BUSCADOR)                                     ▼
 M24 Arquitectura ──► M25 Algoritmos exactos ──► M26 Heurísticas ──► M27 Extensión ──► M28 Validación
                                                                                          │
 PARTE VII (INVESTIGACIÓN AUTÓNOMA)                                                       ▼
 M29 Leer artículos ┄┄► M30 Diseñar una investigación ──────────────────────────► M32 PROYECTO FINAL
 M31 Git y GitHub (transversal: se empieza pronto y se usa en todo el proyecto) ──────────┘
```

---

## 2. Tabla de prerrequisitos por módulo

| Módulo | Prerrequisitos imprescindibles | Recomendados | Desbloquea |
|---|---|---|---|
| M1 Números | Primaria, 1.º–2.º ESO | — | M2, M3, M6 |
| M2 Divisibilidad | M1 (1.1–1.3) | — | M6, M7, M13, M14 |
| M3 Álgebra | M1 | M2 | M4, M12, M15 |
| M4 Funciones, patrones y razonamiento | M1, M3 (3.1–3.8) | — | M5, M8, M10 |
| M5 Combinatoria y probabilidad | M1, M4 (4.6–4.7) | M2 | M8, M17, M19, M21 |
| M6 Python | M1, M2 (2.5) | — | M7 |
| M7 Programación matemática | M6, M2 (2.5–2.8) | M5 (5.1–5.3) | M8, M9, M13.12 |
| M8 Algoritmos y complejidad | M7, M4 (4.4–4.5) | M5 (5.9) | M9, M24–M26 |
| M9 Investigación computacional | M7, M8 (8.1–8.5) | M31 (31.1–31.3) | M24–M28 |
| M10 Lógica y demostraciones | M4 (4.8–4.10) | M2 | M11, M12, todos los teoremas posteriores |
| M11 Conjuntos y relaciones | M10 (10.1–10.4) | M2 (2.8) | M13, M17, M21 |
| M12 Vectores y matrices | M3 (3.9), M10 | M11 | M13 |
| M13 Álgebra lineal sobre GF(p) | M12, M2 (2.7–2.8), M11 (11.5) | M7 | M18–M20, M23 |
| M14 Aritmética modular avanzada | M2, M10, M11 (11.5) | M13 | M16 |
| M15 Polinomios | M3 (3.2–3.6), M13 (13.1–13.4) | M14 | M16, M22 |
| M16 Campos finitos | M14, M15 | — | M22 (cíclicos, BCH, RS sobre extensiones) |
| M17 Códigos correctores | M5 (5.1–5.6), M11 (11.3) | M10 | M18 |
| M18 Códigos lineales | M17, M13 | — | M19, M20 |
| M19 Distancia mínima y peso | M18, M5 (5.3) | M8 (8.3–8.4) | M20, M21, M25 |
| M20 Matrices G y H | M19, M13 (13.7–13.10), M12 (12.12, 12.14) | — | M21, M23 |
| M21 Cotas y parámetros | M20, M5 (5.3–5.4), M4 (4.5, 4.7), M1 (1.4: ⌈x⌉) | M11 (11.8) | M22, M27, M28 |
| M22 Familias de códigos | M21; para 22.5–22.9: M15, M16 | — | M23, M27 |
| M23 Códigos sobre GF(7) | M13, M18–M20 | M21, M22 | M24 |
| M24 Arquitectura de un buscador | M23, M9 | M31 | M25 |
| M25 Algoritmos exactos | M24, M8 | M19 (19.5–19.6) | M26 |
| M26 Heurísticas | M25, M7 (7.9) | M5 (5.8) | M27 |
| M27 Extensión y construcción | M21, M26 | M22 | M28 |
| M28 Validación científica | M25–M27, M9 | M10 (10.10) | M32 |
| M29 Leer artículos | M10, M18–M21 | M22 | M30 |
| M30 Diseñar una investigación | M9, M29 | M28 | M32 |
| M31 Git y GitHub | M6 | — | M9, M24, M32 |
| M32 Proyecto final | M28, M30, M31 | todos | — |

---

## 3. Cadenas críticas de conceptos

Estas son las «cadenas» que llevan desde lo que sabes hoy hasta los conceptos centrales de tu investigación. Si un eslabón falla, todo lo que viene después se tambalea.

**Cadena A — De los restos al campo GF(7):**\
1.1 (conjuntos de números, operación cerrada) → 1.2 (enteros) → 2.5 (división con resto) → 2.6 (Euclides) → 2.7 (Bézout) → 2.8 (aritmética modular) → 11.5 (clases de restos) → 13.1 (campo) → 13.3 (GF(7)) → 13.4 (inversos).

**Cadena B — Álgebra lineal:**\
3.9 (sistemas) → 12.1–12.2 (vectores, combinaciones lineales) → 12.5 (producto de matrices) → 12.7 (Gauss) → 12.8 (rango) → 12.9–12.11 (independencia, base, dimensión) → 13.7–13.9 (lo mismo sobre GF(p)).

**Cadena C — Códigos lineales:**\
11.3 (palabras como elementos de Aⁿ) → 17.4 (distancia de Hamming) → 17.5 (distancia mínima) → 18.1–18.5 (códigos lineales y matriz generadora) → 19.1–19.4 (peso y cálculo de d) → 20.1–20.6 (G, H, síndromes) → 21 (cotas).

**Cadena D — Programación para investigar:**\
6.x → 7.1–7.2 (aritmética modular en Python) → 7.4–7.5 (combinaciones y búsqueda exhaustiva) → 7.7–7.9 (aserciones, tests, semillas) → 8.3–8.6 (complejidad y optimización) → 9.x (método experimental) → 24–28 (buscador y validación).

**Cadena E — De los polinomios a los códigos cíclicos:**\
3.2–3.6 (polinomios) → 15.x (polinomios sobre un campo) → 16.4 (extensiones) → 22.5 (cíclicos) → 22.9 (constacíclicos, cuasicíclicos, cuasitwisted).

**Cadena F — Cotas:**\
1.4 (⌈x⌉) + 1.5 (potencias) + 4.5 (logaritmos) + 4.7 (Σ) + 5.3 (números combinatorios) → 17.6 (bolas de Hamming) → 21.2–21.5 (Singleton, Hamming, Griesmer, Gilbert–Varshamov).

---

## 4. Comprobación de prerrequisitos que faltaban en el temario original

Al diseñar el índice se revisó, concepto por concepto, **dónde se usa cada idea por primera vez y dónde se enseña antes**. Estas son las lagunas detectadas y cómo se han cubierto (marcadas con [+] en el índice):

| Concepto | Se necesita en | Problema detectado | Solución |
|---|---|---|---|
| Inverso módulo p | 13.4, 13.7 (Gauss mod p) | El Módulo 14 (aritmética modular avanzada) iba **después** del 13. | Nuevo cap. **2.7** (Bézout, Euclides extendido); 13.4 es autocontenido. El Módulo 14 profundiza después. |
| Partes enteras ⌊x⌋, ⌈x⌉ | 21.4 (cota de Griesmer), 19.5 | No aparecían. | Añadidas al cap. **1.4**. |
| Logaritmos | 8.4 (O grande), 18.7, 21.5 | No aparecían. | Nuevo cap. **4.5**. |
| Notación Σ y Π | 19.7, 21.3, 21.5 | No aparecía. | Nuevo cap. **4.7**. |
| Binomio de Newton | 19.7, 21.3 | No aparecía. | Nuevo cap. **5.4**. |
| Valor esperado | 26 (análisis de búsquedas aleatorias), 21.5 | No aparecía. | Nuevo cap. **5.8** (◇). |
| Principio del palomar | 1.1 (idea), 21, 25 | No aparecía. | Nuevo cap. **11.6**. |
| Permutaciones como funciones | 21.1 (códigos equivalentes), 24.4 | No aparecía. | Nuevo cap. **11.8**. |
| Producto escalar y ortogonalidad | 20.3–20.4 (matriz de control, código dual) | No aparecía. | Nuevos caps. **12.14** y **13.10**. |
| Determinantes | 22.7–22.8 (Vandermonde, Reed–Solomon) | No aparecían. | Nuevo cap. **12.13** (◇). |
| Grupos, orden, raíces primitivas | 16.6, 22.5–22.7 | No aparecían. | Nuevo cap. **14.6**. |
| Interpolación de Lagrange | 22.7 (Reed–Solomon) | No aparecía. | Nuevo cap. **15.8**. |
| Anillos | 16 (GF(p)[x]/(f)) | No aparecían. | Nuevo cap. **16.1**. |
| Polinomios mínimos, clases ciclotómicas | 22.5–22.6 (cíclicos, BCH) | No aparecían. | Nuevo cap. **16.7** (◇). |
| Ahorro por escalares (q^k − 1)/(q − 1) | 24–25 (eficiencia del buscador) | No aparecía. | Nuevo cap. **19.5**. |
| d mediante columnas de H | 20, 22.3 (Hamming) | No aparecía. | Nuevo cap. **19.6**. |
| Cotas de Griesmer y Plotkin | 21.8 (lectura de tablas), 21.9 | Faltaban: Griesmer es clave para códigos lineales. | Nuevos caps. **21.4** y **21.6** (◇). |
| Códigos símplex | 22.3, 27 | No aparecían. | Nuevo cap. **22.4**. |
| Códigos de Gray q-arios; Brouwer–Zimmermann | 25 (cálculo eficiente de d) | No aparecían. | Añadidos en **25.2** y **25.6** (◇). |
| Construcciones (u \| u+v), X | 27.6 (mejora de parámetros) | No aparecían. | Nuevo cap. **27.4** (◇). |
| Instalación y errores en Python | 6.x | Se daba por supuesto. | Nuevos caps. **6.1**, **6.11**, **6.12**. |
| Representación binaria | 1.1 (por qué falla 0,1), 8.6 | No aparecía. | Nuevo cap. **8.7** (◇). |
| Cómo redactar demostraciones | 10–30 | No aparecía. | Nuevo cap. **10.11**. |

---

## 5. Orden de estudio recomendado

La numeración de los módulos es **temática**. El orden de estudio es **pedagógico**: intercala matemáticas y programación para que pronto puedas experimentar, y llega a los códigos sobre GF(7) **antes** de estudiar los campos de extensión (que tu proyecto actual no necesita).

| Etapa | Qué estudiar | En paralelo | Hito al terminar |
|---|---|---|---|
| **1. Base numérica** | M1 → M2 | Desde 2.5: empezar M6 (6.1–6.5) | Sabes operar con restos a mano y escribir programas sencillos. |
| **2. Álgebra y Python** | M3 → M4 | M6 completo → M7; M31 (31.1–31.3) | **Hito 1:** calculas aritmética módulo 7 a mano y en Python, con tests. |
| **3. Contar y razonar** | M5 → M10 → M11 | M8 | Sabes contar posibilidades, estimar costes y escribir demostraciones sencillas. |
| **4. Álgebra lineal** | M12 → M13 | M9 | **Hito 2:** calculas rangos y resuelves sistemas sobre GF(7) a mano y con tu propia biblioteca probada. |
| **5. Primer recorrido por los códigos** | M17 → M18 → M19 → M20 → M23 | M32.1–32.7 (primeras piezas del proyecto) | **Hito 3:** calculas los parámetros [n, k, d]₇ de códigos pequeños y **verificas** resultados generados por una IA en casos pequeños. |
| **6. Teoría avanzada** | M14 → M15 → M16 → M21 → M22 | M29 | **Hito 4:** comparas tus códigos con las cotas teóricas y con las tablas de mejores códigos conocidos. |
| **7. Buscador e investigación** | M24 → M25 → M26 → M27 → M28 | M30, M31 completo | **Hito 5:** buscador reproducible, verificador independiente e informe con conclusiones proporcionadas a la evidencia (M32). |

**Estimación orientativa** (es una estimación, no un compromiso): con una media de 2–3 sesiones de 45–60 minutos por capítulo y 4 sesiones por semana, el recorrido completo lleva **varios años**. Pero no tienes que esperar al final para hacer cosas reales: el **Hito 3** (calcular y verificar parámetros de códigos pequeños sobre GF(7)) llega a mitad del camino, y los capítulos de Parte I que ya domines de clase se pueden superar rápidamente con la **prueba de salto** (ver [Cómo estudiar este libro](00-como-estudiar-este-libro.md)).

---

## 6. Qué mirar antes de empezar cada capítulo

Cada capítulo tiene una sección **«2. Prerrequisitos»** con una **comprobación rápida**. Regla práctica:

- Si fallas **una** pregunta de la comprobación rápida: repasa ese punto y sigue.
- Si fallas **dos o más**: vuelve al capítulo indicado y repite su prueba de dominio antes de continuar.
