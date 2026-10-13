# Registro de progreso

> Este archivo tiene **dos registros separados**, porque escribir un capítulo y dominarlo son cosas
> distintas:
>
> - **Registro de redacción:** qué partes del libro están escritas (lo actualiza quien redacta).
> - **Registro de aprendizaje:** qué capítulos has **dominado tú**, con tus puntuaciones y errores
>   (lo actualizas tú, o tu tutor con tus resultados).
>
> Última actualización: **12/10/2026 — Entrega 1**.

---

## 1. Índice general (resumen)

El índice completo, con enlaces, está en [`libro/00-indice-general.md`](libro/00-indice-general.md).

| Parte | Módulos | Capítulos | Redactados |
|---|---|---|---|
| I. Fundamentos de ESO | 1–5 | 46 | 1 (1.1) |
| II. Programación | 6–9 | 38 | 0 |
| III. Discretas y álgebra lineal | 10–13 | 45 | 0 |
| IV. Números y polinomios | 14–16 | 25 | 0 |
| V. Teoría de códigos | 17–23 | 62 | 0 |
| VI. Buscador de códigos | 24–28 | 38 | 0 |
| VII. Investigación autónoma | 29–32 | 32 | 0 |
| **Total** | 32 | **286** | **1** |

---

## 2. Registro de redacción

| Campo | Estado |
|---|---|
| **Último capítulo redactado** | 1.1 — Los conjuntos de números: ℕ, ℤ, ℚ y ℝ |
| **Próximo capítulo a redactar** | 1.2 — Números enteros: signos, valor absoluto, orden y jerarquía de operaciones |
| **Documentos de apoyo creados** | Índice general · Mapa de prerrequisitos · Cómo estudiar este libro · Glosario · Hoja de fórmulas · Errores frecuentes · Bibliografía · Este registro |
| **Código creado** | `codigo/verificaciones/verificar_cap_1_1.py` · `codigo/ejemplos/cap_1_1_rincon_del_ordenador.py` |
| **Versiones descargables** | `descargas/libro-gf7-entrega-1.pdf`, `.html` y `-fuentes.zip`, generadas con `herramientas/construir_libro.py` (13/10/2026). |
| **Verificaciones ejecutadas** | `verificar_cap_1_1.py` con Python 3.13.16 el 12/10/2026: **todas las comprobaciones superadas** (incluida la comprobación del criterio del denominador en 124 750 fracciones). |

### Entregas

| Entrega | Fecha | Contenido |
|---|---|---|
| 1 | 12/10/2026 | Índice general completo, mapa de prerrequisitos, sistema de estudio, apéndices iniciales, **capítulo 1.1 completo** con verificación por programa. |
| 1 (descargas) | 13/10/2026 | Primeras versiones descargables (PDF, HTML, ZIP) con todo lo redactado en la Entrega 1. |
| 2 (prevista) | — | Capítulos 1.2 y 1.3 (enteros; fracciones). |
| 3 (prevista) | — | Capítulos 1.4 y 1.5 (decimales y partes enteras; potencias). |
| 4 (prevista) | — | Capítulos 1.6–1.8 y Repaso R1. |
| Siguientes | — | Se seguirá el **orden de estudio recomendado** del mapa de prerrequisitos (Etapa 1: M1 → M2, con M6 en paralelo desde 2.5). |

---

## 3. Conceptos ya explicados en el libro

| Concepto | Capítulo | Nivel de tratamiento |
|---|---|---|
| Conjunto, elemento, ∈, ∉, subconjunto ⊂ | 1.1 | Intuitivo (formal en 11.1) |
| ℕ (con 0), ℤ, ℚ, ℝ, irracionales 𝕀 | 1.1 | Completo para ESO; construcción rigurosa de ℝ solo mencionada |
| Opuesto | 1.1 | Completo |
| Fracciones equivalentes, fracción irreducible | 1.1 | Presentado (operaciones a fondo en 1.3) |
| Decimales exactos, periódicos puros y mixtos; periodo, anteperiodo | 1.1 | Completo |
| Fracción generatriz (método de restar y regla clásica) | 1.1 | Completo |
| Criterio del denominador (2 y 5) | 1.1 | Enunciado; demostrada la parte «exacto»; resto pendiente (2.3, 14.6) |
| Cota del periodo (≤ b − 1) y argumento de los restos | 1.1 | Completo, con demostración |
| Orden en ℝ; comparación de fracciones | 1.1 | Completo |
| Densidad de ℚ (punto medio) | 1.1 | Completo, con demostración |
| Operación cerrada; contraejemplo | 1.1 | Completo |
| Ejemplo, evidencia computacional y demostración | 1.1 | Introducido (a fondo en 10.10) |
| Irracionalidad de √2 (reducción al absurdo) | 1.1 | Demostración en ampliación (método formal en 10.7) |
| 0,(9) = 1 | 1.1 | Completo |
| `float` frente a aritmética exacta; versiones de Python | 1.1 | Introducido (a fondo en 6.2, 8.7, 9.5) |
| [AVANCE] «Reloj de 7» (GF(7)): ⊕, ⊗, parejas (inversos) | 1.1 | Solo avance (formal en 2.8, 13.1–13.4) |
| [AVANCE] Principio del palomar | 1.1 | Solo idea (formal en 11.6) |

