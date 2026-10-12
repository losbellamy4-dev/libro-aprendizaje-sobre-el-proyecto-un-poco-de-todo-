# Cómo estudiar este libro

> **Idea central:** completar un capítulo no es lo mismo que dominarlo. Este libro está diseñado
> para que avances **solo cuando has demostrado que entiendes**, no cuando has terminado de leer.

---

## 1. El ciclo de cada capítulo

```
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ 0. Comprobación rápida de prerrequisitos (§2)                           │
  │        │ ¿fallas 2 o más? ──► vuelve al capítulo indicado               │
  │        ▼                                                                │
  │ 1. Lee la explicación intuitiva (§3) y las definiciones (§4)            │
  │ 2. Ejemplos resueltos (§7–9): TAPA la solución e intenta cada paso      │
  │ 3. Ejercicios nivel A ──► nivel B ──► problemas ──► nivel C (§13)       │
  │ 4. Corrige con las soluciones (§14) y anota tus errores                 │
  │ 5. Preguntas de comprensión (§15)                                       │
  │ 6. Prueba de dominio (§16), otro día, sin mirar nada                    │
  │        │                                                                │
  │   ¿≥ 8/10 y todas las ★?                                                │
  │     SÍ ──► marca el capítulo como DOMINADO en PROGRESO.md ──► siguiente │
  │     NO ──► tabla de diagnóstico ──► refuerzo ──► nueva prueba otro día  │
  └─────────────────────────────────────────────────────────────────────────┘
```

**Consejos prácticos:**

- Estudia con **papel y lápiz**. Las matemáticas se aprenden haciendo, no leyendo.
- Las soluciones están **plegadas** (en GitHub aparecen como «▶ Ver solución»). Ábrelas solo después de intentarlo de verdad. Equivocarse y descubrir por qué es la parte del estudio que más enseña.
- Lleva un **cuaderno de errores**: para cada error, escribe (1) qué hiciste, (2) por qué estaba mal, (3) qué concepto fallaba, (4) un ejercicio parecido resuelto bien.
- Haz la prueba de dominio **otro día**, no justo después de estudiar: así compruebas lo que recuerdas de verdad.

---

## 2. Los tres niveles de ejercicios

| Nivel | Qué exige | Ejemplo (capítulo 1.1) |
|---|---|---|
| **A** | Comprender y aplicar directamente una definición o un procedimiento. | Clasificar −12/4 en ℕ, ℤ, ℚ. |
| **B** | Combinar varios conceptos y resolver problemas que no has visto antes. | Decidir sin dividir si 21/56 da decimal exacto (hay que simplificar **y** aplicar el criterio). |
| **C** | Investigar: recoger datos, formular una conjetura, comprobarla, intentar refutarla y justificar las conclusiones. | Descubrir la relación entre el periodo de 1/p y p − 1. |

Además, cada capítulo incluye **2 problemas de aplicación práctica** y **1 problema combinado** con capítulos anteriores. Desde el capítulo 1.2, cada capítulo tendrá una sección **«Recupera»** con problemas nuevos sobre lo estudiado semanas atrás.

---

## 3. Criterio de dominio

Un capítulo está **dominado** cuando:

1. Has obtenido **8 puntos o más sobre 10** en la prueba de dominio.
2. Has respondido **correctamente todas las preguntas marcadas con ★** (conceptos críticos para lo que viene después).
3. Puedes **explicar con tus palabras** las respuestas a las preguntas de comprensión.

Si no se cumplen, **no avances** a los capítulos que dependen de él (consulta el [mapa de prerrequisitos](00-mapa-de-prerrequisitos.md)). Usa la **tabla de diagnóstico** del capítulo: te dice qué concepto falla, qué sección repasar y qué ejercicio de refuerzo hacer.

### Prueba de salto

Si un capítulo trata algo que ya has estudiado en clase, puedes intentar **directamente** su prueba de dominio. Si sacas **9 o más y todas las ★**, márcalo como dominado y lee solo su **ejemplo avanzado** (§9, la conexión con la investigación) y su sección de errores frecuentes. Esto permite avanzar rápido por la Parte I sin saltarse lagunas.

---

## 4. Repaso espaciado

Lo que no se repasa se olvida. Calendario recomendado para cada capítulo dominado:

| Cuándo | Qué hacer |
|---|---|
| Al día siguiente | Rehacer 2 ejercicios que fallaste. |
| A la semana | Resumen para memorizar (§11) de memoria + 1 problema «Recupera» del capítulo siguiente. |
| Al mes | Repaso acumulativo (R*n*) del módulo. |
| Al final de cada Parte | Examen acumulativo (EP-*X*). |

---

## 5. Cómo pedir corrección a tu tutor (o a una IA)

Las soluciones del libro muestran **una** forma correcta, pero no pueden ver **tu** razonamiento. Cuando quieras que te corrijan, envía:

```
Capítulo: 1.1      Ejercicio: A4 d)
Mi respuesta: 0,3(12) = 312/990 = 52/165
Mi razonamiento: multipliqué por 1000 y resté…
Duda concreta: no sé por qué no coincide al dividir.
```

Quien te corrija debe: (1) señalar **el concepto exacto** que falla (por ejemplo, «olvidaste restar el anteperiodo»), (2) explicarlo, y (3) darte **otro ejercicio parecido** para comprobar que lo has entendido. Si usas una IA para corregir, **comprueba sus cálculos tú mismo**: las IA también se equivocan (lo estudiarás a fondo en el capítulo 28.7).

---

## 6. Tipos de afirmaciones: aprende a distinguirlas

En todo el libro, cada afirmación lleva una etiqueta. Esta distinción es la base del trabajo científico:

| Etiqueta | Qué significa | ¿Se puede usar como verdad? |
|---|---|---|
| **[DEFINICIÓN]** | Acuerdo sobre el significado de una palabra o símbolo. | Es un acuerdo; comprueba que el autor que lees usa la misma. |
| **[PROPIEDAD — demostrada]** / **[TEOREMA]** | Demostrada en el libro. | Sí. |
| **[PROPIEDAD — demostración pendiente: …]** | Verdadera y conocida; se demostrará más adelante. | Sí, pero sabiendo que aún no has visto por qué. |
| **[HECHO ACEPTADO]** | Demostrado por matemáticos; demostración fuera del alcance del libro. | Sí, citando la fuente. |
| **[CONJETURA]** | Parece verdadera, pero no está demostrada. | **No.** Hay que demostrarla o refutarla. |
| **[VERIFICADO POR PROGRAMA]** | Comprobado en un número finito de casos. | Es evidencia, **no** demostración (salvo que el programa haya revisado **todos** los casos posibles de un problema finito, y el programa sea correcto). |
| **[EJEMPLO]** | Un caso concreto. | Ilustra; no demuestra afirmaciones generales. |
| **[AVANCE]** | Anticipo de un capítulo futuro. | No se exige dominarlo todavía. |

---

## 7. Convenios de notación del libro

- **0 ∈ ℕ**: en este libro los naturales empiezan en 0.
- **Coma decimal** en el texto (0,75); **punto** en los programas (`0.75`).
- Listas de decimales separadas por **punto y coma**: 0,5; 1,2.
- **Periodo entre paréntesis**: 0,41(6) = 0,41666…
- Signo menos tipográfico «−» en el texto; guion «-» en el código.
- Las fórmulas se escriben con símbolos Unicode (ℕ, ∈, ⊂, ≤, √, ⟺) en lugar de LaTeX, para que se lean bien en cualquier visor.
- Los capítulos se citan como «capítulo 13.4» (Módulo 13, capítulo 4).

---

## 8. El código del libro

- Todo el código usa **solo la biblioteca estándar de Python 3**: no hay que instalar nada más.
- Cada capítulo con cálculos tiene un programa de **verificación** en [`codigo/verificaciones/`](../codigo/verificaciones/) que recalcula sus resultados por un procedimiento independiente.
- Cuando el libro muestra la salida de un programa, indica **con qué versión de Python se ejecutó y cuándo**. Si una salida no se ha ejecutado realmente, se dice explícitamente.
- Hasta el Módulo 6 no necesitas entender el código: basta con ejecutarlo (`python3 nombre_del_archivo.py`) y ver que todo sale «OK».

---

## 9. Uso honesto de la IA

Este libro se ha redactado con ayuda de una IA (Claude, de Anthropic), y está pensado para que tú aprendas a **no depender** de ella:

- Usa la IA como **tutor**: para que te explique, te proponga ejercicios o revise tu razonamiento. No para que haga los ejercicios por ti.
- **Verifica** todo resultado importante por un segundo camino (a mano, con otro programa o con una fuente fiable).
- En tu investigación, **registra** qué partes ha hecho una IA y cuáles tú (capítulo 31.9).