---

## 4. Decisiones de organización del libro

| N.º | Decisión | Motivo |
|---|---|---|
| D1 | Formato Markdown en un repositorio Git, un archivo por capítulo. | Versionable, legible en GitHub, fácil de ampliar por entregas. |
| D2 | Notación con símbolos Unicode, no LaTeX. | Se lee en cualquier visor, también fuera de GitHub. |
| D3 | 0 ∈ ℕ. | Convenio habitual en informática y en teoría de códigos (peso 0, índice 0). Se avisa de que otros libros usan otro convenio. |
| D4 | Coma decimal en el texto y punto en el código; periodo entre paréntesis: 0,41(6). | Convenio español + compatible con teclado y programas. |
| D5 | Etiquetas obligatorias: DEFINICIÓN, PROPIEDAD (demostrada / pendiente), HECHO ACEPTADO, CONJETURA, VERIFICADO POR PROGRAMA, EJEMPLO, AVANCE. | Requisito del proyecto: no presentar nunca una conjetura como teorema. |
| D6 | Soluciones plegadas (`<details>`) dentro de §14 y respuestas de la prueba de dominio en un anexo al final del capítulo. | Respetar el orden obligatorio de las 17 secciones y, a la vez, evitar ver las soluciones por accidente. |
| D7 | Cada capítulo con cálculos tiene un programa de verificación independiente; se indica versión de Python y fecha de ejecución. | Comprobar cada resultado por un segundo procedimiento y no afirmar nunca salidas no ejecutadas. |
| D8 | Solo biblioteca estándar de Python. | Evitar dependencias externas innecesarias. |
| D9 | Se añaden 29 temas marcados con [+] (28 capítulos o apartados y un apéndice) que faltaban en el temario (ver mapa de prerrequisitos, §4). | Ningún concepto debe usarse antes de haberse enseñado. |
| D10 | La numeración de módulos respeta el temario original; el **orden de estudio** recomendado intercala módulos (etapas 1–7). | Mantener la correspondencia con el temario pedido y, a la vez, llegar antes a la práctica con códigos sobre GF(7). |
| D11 | Criterio de dominio: ≥ 8/10 y todas las preguntas ★; «prueba de salto» con ≥ 9/10. | Progresar por comprensión demostrada, no por capítulos leídos; no hacer perder tiempo con lo ya sabido. |
| D12 | Marcas ★ (núcleo) y ◇ (ampliación) en el índice. | Indicar qué es imprescindible para el proyecto y qué es extensión. |
| D13 | Cada referencia bibliográfica lleva su estado de verificación. | No inventar ni dar por comprobadas fuentes que no se han comprobado. |
| D14 | Versiones descargables (PDF, HTML de un solo archivo y ZIP) generadas automáticamente desde el Markdown con `herramientas/construir_libro.py` en cada entrega. | Poder estudiar sin conexión y en papel sin mantener copias a mano que se desincronicen. |
| D15 | En el Markdown, las líneas que deben verse separadas (apartados a), b)…, enunciado y datos) terminan en «\\» (salto de línea forzado), y los recuadros de definición separan título, fórmula y explicación en párrafos. | Que se lean igual de bien en GitHub, en el HTML y en el PDF. |

---

## 5. Registro de aprendizaje (lo rellenas tú)

**Último capítulo dominado:** — (ninguno todavía)\
**Capítulo que estoy estudiando:** 1.1\
**Próximo capítulo a estudiar:** 1.1 → después 1.2

### 5.1. Estado por capítulo

| Capítulo | Empezado | Prueba de dominio (fecha y nota) | ¿Todas las ★? | ¿Dominado? | Repasar el día |
|---|---|---|---|---|---|
| 1.1 | | | | | |

### 5.2. Ejercicios realizados

| Capítulo | Ejercicios hechos | Acertados | Fallados |
|---|---|---|---|
| 1.1 | | | |

### 5.3. Errores que debo repasar

| Fecha | Capítulo / ejercicio | Qué hice | Concepto que fallaba | Ejercicio de refuerzo hecho | ¿Superado? |
|---|---|---|---|---|---|
| | | | | | |

### 5.4. Módulos completados y pendientes de repaso

| Módulo | Estado | Repaso acumulativo (R*n*) | Nota |
|---|---|---|---|
| 1 | En curso | Pendiente | |
