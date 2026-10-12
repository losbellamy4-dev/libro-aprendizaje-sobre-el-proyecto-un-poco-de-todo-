# Capítulo 1.1 — Los conjuntos de números: ℕ, ℤ, ℚ y ℝ

> **Parte I** · Fundamentos matemáticos de ESO · **Módulo 1** · Números y operaciones
> **Nivel:** 3.º ESO (punto de partida del libro) · **Tipo:** ★ núcleo imprescindible
> **Tiempo orientativo:** 5–6 sesiones de 45–60 minutos, repartidas en 4 unidades.
> **Verificación:** todos los cálculos de este capítulo se han comprobado con el programa
> [`codigo/verificaciones/verificar_cap_1_1.py`](../../../codigo/verificaciones/verificar_cap_1_1.py)
> (ejecutado con Python 3.13.16 el 12/10/2026: todas las comprobaciones superadas).

---

## Cómo está organizado este capítulo

| Unidad | Qué estudias | Secciones | Ejercicios recomendados |
|---|---|---|---|
| **A** (sesiones 1–2) | Naturales, enteros y racionales; clasificar números | §3, §4.1–4.2, §5, Ejemplo 1.1 | A1, A2 |
| **B** (sesiones 2–3) | Fracciones y decimales en los dos sentidos | §4.3, Propiedades 1.4–1.6, Ejemplo 1.2 | A3, A4, B2, B3 |
| **C** (sesión 4) | Irracionales, números reales, orden y densidad | §4.2 (Def. 1.6), §4.4, Prop. 1.3 | A5, B1, B4, B5, B6 |
| **D** (sesión 5) | Operaciones cerradas, contraejemplos y conexión con GF(7) | §4.5, Ejemplo 1.3 | A6, problemas, C1, C2 |
| **Cierre** (sesión 6) | Comprensión y prueba de dominio | §15, §16 | Prueba de dominio |

**Etiquetas que verás en todo el libro** (para distinguir siempre qué tipo de afirmación es cada cosa):

| Etiqueta | Significado |
|---|---|
| **[DEFINICIÓN]** | Un acuerdo sobre el significado de una palabra o símbolo. No se demuestra: se acuerda. |
| **[PROPIEDAD — demostrada]** / **[TEOREMA]** | Afirmación verdadera cuya demostración aparece en este libro (aquí o en el lugar indicado). |
| **[PROPIEDAD — demostración pendiente: …]** | Afirmación verdadera y conocida, cuya demostración necesita herramientas que todavía no tienes. Se indica dónde se demostrará. |
| **[HECHO ACEPTADO]** | Resultado demostrado por matemáticos, cuya demostración queda fuera del alcance de este libro. |
| **[CONJETURA]** | Afirmación que parece verdadera pero que **no** está demostrada (o que tú aún no has demostrado). |
| **[VERIFICADO POR PROGRAMA]** | Comprobado por ordenador en un número finito de casos. Es **evidencia**, no demostración. |
| **[EJEMPLO]** | Un caso concreto. Un ejemplo ilustra, pero no demuestra una afirmación general. |
| **[AVANCE]** | Idea de un capítulo futuro. No se exige dominarla todavía. |

> 📌 **Las soluciones están plegadas.** En GitHub aparecen como «▶ Ver solución»: pulsa solo
> cuando hayas intentado el ejercicio por tu cuenta. Las respuestas de la prueba de dominio
> están en el **anexo final** del capítulo.

---

<a id="s1"></a>
## 1. Título y objetivos

**Título:** Los conjuntos de números: naturales (ℕ), enteros (ℤ), racionales (ℚ) y reales (ℝ).

Al terminar este capítulo serás capaz de:

1. **Clasificar** cualquier número en ℕ, ℤ, ℚ, en los irracionales o en ℝ, y justificarlo.
2. **Explicar por qué existe cada conjunto**: qué problema no se podía resolver con el anterior.
3. **Convertir una fracción en decimal** y **predecir sin dividir** si el decimal será exacto, periódico puro o periódico mixto.
4. **Convertir un decimal exacto o periódico en fracción** (fracción generatriz) y comprobar el resultado por otro camino.
5. **Ordenar números** y situarlos en la recta numérica.
6. **Decidir si una operación es cerrada** en un conjunto y, si no lo es, dar un **contraejemplo**.
7. **Distinguir entre ejemplo, evidencia y demostración**, una habilidad que usarás durante todo el libro.
8. **Entender por qué los ordenadores se equivocan con algunos decimales** y por qué en tu investigación sobre GF(7) se trabaja solo con números enteros.
9. [AVANCE] **Ver por primera vez** un conjunto **finito** de números en el que se puede sumar, restar, multiplicar y dividir: la semilla de GF(7).

---

<a id="s2"></a>
## 2. Prerrequisitos

Este es el primer capítulo, así que solo necesitas lo que se aprende en Primaria y en 1.º–2.º de ESO:

- Sumar, restar, multiplicar y dividir números naturales.
- Hacer una **división con resto** (por ejemplo, 47 entre 5 da cociente 9 y resto 2, porque 47 = 9·5 + 2).
- Saber qué es una **fracción** y simplificar fracciones sencillas.
- Haber usado **números negativos** en contextos como temperaturas o plantas de un edificio.
- Saber qué es un **número primo** (un natural mayor que 1 cuyos únicos divisores son 1 y él mismo: 2, 3, 5, 7, 11, …). Lo usaremos solo en una propiedad; se estudia a fondo en el Módulo 2.

### Comprobación rápida de prerrequisitos

Responde sin calculadora. Si fallas **dos o más**, repasa esos puntos con tu libro de clase antes de seguir (o pide ayuda a tu tutor). Los capítulos 1.2, 1.3 y 2.5 los tratarán de nuevo con detalle.

1. ¿Cuánto es 36 : 4?
2. ¿Cuál es el resto de dividir 47 entre 5?
3. Simplifica 18/24 todo lo posible.
4. ¿Qué temperatura es más baja: −8 °C o −3 °C?
5. ¿Es 9 un número primo?
6. Escribe 0,25 como fracción.

<details>
<summary>▶ Ver respuestas de la comprobación rápida</summary>

1. 9, porque 9 · 4 = 36.
2. Resto 2, porque 47 = 9 · 5 + 2 y 2 < 5.
3. 18/24 = 3/4 (dividiendo numerador y denominador entre 6).
4. −8 °C es más baja (está más lejos del cero hacia abajo).
5. No: 9 = 3 · 3, así que 3 es un divisor distinto de 1 y de 9.
6. 0,25 = 25/100 = 1/4.

</details>

**Notación que usaremos** (decisiones del libro):

- Escribimos los decimales con **coma**, como en España: 0,75. Cuidado: en Python (y en casi todos los lenguajes de programación) se escribe con **punto**: `0.75`.
- Cuando escribamos una lista de decimales, los separaremos con **punto y coma** para no confundirnos: 0,5; 1,2; 3,75.
- Los decimales periódicos se escriben aquí con el **periodo entre paréntesis**: 0,41(6) significa 0,41666…, y 0,(27) significa 0,272727… En tu libro de clase verás el periodo marcado con un arco encima de las cifras; significa lo mismo. Usamos paréntesis porque se pueden escribir con cualquier teclado y en un programa.
- Usamos el signo menos tipográfico «−» en el texto; en los programas se escribe con el guion «-».

---

<a id="s3"></a>
## 3. Explicación intuitiva

### 3.1. La historia de los números es una historia de problemas sin respuesta

Imagina que los números son las **herramientas de una caja**. Cada vez que aparece un problema que las herramientas que tienes no pueden resolver, inventas una herramienta nueva y la añades a la caja. Las herramientas antiguas no se tiran: siguen dentro.

**Paso 1. Contar.** Para contar ovejas, alumnos o páginas usamos 0, 1, 2, 3, … Son los **números naturales**, ℕ. Con ellos siempre se puede **sumar** (3 + 5 = 8) y **multiplicar** (3 · 5 = 15) sin salir de ℕ.

**Paso 2. Restar sin límite.** ¿Cuánto es 5 − 8? Con los naturales **no hay respuesta**: no puedes quitar 8 ovejas de un rebaño de 5. Pero en la vida real sí tiene sentido: si tienes 5 € y gastas 8 €, debes 3 €; si estás en la planta 5 y bajas 8 plantas, llegas al sótano −3. Para que la resta **siempre** tenga respuesta, se añaden los negativos: −1, −2, −3, … Así nacen los **números enteros**, ℤ.

**Paso 3. Repartir sin límite.** ¿Cuánto es 7 : 2? En los enteros **no hay respuesta exacta**: no existe un entero que multiplicado por 2 dé 7. Pero si repartes 7 pizzas entre 2 personas, cada una come 3 pizzas y media: 7/2. Para que la división (entre un número distinto de cero) **siempre** tenga respuesta, se añaden las fracciones. Así nacen los **números racionales**, ℚ.

**Paso 4. Medir sin límite.** Dibuja un cuadrado de lado 1. ¿Cuánto mide su diagonal? Por el teorema de Pitágoras, su longitud d cumple d² = 1² + 1² = 2. Los griegos descubrieron algo sorprendente: **ninguna fracción** multiplicada por sí misma da exactamente 2. La diagonal existe (¡la puedes dibujar!), pero su longitud, √2, no es racional. Para que **toda longitud** tenga un número, se completan los racionales con los **irracionales** (√2, π, …). El conjunto completo son los **números reales**, ℝ.

```
   PROBLEMA SIN RESPUESTA                       SOLUCIÓN: AMPLIAR EL CONJUNTO
   ──────────────────────                       ─────────────────────────────
   5 − 8 = ?   (no cabe en ℕ)        ──────►    ℤ  = ℕ + los negativos
   7 : 2 = ?   (no cabe en ℤ)        ──────►    ℚ  = ℤ + las fracciones
   d · d = 2   (no cabe en ℚ)        ──────►    ℝ  = ℚ + los irracionales
```

Fíjate en el **patrón**: cada conjunto nuevo se inventa para que una operación que «fallaba» deje de fallar. Ese patrón es la idea más importante del capítulo.

### 3.2. El giro de tu investigación: ir en sentido contrario

En la teoría de códigos correctores de errores pasa algo curioso. No queremos conjuntos **infinitos** como ℚ o ℝ: un ordenador no puede guardar infinitos números ni infinitas cifras decimales. Queremos un conjunto **pequeño y finito** de símbolos (por ejemplo, solo siete: 0, 1, 2, 3, 4, 5 y 6) en el que, aun así, se pueda **sumar, restar, multiplicar y dividir** sin salirse nunca del conjunto, igual que en ℚ.

¿Es posible? Piensa en los **días de la semana**. Si hoy es lunes, dentro de 10 días será jueves, porque 10 = 7 + 3 y cada 7 días se vuelve al mismo día. Con los días de la semana «sumamos» y el resultado **siempre** vuelve a ser uno de los 7 días. Esa es la semilla de **GF(7)**, el campo finito de 7 elementos sobre el que trata tu investigación. Lo verás por primera vez en el Ejemplo 1.3 de este capítulo y lo estudiarás con todo detalle en los Módulos 2, 13 y 16.

### 3.3. Una segunda idea clave: exacto frente a aproximado

1/3 es un número **exacto**. Pero si lo escribes en decimal, 0,333…, necesitas **infinitas** cifras. Si te quedas con 0,333, estás usando una **aproximación**. Los ordenadores, con los decimales normales, hacen continuamente aproximaciones de este tipo, y eso puede producir resultados **falsos** en una investigación. En este capítulo aprenderás a reconocer cuándo un número tiene expresión decimal finita y cuándo no, y por qué en tu proyecto solo se usarán **números enteros**, con los que el ordenador es exacto.

---

<a id="s4"></a>
## 4. Definiciones formales

### 4.1. Un poco de lenguaje de conjuntos

> **[DEFINICIÓN 1.1] Conjunto y elemento.** Un **conjunto** es una colección de objetos en la que
> está perfectamente claro qué objetos están dentro y cuáles no. Cada objeto del conjunto se llama
> **elemento**. Si x es un elemento del conjunto A escribimos **x ∈ A** («x pertenece a A»); si no
> lo es, escribimos **x ∉ A** («x no pertenece a A»).

Un conjunto se puede describir **enumerando** sus elementos entre llaves, como {0, 1, 2, 3, 4, 5, 6}, o **describiendo una condición**, como «el conjunto de los números pares». El orden y las repeticiones no importan: {1, 2, 3} y {3, 1, 2, 2} son el mismo conjunto.

> **[DEFINICIÓN 1.2] Subconjunto.** Decimos que A es un **subconjunto** de B, y escribimos
> **A ⊂ B**, si todo elemento de A es también elemento de B.

- ∈ relaciona un **elemento** con un **conjunto**: 2 ∈ ℕ.
- ⊂ relaciona un **conjunto** con otro **conjunto**: {2} ⊂ ℕ, ℕ ⊂ ℤ.

(El estudio sistemático de los conjuntos llega en el Módulo 11. Por ahora basta con esto.)

### 4.2. Los cuatro conjuntos de números

> **[DEFINICIÓN 1.3] Números naturales.**
> **ℕ = {0, 1, 2, 3, 4, …}**
> Los puntos suspensivos significan «y así sucesivamente, sin fin»: ℕ es infinito.

⚠️ **Convenio importante.** Algunos libros no incluyen el 0 en ℕ y empiezan en 1. **En este libro el 0 es natural**, porque en informática y en teoría de códigos contamos desde 0 (la palabra de peso 0, la posición 0 de una lista…). Cuando un autor necesita dejar claro que no incluye el 0 suele escribir ℕ* o ℤ⁺ (enteros positivos). **Lección de investigador:** antes de usar un resultado, comprueba siempre qué definiciones usa el autor. Dos libros pueden decir cosas que parecen contradictorias solo porque definen la misma palabra de forma distinta.

> **[DEFINICIÓN 1.4] Números enteros.**
> **ℤ = {…, −3, −2, −1, 0, 1, 2, 3, …}**
> Son los naturales junto con sus **opuestos**. El **opuesto** de un número a es el número −a que
> cumple a + (−a) = 0. El opuesto de 5 es −5; el opuesto de −5 es 5; el opuesto de 0 es 0.

(La letra ℤ viene del alemán *Zahlen*, «números».)

> **[DEFINICIÓN 1.5] Números racionales.**
> **ℚ = { a/b : a ∈ ℤ, b ∈ ℤ, b ≠ 0 }**
> Se lee: «ℚ es el conjunto de todos los números de la forma a/b, tales que a es entero, b es entero
> y b es distinto de cero». En la fracción a/b, a es el **numerador** y b el **denominador**.

Tres aclaraciones imprescindibles:

1. **Fracciones equivalentes.** Muchas fracciones representan el **mismo** número racional: 1/2 = 2/4 = 3/6 = −5/−10. Dos fracciones a/b y c/d son iguales exactamente cuando **a · d = b · c** (los «productos cruzados» coinciden). Por ejemplo, 2/4 = 3/6 porque 2 · 6 = 12 = 4 · 3.
2. **Fracción irreducible.** Una fracción es **irreducible** si no se puede simplificar más, es decir, si el numerador y el denominador no tienen ningún divisor común mayor que 1. 3/4 es irreducible; 6/8 no lo es (ambos son divisibles entre 2). Todo número racional se puede escribir como fracción irreducible con denominador positivo, y de **una sola manera**.
3. **¿Por qué b ≠ 0?** Porque dividir entre 0 no tiene sentido: si 5/0 fuera un número x, tendría que cumplir x · 0 = 5, pero cualquier número multiplicado por 0 da 0. En cambio, 0/5 = 0 sin ningún problema (0 · 5 = 0).

(La letra ℚ viene de *quotient*, «cociente».)

> **[DEFINICIÓN 1.6] Números reales e irracionales.**
> Un **número real** es cualquier número que se puede escribir con una **expresión decimal**, finita
> o infinita, con signo. Cada número real corresponde a **un punto** de la recta numérica, y cada
> punto de la recta corresponde a un número real. El conjunto de los números reales se llama **ℝ**.
> Un número real es **irracional** si **no** es racional, es decir, si no se puede escribir como
> fracción de enteros. Al conjunto de los irracionales lo llamaremos **𝕀** (también se escribe ℝ ∖ ℚ,
> «ℝ menos ℚ»).

🔎 **Honestidad matemática.** La definición anterior es la adecuada para ESO, pero no es la definición rigurosa que se usa en la universidad. Definir ℝ con todo rigor (con las llamadas «cortaduras de Dedekind» o con «sucesiones de Cauchy») es un tema de primer curso de Análisis Matemático. Para la teoría de códigos **casi nunca necesitarás ℝ**: tu investigación vive en conjuntos finitos. Lo verás en la Ampliación B, al final del capítulo.

### 4.3. Expresiones decimales

> **[DEFINICIÓN 1.7] Tipos de expresión decimal.**
> - Un decimal es **exacto** (o finito) si tiene un número finito de cifras decimales: 0,175.
> - Un decimal es **periódico** si, a partir de cierta cifra, un bloque de cifras se repite
>   indefinidamente. Ese bloque se llama **periodo**.
>   - **Periódico puro:** el periodo empieza justo después de la coma: 0,(428571) = 0,428571428571…
>   - **Periódico mixto:** entre la coma y el periodo hay cifras que no se repiten, llamadas
>     **anteperiodo**: en 0,41(6) = 0,41666…, el anteperiodo es 41 y el periodo es 6.
> - Un decimal es **infinito no periódico** si tiene infinitas cifras y ningún bloque se repite
>   indefinidamente: 1,4142135623… (√2).
> - La **parte entera** es lo que hay antes de la coma: en 2,1(6) la parte entera es 2.
> - La **fracción generatriz** de un decimal exacto o periódico es la fracción irreducible que
>   tiene ese decimal.

⚠️ «Que se repitan cifras a simple vista» **no** basta para ser periódico. 0,1212 es **exacto** (tiene 4 cifras y se acaba); 0,(12) = 0,121212… es periódico. Y en 0,1010010001… se repiten muchos 0 y 1, pero **no hay un bloque fijo** que se repita: no es periódico.

### 4.4. El orden

> **[DEFINICIÓN 1.8] Orden.** Para dos números reales a y b, escribimos **a < b** («a es menor que b»)
> si la diferencia **b − a es positiva**. En la recta numérica, a < b significa que a está **a la
> izquierda** de b. Escribimos a ≤ b si a < b o a = b.

Consecuencias que usarás constantemente:

- Todo número negativo es menor que 0, y 0 es menor que todo número positivo.
- Entre negativos, **el que está más lejos del cero es el menor**: −7 < −3, porque −3 − (−7) = 4 es positivo.
- Para comparar dos fracciones con **denominadores positivos**: a/b < c/d exactamente cuando **a · d < c · b**. Por ejemplo, 3/7 < 4/9 porque 3 · 9 = 27 < 28 = 4 · 7.
- Para comparar decimales, se comparan las partes enteras y después cifra a cifra: 0,6 < 0,666… < 0,67.

### 4.5. Operaciones cerradas y contraejemplos

> **[DEFINICIÓN 1.9] Operación cerrada.** Un conjunto A es **cerrado** para una operación (por
> ejemplo, la suma) si, **siempre** que a y b son elementos de A, el resultado de operarlos también
> es elemento de A. En símbolos, para la suma: **para todo a ∈ A y todo b ∈ A, se cumple a + b ∈ A.**

> **[DEFINICIÓN 1.10] Contraejemplo.** Un **contraejemplo** de una afirmación del tipo «para todo…
> se cumple…» es **un caso concreto** en el que la afirmación **falla**.

La regla de oro (la estudiarás a fondo en el Módulo 10):

| Para demostrar que una afirmación «para todo…» es… | Hace falta… |
|---|---|
| **FALSA** | **Un solo** contraejemplo. |
| **VERDADERA** | Un **razonamiento general** (una demostración). Ningún número de ejemplos basta, porque los casos son infinitos. |

Por ejemplo, «ℕ es cerrado para la resta» es **falso**: basta el contraejemplo 2 − 5 = −3 ∉ ℕ. En cambio, para afirmar que «ℚ es cerrado para la suma» no bastan mil ejemplos: hay que dar un argumento que funcione para **todas** las fracciones (lo verás en la Propiedad 1.2).

### 4.6. Propiedades y teoremas

> **[PROPIEDAD 1.1 — demostrada] Inclusiones.** **ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ.**

*Demostración.*
- ℕ ⊂ ℤ: por la Definición 1.4, ℤ contiene a todos los naturales.
- ℤ ⊂ ℚ: todo entero n se puede escribir como n/1, que es una fracción de enteros con denominador 1 ≠ 0.
- ℚ ⊂ ℝ: todo racional a/b tiene una expresión decimal (se obtiene dividiendo a entre b; la Propiedad 1.4 dice qué forma tiene), así que es real. ∎

(El símbolo ∎ marca el final de una demostración.)

> **[PROPIEDAD 1.2 — demostrada] Tabla de cierre.**
>
> | Conjunto | Suma | Resta | Multiplicación | División (divisor ≠ 0) |
> |---|---|---|---|---|
> | ℕ | Sí | **No** (2 − 5 = −3) | Sí | **No** (1 : 2 = 1/2) |
> | ℤ | Sí | Sí | Sí | **No** (1 : 2 = 1/2) |
> | ℚ | Sí | Sí | Sí | Sí |
> | ℝ | Sí | Sí | Sí | Sí |

*Demostración para ℚ* (para ℕ y ℤ, los «Sí» los aceptamos por la experiencia de Primaria, y los «No» quedan demostrados por los contraejemplos de la tabla). Sean a/b y c/d dos racionales, con a, b, c, d enteros y b ≠ 0, d ≠ 0.

- **Suma:** a/b + c/d = (a·d + c·b)/(b·d). El numerador a·d + c·b es entero (sumas y productos de enteros son enteros) y el denominador b·d es entero y **distinto de 0** (el producto de dos números distintos de cero no es cero). Luego el resultado es racional.
- **Resta:** a/b − c/d = (a·d − c·b)/(b·d), con el mismo razonamiento.
- **Multiplicación:** (a/b)·(c/d) = (a·c)/(b·d), con b·d ≠ 0.
- **División:** si además c/d ≠ 0 (es decir, c ≠ 0), (a/b) : (c/d) = (a·d)/(b·c), y b·c ≠ 0. ∎

Fíjate en que la demostración **no usa ningún ejemplo concreto**: funciona para cualesquiera a, b, c, d. Eso es lo que la convierte en demostración.

> **[PROPIEDAD 1.3 — demostrada] Densidad de ℚ.** Entre dos racionales distintos siempre hay otro
> racional. En concreto, si a < b son racionales, su **punto medio** (a + b)/2 es racional y cumple
> a < (a + b)/2 < b.

*Demostración.* (a + b)/2 es racional porque es una suma de racionales dividida entre 2 (Propiedad 1.2). Además:
(a + b)/2 − a = (b − a)/2, que es positivo porque b − a > 0. Luego a < (a + b)/2.
b − (a + b)/2 = (b − a)/2 > 0. Luego (a + b)/2 < b. ∎

**Consecuencia:** entre dos racionales distintos hay **infinitos** racionales (aplica el punto medio una y otra vez). Compáralo con ℤ: entre 3 y 4 **no hay ningún** entero.

> **[PROPIEDAD 1.4 — demostrada] Toda fracción da un decimal exacto o periódico.** Al dividir a entre
> b (enteros, b > 0) se obtiene siempre un decimal exacto o un decimal periódico. Además, **el periodo
> tiene como mucho b − 1 cifras.**

*Demostración (argumento de los restos).* Haz la división larga de a entre b. Después de calcular la parte entera, en cada paso «bajas un 0»: multiplicas el resto actual r por 10, lo divides entre b, escribes la cifra del cociente y obtienes un resto nuevo. Observa dos cosas:

1. **Cada resto es uno de los números 0, 1, 2, …, b − 1** (un resto siempre es menor que el divisor).
2. **La siguiente cifra y el siguiente resto dependen solo del resto actual** (se calculan con 10·r entre b).

Si en algún momento el resto es 0, la división termina: **decimal exacto**. Si nunca es 0, todos los restos están entre 1 y b − 1: solo hay **b − 1 valores posibles**. Si miras los b primeros restos, tienes b restos y solo b − 1 valores posibles, así que **dos de ellos tienen que coincidir** (es como meter b calcetines en b − 1 cajones: algún cajón tiene dos; esta idea se llama *principio del palomar* y la estudiarás en el capítulo 11.6). Cuando un resto se repite, por el punto 2, **todo lo que viene después se repite**: las cifras forman un periodo. Como la repetición ocurre dentro de los b primeros restos, el periodo tiene como mucho b − 1 cifras. ∎

> **[PROPIEDAD 1.5] Criterio del denominador.** Sea a/b una fracción **irreducible** con b > 1.
> - (i) Si los únicos factores primos de b son 2 y/o 5, el decimal es **exacto**. **[demostrada]**
> - (ii) Si b no tiene ni el factor 2 ni el factor 5, el decimal es **periódico puro**.
> - (iii) Si b tiene el factor 2 o el 5 y además algún otro primo, el decimal es **periódico mixto**.
> - Además, en (ii) y (iii) el decimal **nunca** es exacto.
>
> **[demostración pendiente de (ii), (iii) y la última frase: capítulos 2.3 y 14.6]**

*Demostración de (i).* Si b = 2^i · 5^j (es decir, b es un producto de i doses y j cincos), llama m al mayor de los números i y j. Multiplicando numerador y denominador por los doses o cincos que falten, el denominador se convierte en 2^m · 5^m = 10^m, es decir, un 1 seguido de m ceros. Y una fracción con denominador 10^m es un decimal exacto con m cifras decimales. Por ejemplo, 7/40: 40 = 2³ · 5, m = 3, faltan dos cincos: 7/40 = (7·25)/(40·25) = 175/1000 = 0,175. ∎

**[VERIFICADO POR PROGRAMA]** El criterio completo (i)–(iii) coincide con la división larga en **las 124 750 fracciones a/b con 1 ≤ a < b ≤ 500**. Esto es **evidencia**, no demostración: hay infinitas fracciones. La demostración llegará cuando tengas la factorización en primos (Módulo 2).

⚠️ El criterio exige que la fracción sea **irreducible**. 21/56 parece tener un 7 en el denominador (56 = 2³ · 7), pero 21/56 = 3/8, y 3/8 = 0,375 es exacto.

> **[PROPIEDAD 1.6 — demostrada] Todo decimal exacto o periódico es racional.**

*Demostración.*
- **Exacto:** si x tiene m cifras decimales, x = N/10^m, donde N es el número que resulta de quitar la coma. Por ejemplo, 0,175 = 175/1000.
- **Periódico:** supongamos que x tiene un anteperiodo de j cifras y un periodo de p cifras. Al multiplicar x por 10^j, la coma se desplaza justo hasta el comienzo del periodo; al multiplicarlo por 10^(j+p), la coma se desplaza justo hasta el comienzo del **siguiente** periodo. Por tanto 10^(j+p)·x y 10^j·x tienen **exactamente las mismas cifras decimales**, y al restarlos las cifras decimales se cancelan: (10^(j+p) − 10^j)·x = N, donde N es un entero. Despejando, x = N / (10^(j+p) − 10^j), que es una fracción de enteros. ∎

**Conclusión de las Propiedades 1.4 y 1.6:**

> Un número es **racional** ⟺ su expresión decimal es **exacta o periódica**.
> Un número es **irracional** ⟺ su expresión decimal es **infinita y no periódica**.

(El símbolo ⟺ se lee «si y solo si» y significa que cada lado implica el otro.)

> **[OBSERVACIÓN 1.1 — demostrada] 0,(9) = 1.**

*Demostración.* Sea x = 0,999… Entonces 10x = 9,999… Restando, 10x − x = 9,999… − 0,999… = 9, es decir, 9x = 9, luego x = 1. ∎
**Segunda comprobación:** 1/3 = 0,333…; multiplicando por 3, 3 · (1/3) = 1 y 3 · 0,333… = 0,999… Luego 0,999… = 1.
No es que 0,(9) esté «muy cerca» de 1: **es** 1. Simplemente, el número 1 tiene dos expresiones decimales. (La división larga nunca produce el periodo 9; lo verás en el ejercicio B3.)

> **[TEOREMA 1.1] √2 es irracional.** No existe ninguna fracción a/b tal que (a/b)² = 2.
> *Demostración completa en la Ampliación A, al final del capítulo (es opcional en esta primera
> lectura; el método, «reducción al absurdo», se estudia en el capítulo 10.7).*

> **[PROPIEDAD 1.7 — demostración pendiente: capítulo 10.7]** Si n es un número natural que **no** es
> un cuadrado perfecto (no es 0, 1, 4, 9, 16, 25, …), entonces √n es irracional.
> Si n **sí** es cuadrado perfecto, √n es natural: √49 = 7.

> **[HECHO ACEPTADO 1.1] π es irracional.** Lo demostró Johann Heinrich Lambert en el siglo XVIII.
> La demostración usa herramientas universitarias y no la veremos. Por eso **π no es 3,14 ni 22/7**:
> esos números son racionales y solo son aproximaciones de π.

---

<a id="s5"></a>
## 5. Esquema visual y mapa conceptual

### 5.1. Los conjuntos, unos dentro de otros

```
┌──────────────────────────────── ℝ  (reales) ─────────────────────────────────┐
│                                                                              │
│  ┌────────────────────── ℚ  (racionales) ─────────────────┐  IRRACIONALES    │
│  │                                                        │                  │
│  │  ┌─────────────── ℤ  (enteros) ───────────┐            │   √2     √5      │
│  │  │                                        │   1/2      │   π      −√3     │
│  │  │  ┌────── ℕ  (naturales) ──────┐        │   −3/4     │   0,1010010001…  │
│  │  │  │   0   1   2   3   17  ...  │  −1    │   0,75     │                  │
│  │  │  └────────────────────────────┘  −25   │   0,(3)    │                  │
│  │  │                                        │            │                  │
│  │  └────────────────────────────────────────┘            │                  │
│  └────────────────────────────────────────────────────────┘                  │
└──────────────────────────────────────────────────────────────────────────────┘
```

**Cómo leerlo:** si un número está en una caja, está también en todas las cajas que la rodean. Los irracionales están dentro de ℝ pero **fuera** de ℚ: un número no puede ser a la vez racional e irracional.

### 5.2. Árbol de decisión: ¿qué tipo de número es?

```
            ¿Se puede escribir como fracción a/b con a, b enteros y b ≠ 0?
                    │                                    │
                   SÍ                                   NO
                    │                                    │
                    ▼                                    ▼
      Simplifica hasta la fracción              IRRACIONAL (está en ℝ, no en ℚ)
      irreducible con denominador > 0           Su decimal es infinito no periódico.
                    │
         ¿El denominador es 1?
           │                 │
          SÍ                NO ──────►  RACIONAL NO ENTERO (está en ℚ, no en ℤ)
           │
     Es un entero n. ¿n ≥ 0?
           │          │
          SÍ         NO ─────►  ENTERO NEGATIVO (está en ℤ, no en ℕ)
           │
           ▼
      NATURAL (está en ℕ, y por tanto en ℤ, ℚ y ℝ)
```

### 5.3. Árbol de decisión: ¿qué decimal dará la fracción a/b?

```
     Simplifica a/b hasta que sea irreducible (¡siempre lo primero!)
                               │
             Descompón el denominador b en factores primos
                               │
      ┌────────────────────────┼─────────────────────────┐
      ▼                        ▼                         ▼
 Solo hay 2 y/o 5        No hay ni 2 ni 5        Hay 2 o 5 y además otro primo
      │                        │                         │
 DECIMAL EXACTO        PERIÓDICO PURO              PERIÓDICO MIXTO
 ej.: 7/40 = 0,175     ej.: 3/7 = 0,(428571)       ej.: 5/12 = 0,41(6)
```

### 5.4. La recta numérica

```
   −3      −2      −1       0       1       2
────┼───────┼───────┼───────┼───────┼───────┼────►
        ▲       ▲              ▲       ▲  ▲
        │       │              │       │  └──── 7/4 = 1,75
        │       │              │       └─────── √2 ≈ 1,414…
        │       │              └─────────────── 1/3 = 0,(3)
        │       └────────────────────────────── −3/2 = −1,5
        └────────────────────────────────────── −2,5
```

Cada número real es un punto de la recta. Los racionales están «por todas partes» (Propiedad 1.3), pero **no la llenan**: entre ellos quedan los irracionales, como √2.

### 5.5. Mapa conceptual del capítulo

```
                         NÚMEROS
                            │
      ┌─────────────────────┼──────────────────────┐
      ▼                     ▼                      ▼
  CONJUNTOS            REPRESENTACIÓN          OPERACIONES
  ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ        fracción ⟷ decimal      ¿cerrada o no?
      │                     │                      │
  cada uno nace        exacto / periódico     contraejemplo (1 basta
  para resolver        / no periódico         para refutar) frente a
  una operación             │                 demostración (hace falta
  que fallaba          racional ⟺ exacto       para afirmar «siempre»)
                       o periódico                 │
                            │                      ▼
                            ▼              [AVANCE] conjunto FINITO
                     el ordenador usa       cerrado para + − × ÷
                     aproximaciones         ──► GF(7), tu investigación
                     (float) ──► en GF(7)
                     solo enteros exactos
```

---

<a id="s6"></a>
## 6. Fórmulas importantes, símbolo a símbolo

**F1. Definición de ℚ:** ℚ = { a/b : a, b ∈ ℤ, b ≠ 0 }
- { … : … } — «el conjunto de los … tales que …».
- a, b ∈ ℤ — a y b son números enteros.
- b ≠ 0 — el denominador no puede ser cero.

**F2. Igualdad de fracciones:** a/b = c/d ⟺ a · d = b · c  (con b ≠ 0, d ≠ 0)
- Sirve para comprobar si dos fracciones son el mismo número sin simplificarlas.

**F3. Suma y resta:** a/b ± c/d = (a·d ± c·b)/(b·d)
- ± significa «más o menos»: la fórmula vale para la suma (+) y para la resta (−).
- En la práctica conviene usar el mínimo común múltiplo de los denominadores (capítulo 1.3), pero esta fórmula **siempre** funciona.

**F4. Producto:** (a/b) · (c/d) = (a·c)/(b·d)

**F5. Cociente:** (a/b) : (c/d) = (a·d)/(b·c), con c ≠ 0

**F6. Comparación:** si b > 0 y d > 0: a/b < c/d ⟺ a·d < c·b
- La condición b > 0, d > 0 es esencial: con denominadores negativos el sentido de la desigualdad puede cambiar. Por eso, antes de comparar, se escriben las fracciones con denominador positivo.

**F7. Punto medio:** m = (a + b)/2
- m está exactamente a mitad de camino entre a y b. Si a y b son racionales, m también.

**F8. Fracción generatriz de un decimal exacto:** x = N / 10^m
- N: el número que queda al quitar la coma.
- m: el número de cifras decimales.
- 10^m: un 1 seguido de m ceros (10^3 = 1000).
- Ejemplo: 0,175 = 175/1000 = 7/40.

**F9. Fracción generatriz de un decimal periódico** (regla clásica, que se deduce de la Propiedad 1.6):

```
             (número sin coma hasta el final del primer periodo) − (número sin coma hasta el final del anteperiodo)
      x  =  ────────────────────────────────────────────────────────────────────────────────────────────────────────
                 tantos 9 como cifras tiene el PERIODO, seguidos de tantos 0 como cifras tiene el ANTEPERIODO
```

- Ejemplo periódico mixto: 1,2(3) → numerador 123 − 12 = 111; denominador 90 (un 9 por la cifra del periodo, un 0 por la del anteperiodo) → 111/90 = 37/30.
- Ejemplo periódico puro (sin anteperiodo): 2,(18) → (218 − 2)/99 = 216/99 = 24/11.
- **No la memorices sin entenderla:** en el Ejemplo 1.2 verás de dónde sale. Si la olvidas, siempre puedes usar el **método de restar** (multiplicar por potencias de 10 y restar), que es la demostración de la regla.

**F10. Cota del periodo:** longitud del periodo de a/b ≤ b − 1
- Es una **cota** (un máximo posible), no el valor exacto. 1/13 tiene periodo 6, y 6 ≤ 12.

---

<a id="s7"></a>
## 7. Ejemplo básico resuelto paso a paso

> **[EJEMPLO 1.1] Clasifica los siguientes números en ℕ, ℤ, ℚ, 𝕀 y ℝ:**
> 7;  −3;  0;  2/5;  −12/4;  0,75;  0,(6);  √9;  √5;  π;  −√16;  1,0100100010000… (cada vez hay un 0 más entre dos unos).

**Estrategia.** Para cada número: (1) **simplifícalo** todo lo posible; (2) recorre el árbol de decisión de §5.2.

1. **7.** Es un número de contar. Está en ℕ y, por la Propiedad 1.1, también en ℤ, ℚ y ℝ.
2. **−3.** Es negativo, así que no está en ℕ. Es el opuesto de un natural: está en ℤ (y en ℚ y ℝ).
3. **0.** Con nuestro convenio, 0 ∈ ℕ.
4. **2/5.** Es una fracción de enteros, así que está en ℚ. ¿Es un entero disfrazado? 5 no divide a 2, y 2/5 = 0,4 no es entero. Está en ℚ y ℝ, **no** en ℤ.
5. **−12/4.** ¡Primero simplificamos! −12/4 = −3, porque 4 · (−3) = −12. Es un **entero** negativo: está en ℤ, ℚ y ℝ. Error típico: verlo escrito como fracción y decir que «no es entero».
6. **0,75.** Decimal exacto: 0,75 = 75/100 = 3/4 (dividiendo entre 25). Está en ℚ, no en ℤ.
7. **0,(6).** Tiene infinitas cifras, pero es **periódico**, así que es racional (Propiedad 1.6). Su fracción: x = 0,666…; 10x = 6,666…; restando, 9x = 6; x = 6/9 = 2/3. Está en ℚ.
8. **√9.** √9 = 3, porque 3 · 3 = 9 y 3 ≥ 0. Es natural.
9. **√5.** 2² = 4 < 5 < 9 = 3², así que 5 no es un cuadrado perfecto. Por la Propiedad 1.7, √5 es **irracional** (√5 = 2,2360679…).
10. **π.** Irracional (Hecho aceptado 1.1).
11. **−√16.** √16 = 4, luego −√16 = −4: entero negativo.
12. **1,0100100010000…** Sus cifras siguen un patrón (bloques de ceros cada vez más largos), pero **ningún bloque fijo** se repite. Razonemos: si fuera periódico con un periodo de p cifras, como aparecen bloques de ceros tan largos como queramos, dentro de la parte periódica acabaría habiendo más de p ceros seguidos; entonces el periodo entero estaría formado solo por ceros y, a partir de ahí, no volvería a aparecer ningún 1. Pero siempre vuelve a aparecer un 1. Luego no es periódico: es infinito no periódico y, por tanto, **irracional**.

**Resultado:**

| Número | Simplificado | ℕ | ℤ | ℚ | 𝕀 | ℝ |
|---|---|:-:|:-:|:-:|:-:|:-:|
| 7 | 7 | ✓ | ✓ | ✓ | | ✓ |
| −3 | −3 | | ✓ | ✓ | | ✓ |
| 0 | 0 | ✓ | ✓ | ✓ | | ✓ |
| 2/5 | 0,4 | | | ✓ | | ✓ |
| −12/4 | −3 | | ✓ | ✓ | | ✓ |
| 0,75 | 3/4 | | | ✓ | | ✓ |
| 0,(6) | 2/3 | | | ✓ | | ✓ |
| √9 | 3 | ✓ | ✓ | ✓ | | ✓ |
| √5 | 2,2360679… | | | | ✓ | ✓ |
| π | 3,1415926… | | | | ✓ | ✓ |
| −√16 | −4 | | ✓ | ✓ | | ✓ |
| 1,0100100010… | — | | | | ✓ | ✓ |

**Comprobación por un segundo procedimiento (regla de la escalera).** Por la Propiedad 1.1, en cada fila las marcas de ℕ, ℤ, ℚ deben formar una «escalera»: si hay ✓ en ℕ, tiene que haberlo en ℤ y ℚ; si hay ✓ en ℤ, tiene que haberlo en ℚ. Además, **ℚ e 𝕀 nunca pueden estar marcados a la vez**, y **ℝ siempre** está marcado. Revisa la tabla fila a fila: se cumple en todas. Si en tu tabla alguna fila rompe la escalera, hay un error seguro.

---

<a id="s8"></a>
## 8. Ejemplo intermedio resuelto paso a paso

> **[EJEMPLO 1.2]** (a) Predice, **sin dividir**, qué tipo de decimal dan 7/40, 5/12 y 3/7.
> (b) Haz las divisiones y comprueba tu predicción. (c) Partiendo **solo de los decimales**,
> recupera las fracciones. (d) Comprueba que coinciden con las originales.

### (a) Predicción

**Paso 1: ¿son irreducibles?** 7 y 40 no tienen divisores comunes (7 es primo y no divide a 40). 5 y 12 tampoco (5 es primo y no divide a 12). 3 y 7 son primos distintos. Las tres son irreducibles.

**Paso 2: factorizar los denominadores y aplicar la Propiedad 1.5.**

| Fracción | Denominador | Factores | Predicción |
|---|---|---|---|
| 7/40 | 40 | 2 · 2 · 2 · 5 = 2³ · 5 | Solo 2 y 5 → **exacto** |
| 5/12 | 12 | 2 · 2 · 3 = 2² · 3 | Tiene 2 y además 3 → **periódico mixto** |
| 3/7 | 7 | 7 | Ni 2 ni 5 → **periódico puro** |

### (b) Divisiones (con todos los restos a la vista)

En cada fila: multiplicamos el resto anterior por 10 («bajamos un cero»), dividimos entre el denominador, anotamos la cifra y el nuevo resto. **Vigilar los restos** es la clave: cuando uno se repite, empieza la repetición.

**7 : 40.** Como 7 < 40, la parte entera es 0 y el primer resto es 7.

| Paso | Resto × 10 | : 40 | Cifra | Nuevo resto |
|---|---|---|---|---|
| 1 | 70 | 70 = 1 · 40 + 30 | 1 | 30 |
| 2 | 300 | 300 = 7 · 40 + 20 | 7 | 20 |
| 3 | 200 | 200 = 5 · 40 + 0 | 5 | **0** → termina |

7/40 = **0,175**. Decimal exacto ✓.

**5 : 12.** Parte entera 0, primer resto 5.

| Paso | Resto × 10 | : 12 | Cifra | Nuevo resto |
|---|---|---|---|---|
| 1 | 50 | 50 = 4 · 12 + 2 | 4 | 2 |
| 2 | 20 | 20 = 1 · 12 + 8 | 1 | 8 |
| 3 | 80 | 80 = 6 · 12 + 8 | 6 | **8** ← ya había salido |

El resto 8 se repite, así que la cifra 6 se repetirá para siempre: 5/12 = 0,41666… = **0,41(6)**. Periódico mixto: anteperiodo 41, periodo 6 ✓.

**3 : 7.** Parte entera 0, primer resto 3.

| Paso | Resto × 10 | : 7 | Cifra | Nuevo resto |
|---|---|---|---|---|
| 1 | 30 | 30 = 4 · 7 + 2 | 4 | 2 |
| 2 | 20 | 20 = 2 · 7 + 6 | 2 | 6 |
| 3 | 60 | 60 = 8 · 7 + 4 | 8 | 4 |
| 4 | 40 | 40 = 5 · 7 + 5 | 5 | 5 |
| 5 | 50 | 50 = 7 · 7 + 1 | 7 | 1 |
| 6 | 10 | 10 = 1 · 7 + 3 | 1 | **3** ← ¡es el resto inicial! |

Volvemos al resto 3, que era el de partida, así que todo se repite desde la primera cifra: 3/7 = **0,(428571)**. Periódico puro ✓. Su periodo tiene 6 cifras, el máximo permitido por la Propiedad 1.4 (b − 1 = 6).

👀 **Fíjate en los restos de esta última división: 3, 2, 6, 4, 5, 1.** Han aparecido **todos** los restos no nulos posibles al dividir entre 7. No es casualidad; volveremos a ello en el Ejemplo 1.3 y en el Módulo 14.

### (c) Del decimal a la fracción (método de restar)

**0,175** (exacto, 3 cifras decimales): 0,175 = 175/1000. Simplificamos: 175 = 5 · 5 · 7 y 1000 = 2 · 2 · 2 · 5 · 5 · 5. Dividimos entre 25: **175/1000 = 7/40**.

**0,41(6)** (periódico mixto). Llamamos x al número:

```
        x =   0,41666…
     100x =  41,666…      (multiplicamos por 100: la coma salta el anteperiodo "41")
    1000x = 416,666…      (multiplicamos por 1000: la coma salta además un periodo "6")
```

Las dos últimas líneas tienen **las mismas cifras decimales** (666…), así que al restarlas desaparecen:

```
    1000x − 100x = 416,666… − 41,666…
            900x = 375
               x = 375/900
```

Simplificamos: 375 = 3 · 5³ y 900 = 2² · 3² · 5². El máximo común divisor es 3 · 5² = 75. 375 : 75 = 5 y 900 : 75 = 12. Luego **x = 5/12**.

**¿Por qué multiplicamos por 100 y por 1000?** Porque queremos dos múltiplos de x cuyas partes decimales sean **idénticas**, para que al restar se cancelen. Eso ocurre cuando, en ambos, la coma queda justo antes del inicio de un periodo.

**Comprobación con la regla F9:** numerador = 416 − 41 = 375; denominador: un 9 (periodo de 1 cifra) y dos 0 (anteperiodo de 2 cifras) = 900. Sale 375/900 = 5/12 ✓. Ahora ves de dónde sale la regla: es exactamente la resta 1000x − 100x.

**0,(428571)** (periódico puro, 6 cifras de periodo):

```
          x =      0,428571428571…
    1000000x = 428571,428571…
    1000000x − x = 428571
         999999x = 428571
               x = 428571/999999
```

Para simplificar: 999999 = 3 · 3 · 3 · 7 · 11 · 13 · 37 y 428571 = 3 · 3 · 3 · 3 · 11 · 13 · 37, que comparten 3³ · 11 · 13 · 37 = 142857. Dividiendo: 428571 : 142857 = 3 y 999999 : 142857 = 7. Luego **x = 3/7**.

### (d) Comprobación

Hemos recuperado exactamente 7/40, 5/12 y 3/7 ✓. Además, una comprobación independiente rápida para el decimal exacto: 0,175 · 40 = 7 ✓ (multiplicar por el denominador debe devolver el numerador).

💡 **Para un decimal periódico largo**, factorizar 999999 a mano es pesado. Una forma más rápida de comprobar es **al revés**: dividir 3 entre 7 (como en (b)) y ver que sale 0,(428571). Las dos direcciones (fracción → decimal y decimal → fracción) se comprueban mutuamente.

---

<a id="s9"></a>
## 9. Ejemplo avanzado aplicado a tu investigación

> **[EJEMPLO 1.3] ¿En qué «mundo de números» viven los códigos sobre GF(7)?**
> (a) ¿Por qué un programa de investigación **no** debe usar decimales del ordenador?
> (b) ¿Es el conjunto {0, 1, 2, 3, 4, 5, 6} cerrado para la suma y el producto habituales?
> (c) ¿Qué pasa si operamos «con reloj de 7»? ¿Y «con reloj de 6»?
> (d) ¿Qué conclusión sacamos para tu proyecto?

### (a) El ordenador y los decimales

Ya sabes que 1/3 = 0,333… no se puede escribir en decimal con un número finito de cifras. Los ordenadores tienen el mismo problema, pero con **otros números**: internamente no trabajan en base 10 (con las cifras 0–9) sino en **base 2** (solo con las cifras 0 y 1; lo estudiarás en el capítulo 8.7). En base 2, el número 1/10 tiene una expresión **periódica**, igual que 1/3 la tiene en base 10. Como el ordenador solo guarda un número limitado de cifras, **recorta** el periodo y guarda una aproximación de 0,1 (Ampliación C).

Este pequeño programa lo muestra. Todavía no sabes Python; basta con que leas los comentarios (lo que va detrás de `#`).

**Para qué sirve:** comprobar con tus propios ojos que los decimales del ordenador (llamados `float`) no son exactos, que las fracciones exactas sí lo son, y probar las operaciones «con reloj de 7» del apartado (c).

```python
# Archivo: codigo/ejemplos/cap_1_1_rincon_del_ordenador.py

print(0.1 + 0.2)              # suma con decimales "de ordenador" (float)
print(0.1 + 0.2 == 0.3)       # ¿es exactamente igual a 0.3?

from fractions import Fraction
print(Fraction(1, 10) + Fraction(2, 10))               # suma EXACTA de fracciones
print(Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10))

print((4 + 5) % 7)            # suma "con reloj de 7": resto de dividir 9 entre 7
print((3 * 5) % 7)            # producto "con reloj de 7": resto de dividir 15 entre 7
```

**Entrada:** ninguna (el programa no pide datos).
**Salida obtenida** al ejecutarlo realmente (Python 3.13.16, 12/10/2026):

```
0.30000000000000004
False
3/10
True
2
1
```

**Por qué esa salida es correcta:**

- Línea 1: el ordenador guarda aproximaciones de 0,1 y de 0,2; al sumarlas, los pequeños errores se notan en la cifra 17.ª: sale 0,30000000000000004 en lugar de 0,3.
- Línea 2: por eso la comparación «¿es igual a 0,3?» da `False` (falso). **Una investigación que compara decimales del ordenador con `==` puede sacar conclusiones falsas.**
- Líneas 3–4: `Fraction` guarda numerador y denominador como **enteros**, y con enteros Python es exacto: 1/10 + 2/10 = 3/10, y la comparación da `True` (verdadero).
- Líneas 5–6: `%` calcula el **resto** de una división. 9 = 1 · 7 + 2 → resto 2. 15 = 2 · 7 + 1 → resto 1. Esto es lo que usaremos en el apartado (c).

**Pruebas:** el programa [`verificar_cap_1_1.py`](../../../codigo/verificaciones/verificar_cap_1_1.py) comprueba automáticamente estas mismas salidas (y todos los cálculos del capítulo).

**Limitaciones:** las salidas de las líneas 1–2 dependen de cómo representa el ordenador los `float` (norma internacional IEEE 754, usada por prácticamente todos los ordenadores actuales). Las líneas 3–6 usan solo enteros y son exactas en cualquier ordenador.

**Regla para todo el libro:** en tu investigación sobre GF(7) **solo se usarán números enteros** (0, 1, 2, 3, 4, 5, 6 y los resultados de operar con ellos), nunca decimales del ordenador. Y **nunca** se dividirá con `/` en Python: en GF(7) dividir significa otra cosa, como verás ahora.

### (b) ¿Es {0, 1, 2, 3, 4, 5, 6} cerrado con las operaciones de siempre?

Llamemos S = {0, 1, 2, 3, 4, 5, 6}. Para la **suma habitual**, un solo contraejemplo basta para ver que **no** es cerrado: 4 + 5 = 9 y 9 ∉ S. Para el **producto habitual**, tampoco: 3 · 5 = 15 ∉ S. Con las operaciones de siempre, S no sirve: los resultados «se escapan».

### (c) Operar «con reloj de 7» y «con reloj de 6»

Recuerda los días de la semana: después del domingo vuelve el lunes. Definimos dos operaciones nuevas en S (los símbolos ⊕ y ⊗ son solo para distinguirlas de las de siempre):

- **a ⊕ b** = el **resto** de dividir a + b entre 7.
- **a ⊗ b** = el **resto** de dividir a · b entre 7.

Ejemplos: 4 ⊕ 5: 9 = 1 · 7 + **2**, luego 4 ⊕ 5 = 2. 6 ⊕ 6: 12 = 1 · 7 + **5**, luego 6 ⊕ 6 = 5. 3 ⊗ 5: 15 = 2 · 7 + **1**, luego 3 ⊗ 5 = 1.

**Ahora S sí es cerrado**: el resto de dividir entre 7 es **siempre** uno de los números 0, 1, …, 6. (Esto no es un ejemplo: es un razonamiento general, válido para cualesquiera a y b.)

La tabla completa de ⊗ («multiplicar con reloj de 7») es:

```
 ⊗ │ 0 1 2 3 4 5 6
───┼───────────────
 0 │ 0 0 0 0 0 0 0
 1 │ 0 1 2 3 4 5 6
 2 │ 0 2 4 6 1 3 5
 3 │ 0 3 6 2 5 1 4
 4 │ 0 4 1 5 2 6 3
 5 │ 0 5 3 1 6 4 2
 6 │ 0 6 5 4 3 2 1
```

Mira las filas 1 a 6 (sin la columna del 0): **cada una contiene los números 1, 2, 3, 4, 5, 6 exactamente una vez**, solo que en distinto orden. En particular, **en cada fila aparece el 1**. Eso significa que para cada número a ≠ 0 hay una «pareja» b con a ⊗ b = 1:

| a | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| pareja b (a ⊗ b = 1) | 1 | 4 | 5 | 2 | 3 | 6 |

Por ejemplo, 2 ⊗ 4 = 8 → resto 1. ¿Para qué sirve esto? Para **dividir**. En ℚ, dividir entre 2 es lo mismo que multiplicar por 1/2, que es el número que multiplicado por 2 da 1. En el mundo «reloj de 7», el número que multiplicado por 2 da 1 es el **4**. Así que «dividir entre 2» se hace «multiplicando por 4». Comprobación: si «6 entre 2» debe ser 3, entonces 6 ⊗ 4 = 24 → resto 3 ✓, y en efecto 3 ⊗ 2 = 6 ✓.

**Comparemos con el reloj de 6.** Ahora S′ = {0, 1, 2, 3, 4, 5} y operamos con restos de dividir entre 6:

```
 ⊗ │ 0 1 2 3 4 5        (reloj de 6)
───┼─────────────
 0 │ 0 0 0 0 0 0
 1 │ 0 1 2 3 4 5
 2 │ 0 2 4 0 2 4   ← nunca aparece el 1
 3 │ 0 3 0 3 0 3   ← nunca aparece el 1
 4 │ 0 4 2 0 4 2   ← nunca aparece el 1
 5 │ 0 5 4 3 2 1
```

Aquí pasan dos cosas «raras»: 2 ⊗ 3 = 6 → resto **0**: ¡dos números distintos de cero cuyo producto es cero! Y en las filas de 2, 3 y 4 **no aparece el 1**, así que no se puede «dividir» entre 2, 3 ni 4.

### (d) Conclusión para tu proyecto

- **[VERIFICADO POR PROGRAMA]** Con el reloj de 7, el conjunto {0, …, 6} es cerrado para ⊕ y ⊗, y todo número distinto de 0 tiene pareja (por tanto, se puede dividir entre él). Con el reloj de 6, no. (Lo hemos comprobado a mano en las tablas, y `verificar_cap_1_1.py` lo comprueba también.)
- **[AVANCE — demostración pendiente: Módulos 13–14]** Lo que distingue al 7 del 6 es que **7 es primo** y 6 no. En general: con el reloj de n, todo número no nulo tiene pareja **exactamente cuando n es primo**. Investigarás esta afirmación tú mismo en el ejercicio C2.
- El mundo «reloj de 7» es, precisamente, **GF(7)**: un conjunto **finito** con el que se puede sumar, restar, multiplicar y dividir (entre números no nulos) igual que en ℚ. Los códigos de tu investigación son listas de símbolos de GF(7), y para calcular sus parámetros habrá que resolver sistemas de ecuaciones, para lo cual **hace falta poder dividir**. Por eso se usa GF(7) y no el «reloj de 6».
- Y recuerda los restos de la división 3 : 7 del Ejemplo 1.2: 3, 2, 6, 4, 5, 1. Cada resto se obtiene del anterior multiplicando por 10 y tomando el resto entre 7, es decir, «multiplicando por 3 con reloj de 7» (porque 10 = 1 · 7 + 3). Que aparezcan todos los restos no nulos está relacionado con una propiedad del número 3 en GF(7) que estudiarás en el capítulo 14.6 (*raíces primitivas*).

---

<a id="s10"></a>
## 10. Errores frecuentes

| # | Error | Por qué está mal | Cómo corregirlo y detectarlo |
|---|---|---|---|
| E1 | «−12/4 no es entero porque está escrito como fracción.» | La forma de escribir no decide el conjunto; decide el **valor**: −12/4 = −3. | **Simplifica siempre antes de clasificar.** |
| E2 | «Todo número con infinitas cifras decimales es irracional.» | 1/3 = 0,333… es racional. Lo que caracteriza a los irracionales es ser **infinitos y no periódicos**. | Pregúntate: ¿hay un bloque que se repite siempre? |
| E3 | «π = 3,14» o «π = 22/7». | Son racionales; π es irracional. Son **aproximaciones**. | Escribe π ≈ 3,14 (con ≈, «aproximadamente»). |
| E4 | «0,(9) es un poco menor que 1.» | 0,(9) = 1 exactamente (Observación 1.1). | Haz la resta 10x − x. |
| E5 | «√ de cualquier número es irracional.» | √9 = 3, √(1/4) = 1/2. | Comprueba primero si es un cuadrado perfecto. |
| E6 | Escribir «2 ⊂ ℕ». | ⊂ es entre conjuntos. Lo correcto es 2 ∈ ℕ (o {2} ⊂ ℕ). | ∈: elemento–conjunto; ⊂: conjunto–conjunto. |
| E7 | «−7 > −3 porque 7 > 3.» | Entre negativos, el más alejado del 0 es el menor: −7 < −3. | Dibuja la recta, o calcula la diferencia: −3 − (−7) = 4 > 0. |
| E8 | Fracción generatriz de 0,41(6) = 416/999. | Esa regla es solo para periódicos **puros**; aquí hay anteperiodo. | Comprueba dividiendo: 416/999 = 0,(416), no 0,41(6). |
| E9 | Decir que 21/56 da decimal periódico «porque 56 tiene un 7». | El criterio exige fracción **irreducible**: 21/56 = 3/8. | **Simplifica primero.** |
| E10 | «He probado 10 ejemplos y funciona, así que es verdad siempre.» | Los ejemplos no demuestran afirmaciones sobre infinitos casos. | Busca una demostración o, al menos, etiquétalo como **conjetura**. |
| E11 | Dividir entre cero, o creer que 0/5 no existe. | a/0 no está definido; 0/5 = 0. | Comprueba: «¿qué número multiplicado por el divisor da el dividendo?». |
| E12 | Escribir `0,75` en Python. | Python usa punto decimal; `0,75` significa otra cosa (dos números separados). | En programas: `0.75`. En el cuaderno: 0,75. |
| E13 | Comparar decimales del ordenador con `==`. | Los `float` son aproximaciones: `0.1 + 0.2 == 0.3` da `False`. | En GF(7), solo enteros. Si necesitas fracciones exactas: `Fraction`. |
| E14 | Confundir «periodo de como mucho b − 1 cifras» con «periodo de exactamente b − 1 cifras». | Es una **cota** (un máximo): 1/13 tiene periodo 6, no 12. | Distingue «≤» de «=». |

---

<a id="s11"></a>
## 11. Resumen para memorizar

1. **ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ**; los irracionales están en ℝ pero no en ℚ. En este libro, 0 ∈ ℕ.
2. Cada conjunto nace para que una operación deje de fallar: ℤ para restar, ℚ para dividir, ℝ para medir (√2).
3. **Racional ⟺ decimal exacto o periódico. Irracional ⟺ decimal infinito no periódico.**
4. Fracción **irreducible** a/b: denominador solo con 2 y 5 → exacto; sin 2 ni 5 → periódico puro; mezcla → periódico mixto.
5. El periodo de a/b tiene **como mucho b − 1** cifras, porque solo hay b − 1 restos no nulos.
6. Fracción generatriz: multiplica por potencias de 10 para que coincidan las partes decimales y **resta**.
7. 0,(9) = 1. √n es natural o irracional. π es irracional.
8. Entre dos racionales siempre hay otro (punto medio).
9. **Un contraejemplo basta para refutar; ningún número de ejemplos basta para demostrar.**
10. El ordenador aproxima los decimales: **en GF(7) solo se usan enteros**.
11. [AVANCE] Con el «reloj de 7» se puede sumar, restar, multiplicar y dividir sin salir de {0, …, 6}: eso es GF(7).

---

<a id="s12"></a>
## 12. Tabla de fórmulas y propiedades

| Código | Enunciado | Condiciones | Estado |
|---|---|---|---|
| F1 | ℚ = { a/b : a, b ∈ ℤ, b ≠ 0 } | — | Definición |
| F2 | a/b = c/d ⟺ a·d = b·c | b, d ≠ 0 | Propiedad (se demuestra en 1.3) |
| F3 | a/b ± c/d = (a·d ± c·b)/(b·d) | b, d ≠ 0 | Propiedad |
| F4 | (a/b)·(c/d) = (a·c)/(b·d) | b, d ≠ 0 | Propiedad |
| F5 | (a/b) : (c/d) = (a·d)/(b·c) | b, c, d ≠ 0 | Propiedad |
| F6 | a/b < c/d ⟺ a·d < c·b | b, d > 0 | Propiedad |
| F7 | a < (a + b)/2 < b | a < b | Prop. 1.3, demostrada |
| F8 | decimal exacto con m cifras = N/10^m | — | Prop. 1.6, demostrada |
| F9 | generatriz = (sin coma hasta fin del 1.er periodo − sin coma hasta fin del anteperiodo) / (9…9 0…0) | decimal periódico | Prop. 1.6, demostrada |
| F10 | longitud del periodo de a/b ≤ b − 1 | b > 0 | Prop. 1.4, demostrada |
| P1.1 | ℕ ⊂ ℤ ⊂ ℚ ⊂ ℝ | — | Demostrada |
| P1.2 | Cierre: ℕ (+, ×); ℤ (+, −, ×); ℚ y ℝ (+, −, ×, : entre no nulos) | — | Demostrada (ℚ) |
| P1.5 | Criterio del denominador | fracción irreducible | (i) demostrada; resto pendiente (2.3, 14.6) |
| T1.1 | √2 ∉ ℚ | — | Demostrado (Ampliación A) |
| P1.7 | √n ∈ ℕ o √n ∉ ℚ | n ∈ ℕ | Pendiente (10.7) |
| H1.1 | π ∉ ℚ | — | Hecho aceptado |
| O1.1 | 0,(9) = 1 | — | Demostrada |

---

<a id="s13"></a>
## 13. Ejercicios sin resolver

> **Instrucciones.** Hazlos en tu cuaderno, en orden. En cada uno, **escribe el razonamiento**, no
> solo el resultado. Cuando termines un bloque, compara con las soluciones (§14). Anota en tu
> registro (PROGRESO.md) los que falles y por qué.

### Nivel A — Comprender y aplicar directamente las definiciones

**A1.** Clasifica en una tabla como la del Ejemplo 1.1 (ℕ, ℤ, ℚ, 𝕀, ℝ):
a) −8  b) 15/3  c) −2/7  d) 0,125  e) 0,(12)  f) √25  g) √10  h) −√36/3  i) 3,141592  j) 0,123456789101112… (se escriben seguidos todos los naturales a partir del 1).

**A2.** Verdadero o falso. Justifica las verdaderas; da un contraejemplo de las falsas.
a) Todo número natural es entero.
b) Todo número entero es natural.
c) −5 ∈ ℕ.
d) ℤ ⊂ ℚ.
e) 0 ∈ ℚ.
f) Todo número con infinitas cifras decimales es irracional.
g) √2 ∈ ℚ.
h) Existe un número que es a la vez racional e irracional.

**A3.** Para cada fracción, **predice sin dividir** el tipo de decimal (exacto, periódico puro o mixto) y después **divide** para comprobarlo: 3/8;  7/9;  13/6;  9/25;  4/11.

**A4.** Halla la fracción generatriz irreducible y **comprueba dividiendo**:
a) 0,45  b) 0,(5)  c) 2,(18)  d) 0,3(12)  e) 1,0(6).

**A5.** Ordena de menor a mayor y sitúa aproximadamente en una recta numérica:
−2,5;  7/4;  −√4;  0,(3);  −3/2;  1,7.

**A6.** Decide si cada afirmación es verdadera o falsa. Si es falsa, da un contraejemplo; si es verdadera, explica por qué es verdad **en todos los casos**.
a) El producto de dos naturales es natural.
b) La resta de dos naturales es natural.
c) El cociente de dos enteros (con divisor no nulo) es entero.
d) La suma de dos racionales es racional.
e) La suma de dos irracionales es irracional.

### Nivel B — Combinar conceptos y resolver problemas nuevos

**B1.** Encuentra un número racional entre 3/7 y 4/9. Después, encuentra tres más. ¿Cuántos racionales hay entre 3/7 y 4/9? Justifica.

**B2.** **Sin dividir**, decide cuáles de estas fracciones dan un decimal exacto: 21/56;  33/120;  9/14;  6/15;  35/42. (Cuidado: hay trampas.)

**B3.** (a) Demuestra de **dos maneras distintas** que 0,(9) = 1. (b) Halla la fracción generatriz de 0,4(9) y de 2,(9). (c) ¿Qué observas? ¿Qué consecuencia tiene sobre las expresiones decimales de un número?

**B4.** (a) Sin dividir, justifica que el periodo de 1/13 tiene como mucho 12 cifras. (b) Calcula 1/13 anotando todos los restos y halla la longitud real de su periodo. (c) ¿Contradice el resultado de (b) lo que dijiste en (a)? Explica la diferencia entre una **cota** y un **valor exacto**.

**B5.** Un compañero escribe: «He programado un ordenador que ha comprobado que ninguna fracción a/b con denominador b entre 1 y 1000 cumple (a/b)² = 2. Por tanto, √2 es irracional.»
(a) ¿Es verdadera su conclusión? (b) ¿Es válido su razonamiento? (c) ¿Qué ha conseguido realmente con su programa?

**B6.** Para cada ecuación, di cuál es el **conjunto más pequeño** (ℕ, ℤ, ℚ o ℝ) en el que tiene alguna solución, y cuál es esa solución:
a) x + 9 = 4  b) 3x = 5  c) 5x = 35  d) x² = 9  e) x² = 7  f) 2x + 3 = 0.

### Nivel C — Investigación: formular hipótesis, comprobar y justificar

**C1. La longitud del periodo de 1/p.**
1. Para cada primo p ∈ {3, 7, 11, 13, 17, 19}, calcula 1/p por división larga **anotando los restos**, y halla la longitud de su periodo. (Si te atreves, añade p = 23.)
2. Haz una tabla con p, p − 1 y la longitud del periodo.
3. Busca una relación entre la longitud del periodo y p − 1. **Formúlala como conjetura**, por escrito.
4. ¿Qué tipo de evidencia tienes: ejemplos, evidencia computacional o demostración?
5. ¿Qué tendrías que hacer para intentar **refutar** tu conjetura?

**C2. Mundos de reloj.**
1. Construye la tabla de multiplicar «con reloj de n» (multiplicar y quedarse con el resto de dividir entre n) para n = 4, 5, 6 y 8. (La de n = 7 ya la tienes en el Ejemplo 1.3.)
2. Para cada n, responde: ¿todo número distinto de 0 tiene una «pareja» b tal que a ⊗ b = 1? Si no, ¿qué números no la tienen?
3. Formula una **conjetura**: ¿para qué valores de n todo número no nulo tiene pareja?
4. **Antes de calcular**, predice qué pasará con n = 9, 10 y 11. Después compruébalo.
5. Intenta explicar **por qué** falla cuando n no es primo. (Pista: si n = a · b con a y b entre 2 y n − 1, ¿cuánto vale a ⊗ b?)

### Problemas de aplicación práctica

**P1. Ascensores y temperaturas.**
a) Un ascensor sube de la planta −3 (garaje) a la planta 5. ¿Cuántas plantas ha subido? Después baja de la planta 4 a la −2: expresa ese cambio de planta con un número entero.
b) A las 6:00 un termómetro marca −4,5 °C y la temperatura sube 0,75 °C cada hora de forma constante. ¿A qué hora marcará 0 °C? ¿Qué temperatura marcará a las 14:00?
c) ¿Qué conjuntos de números has necesitado y por qué?

**P2. Céntimos y ordenadores.**
Una aplicación de una tienda suma precios.
a) Suma a mano 0,10 € diez veces.
b) Un programa que suma 0.1 diez veces, **una a una**, muestra `0.9999999999999999`. Explica por qué, usando lo aprendido en el Ejemplo 1.3.
c) Propón una forma de evitar el problema trabajando **solo con números enteros**, y úsala para sumar estos precios: 2,35 €; 0,99 €; 12,10 €; 0,56 €.
d) ¿Qué tiene que ver esto con tu investigación sobre GF(7)?

### Problema combinado

Como este es el primer capítulo, este problema combina lo aprendido aquí con lo que ya sabes de cursos anteriores (división con resto y fracciones). En los capítulos siguientes, el problema combinado mezclará capítulos del libro.

**PC. El calendario y los restos.** Hoy es lunes.
a) ¿Qué día de la semana será dentro de 23 días?
b) ¿Y dentro de 100 días?
c) ¿Qué día de la semana fue hace 10 días? Resuélvelo de dos formas distintas.
d) Explica por qué, para responder, solo importa el **resto** de dividir entre 7.
e) Expresa 100 días en semanas como número decimal. ¿Qué relación hay entre la parte decimal y el resto del apartado b)?

---

<a id="s14"></a>
## 14. Soluciones razonadas

> ⚠️ Intenta cada ejercicio **antes** de abrir su solución. Si te equivocas, no basta con leer la
> solución: identifica **qué concepto** fallaba (usa la columna «concepto» del §16) y haz un
> ejercicio parecido.

<details>
<summary>▶ Solución A1</summary>

| | Número | Simplificado / razonamiento | ℕ | ℤ | ℚ | 𝕀 | ℝ |
|---|---|---|:-:|:-:|:-:|:-:|:-:|
| a | −8 | entero negativo | | ✓ | ✓ | | ✓ |
| b | 15/3 | = 5, porque 3 · 5 = 15 | ✓ | ✓ | ✓ | | ✓ |
| c | −2/7 | 7 no divide a 2: no es entero | | | ✓ | | ✓ |
| d | 0,125 | = 125/1000 = 1/8 | | | ✓ | | ✓ |
| e | 0,(12) | = 12/99 = 4/33 (periódico) | | | ✓ | | ✓ |
| f | √25 | = 5, porque 5 · 5 = 25 | ✓ | ✓ | ✓ | | ✓ |
| g | √10 | 3² = 9 < 10 < 16 = 4²: no es cuadrado perfecto (Prop. 1.7) | | | | ✓ | ✓ |
| h | −√36/3 | = −6/3 = −2 | | ✓ | ✓ | | ✓ |
| i | 3,141592 | decimal **exacto** = 3141592/1000000 = 392699/125000 | | | ✓ | | ✓ |
| j | 0,123456789101112… | infinito no periódico (ver abajo) | | | | ✓ | ✓ |

**Trampa de i):** 3,141592 se parece a π, pero es un decimal exacto de 6 cifras, luego es racional. π tiene infinitas cifras.

**Justificación de j):** cuando escribimos 10, 100, 1000, 10000, … aparecen bloques de 1, 2, 3, 4, … ceros seguidos, tan largos como queramos. Si el decimal fuera periódico con un periodo de p cifras, al aparecer un bloque de más de p ceros dentro de la parte periódica, el periodo entero tendría que estar formado solo por ceros, y a partir de ahí todas las cifras serían 0. Pero siempre siguen apareciendo cifras distintas de 0 (cada número natural empieza por una cifra no nula). Contradicción: no es periódico. (Este número se llama *constante de Champernowne*.)

**Comprobación:** todas las filas cumplen la regla de la escalera del Ejemplo 1.1.

</details>

<details>
<summary>▶ Solución A2</summary>

a) **Verdadero.** Por definición, ℤ contiene a todos los naturales (Prop. 1.1).
b) **Falso.** Contraejemplo: −1 ∈ ℤ pero −1 ∉ ℕ.
c) **Falso.** −5 es negativo; los naturales son 0, 1, 2, …
d) **Verdadero.** Todo entero n se escribe n/1, con denominador 1 ≠ 0.
e) **Verdadero.** 0 = 0/1.
f) **Falso.** Contraejemplo: 1/3 = 0,333… tiene infinitas cifras y es racional.
g) **Falso.** Teorema 1.1: √2 es irracional.
h) **Falso.** Por la Definición 1.6, irracional significa «real que **no** es racional»: no se pueden cumplir las dos cosas a la vez.

</details>

<details>
<summary>▶ Solución A3</summary>

Todas son irreducibles (compruébalo: numerador y denominador no tienen divisores comunes).

| Fracción | Denominador | Predicción | División (restos) | Resultado |
|---|---|---|---|---|
| 3/8 | 2³ | exacto | 30 = 3·8+6; 60 = 7·8+4; 40 = 5·8+0 | 0,375 |
| 7/9 | 3² | periódico puro | 70 = 7·9+7 → resto 7 se repite | 0,(7) |
| 13/6 | 2·3 | periódico mixto | 13 = 2·6+1; 10 = 1·6+4; 40 = 6·6+4 → se repite | 2,1(6) |
| 9/25 | 5² | exacto | 90 = 3·25+15; 150 = 6·25+0 | 0,36 |
| 4/11 | 11 | periódico puro | 40 = 3·11+7; 70 = 6·11+4 → resto 4 inicial | 0,(36) |

**Segunda comprobación para los exactos:** 3/8 = (3·125)/(8·125) = 375/1000 = 0,375 ✓; 9/25 = (9·4)/(25·4) = 36/100 = 0,36 ✓.

</details>

<details>
<summary>▶ Solución A4</summary>

a) **0,45** = 45/100 = **9/20** (dividiendo entre 5). Comprobación: 9/20 = 45/100 = 0,45 ✓.

b) x = 0,555…; 10x = 5,555…; 10x − x = 5 → 9x = 5 → **x = 5/9**. Comprobación: 50 = 5·9 + 5, el resto 5 se repite → 0,(5) ✓.

c) x = 2,1818…; 100x = 218,1818…; 100x − x = 216 → 99x = 216 → x = 216/99 = **24/11** (dividiendo entre 9). Con la regla F9: (218 − 2)/99 = 216/99 ✓. Comprobación: 24 = 2·11 + 2; 20 = 1·11 + 9; 90 = 8·11 + 2 → resto 2 repetido → 2,(18) ✓.

d) x = 0,31212…; 10x = 3,1212…; 1000x = 312,1212…; 1000x − 10x = 309 → 990x = 309 → x = 309/990 = **103/330** (dividiendo entre 3). Con la regla F9: (312 − 3)/990 = 309/990 ✓. Comprobación: 1030 = 3·330 + 40; 400 = 1·330 + 70; 700 = 2·330 + 40 → el resto 40 se repite → 0,3(12) ✓.

e) x = 1,0666…; 10x = 10,666…; 100x = 106,666…; 100x − 10x = 96 → 90x = 96 → x = 96/90 = **16/15** (dividiendo entre 6). Con la regla F9: (106 − 10)/90 = 96/90 ✓. Comprobación: 16 = 1·15 + 1; 10 = 0·15 + 10; 100 = 6·15 + 10 → se repite → 1,0(6) ✓.

</details>

<details>
<summary>▶ Solución A5</summary>

Pasamos todo a decimal: −2,5; 7/4 = 1,75; −√4 = −2; 0,(3) = 0,333…; −3/2 = −1,5; 1,7.

**−2,5 < −√4 < −3/2 < 0,(3) < 1,7 < 7/4**

Comprobación de las comparaciones delicadas: −2,5 < −2 porque −2 − (−2,5) = 0,5 > 0. 1,7 < 1,75 porque 1,75 − 1,7 = 0,05 > 0.

```
   −3      −2      −1       0       1       2
────┼───────┼───────┼───────┼───────┼───────┼────►
        ▲   ▲   ▲              ▲          ▲▲
      −2,5  │  −3/2          0,(3)     1,7 7/4
           −√4
```

</details>

<details>
<summary>▶ Solución A6</summary>

a) **Verdadera.** Multiplicar naturales es sumar repetidamente naturales (3 · 4 = 4 + 4 + 4), y sumar naturales da un natural; además n · 0 = 0 ∈ ℕ.
b) **Falsa.** Contraejemplo: 2 − 5 = −3 ∉ ℕ.
c) **Falsa.** Contraejemplo: 1 : 2 = 1/2 ∉ ℤ.
d) **Verdadera** para **todos** los casos: es la Propiedad 1.2. a/b + c/d = (a·d + c·b)/(b·d), con numerador entero y denominador entero no nulo.
e) **Falsa.** Contraejemplo: √2 y −√2 son irracionales, pero √2 + (−√2) = 0 ∈ ℚ.
   ¿Por qué −√2 es irracional? Si fuera −√2 = a/b, entonces √2 = (−a)/b sería racional, lo que contradice el Teorema 1.1.

</details>

<details>
<summary>▶ Solución B1</summary>

**Punto medio:** (3/7 + 4/9)/2. Denominador común 63: 3/7 = 27/63 y 4/9 = 28/63. Suma: 55/63. Mitad: **55/126**.
Comprobación con denominador 126: 3/7 = 54/126 y 4/9 = 56/126, y 54 < 55 < 56 ✓.

**Tres más:** usamos un denominador mayor para «hacer sitio». Con 504 (= 63 · 8): 3/7 = 216/504 y 4/9 = 224/504. Entre 216 y 224 hay 217, 218, …, 223. Por ejemplo: **217/504, 218/504 = 109/252, 219/504 = 73/168**.

**¿Cuántos hay? Infinitos.** Razonamiento: entre 3/7 y 55/126 hay otro punto medio; entre 3/7 y ese nuevo punto, otro; y así sin fin, obteniendo cada vez un número distinto (cada uno es menor que el anterior). Es la Propiedad 1.3 aplicada una y otra vez.

</details>

<details>
<summary>▶ Solución B2</summary>

**Simplificar primero** (Error E9):

| Fracción | Irreducible | Denominador | ¿Exacto? |
|---|---|---|---|
| 21/56 | 3/8 (÷7) | 2³ | **Sí**: 0,375 |
| 33/120 | 11/40 (÷3) | 2³·5 | **Sí**: 0,275 |
| 9/14 | 9/14 | 2·7 | No: periódico mixto, 0,6(428571) |
| 6/15 | 2/5 (÷3) | 5 | **Sí**: 0,4 |
| 35/42 | 5/6 (÷7) | 2·3 | No: periódico mixto, 0,8(3) |

Las trampas son 21/56 (el 7 «desaparece» al simplificar) y 35/42 (parece tener un 7, pero lo que queda, 6, contiene un 3).

</details>

<details>
<summary>▶ Solución B3</summary>

(a) **Método 1 (restar):** x = 0,999…, 10x = 9,999…, 9x = 9, x = 1.
**Método 2 (fracciones):** 1/3 = 0,333…; multiplicando por 3: 1 = 0,999…
(También: con la regla F9, 0,(9) = 9/9 = 1.)

(b) x = 0,4999…; 10x = 4,999…; 100x = 49,999…; 90x = 45; **x = 1/2 = 0,5**.
x = 2,999…; 10x = 29,999…; 9x = 27; **x = 3**.

(c) Un decimal que termina en «(9)» es otra forma de escribir un decimal exacto: 0,4(9) = 0,5 y 2,(9) = 3. **Algunos números tienen dos expresiones decimales** (los decimales exactos distintos de 0). Por eso, por convenio, se usa la forma sin «(9)».

**Curiosidad demostrable:** la división larga **nunca** produce el periodo 9. Si un resto r produjera la cifra 9 y otra vez el mismo resto r, tendríamos 10·r = 9·b + r, es decir, 9·r = 9·b, o sea, r = b; pero un resto siempre es menor que el divisor b. Contradicción. **[VERIFICADO POR PROGRAMA]** para todas las fracciones con denominador hasta 300, aunque la demostración anterior ya lo prueba para todas.

</details>

<details>
<summary>▶ Solución B4</summary>

(a) Al dividir entre 13 los restos posibles son 0, 1, …, 12. Si en algún momento saliera el resto 0, la división terminaría y no habría periodo. Si no sale, solo quedan 12 restos posibles (1, …, 12) y, por la Propiedad 1.4, el periodo tiene **como mucho 12 cifras**.

(b)

| Paso | Resto × 10 | : 13 | Cifra | Nuevo resto |
|---|---|---|---|---|
| 1 | 10 | 10 = 0·13 + 10 | 0 | 10 |
| 2 | 100 | 100 = 7·13 + 9 | 7 | 9 |
| 3 | 90 | 90 = 6·13 + 12 | 6 | 12 |
| 4 | 120 | 120 = 9·13 + 3 | 9 | 3 |
| 5 | 30 | 30 = 2·13 + 4 | 2 | 4 |
| 6 | 40 | 40 = 3·13 + 1 | 3 | **1** ← resto inicial |

1/13 = **0,(076923)**: el periodo tiene **6 cifras**.

(c) **No hay contradicción.** En (a) obtuvimos una **cota**: un valor máximo posible («como mucho 12»). En (b) obtuvimos el **valor exacto**: 6, que es menor o igual que 12. Una cota no promete que se alcance. Esta distinción será fundamental en tu investigación: las «cotas» de la teoría de códigos (Singleton, Hamming, Griesmer… en el Módulo 21) dicen hasta dónde **podría** llegar la distancia mínima de un código, no que exista un código que llegue.

</details>

<details>
<summary>▶ Solución B5</summary>

(a) **Sí**, la conclusión es verdadera: √2 es irracional (Teorema 1.1).
(b) **No**, el razonamiento no es válido. Hay **infinitos** denominadores posibles; comprobar hasta 1000 no dice nada sobre b = 1001, b = 10⁹ o cualquier otro. Sería como decir «he mirado 1000 cajones y no he encontrado la llave, así que la llave no existe».
(c) Ha conseguido **evidencia computacional** (un resultado verificado por programa en un número finito de casos), que hace la afirmación creíble, pero no la demuestra. La demostración de verdad es la de la Ampliación A, que funciona para **todos** los denominadores a la vez.

**Conexión con tu investigación:** si un programa examina un millón de palabras de un código y no encuentra ninguna de peso menor que 5, eso **no** demuestra que la distancia mínima sea 5, salvo que haya examinado **todas** las palabras (o que exista una demostración). Esta diferencia separa una evidencia de un récord demostrado (Módulos 25 y 28).

</details>

<details>
<summary>▶ Solución B6</summary>

a) x = 4 − 9 = −5 → **ℤ** (no hay solución en ℕ).
b) x = 5/3 → **ℚ** (3 no divide a 5: no hay solución entera).
c) x = 35/5 = 7 → **ℕ**.
d) x = 3 o x = −3. Como 3 ∈ ℕ → **ℕ**.
e) x = √7 o x = −√7, irracionales (7 no es cuadrado perfecto) → **ℝ**.
f) 2x = −3, x = −3/2 → **ℚ**.

</details>

<details>
<summary>▶ Solución C1</summary>

**Datos** (1/13 ya lo calculaste en B4; 1/7 tiene un periodo de la misma longitud que el de 3/7, calculado en el Ejemplo 1.2):

| p | p − 1 | 1/p | Longitud del periodo |
|---|---|---|---|
| 3 | 2 | 0,(3) | 1 |
| 7 | 6 | 0,(142857) | 6 |
| 11 | 10 | 0,(09) | 2 |
| 13 | 12 | 0,(076923) | 6 |
| 17 | 16 | 0,(0588235294117647) | 16 |
| 19 | 18 | 0,(052631578947368421) | 18 |
| 23 | 22 | 0,(0434782608695652173913) | 22 |

**Conjetura esperada:** «Para todo primo p distinto de 2 y de 5, la longitud del periodo de 1/p **divide** a p − 1.» (1 divide a 2; 6 divide a 6; 2 divide a 10; 6 divide a 12; 16 divide a 16…). Observación adicional: a veces la longitud es **exactamente** p − 1 (7, 17, 19, 23) y a veces es más pequeña (3, 11, 13).

**Tipo de evidencia:** 6 o 7 ejemplos calculados a mano (y el programa de verificación los confirma). Es **evidencia**, no demostración.

**Cómo intentar refutarla:** calcular más primos (29, 31, 37, 41…), buscando uno cuya longitud de periodo **no** divida a p − 1. Un solo caso así la refutaría.

**Estado real:** esta conjetura es **verdadera**: es un teorema que se deduce del *pequeño teorema de Fermat*, que demostrarás en el capítulo 14.5. Que la hayas descubierto a partir de datos es exactamente cómo trabaja un investigador: **datos → patrón → conjetura → demostración**. Y fíjate en que no sabíamos que era verdadera hasta tener la demostración: muchos patrones que se cumplen en los primeros casos fallan más adelante (verás ejemplos célebres en el capítulo 10.10).

</details>

<details>
<summary>▶ Solución C2</summary>

**Tablas** (solo filas y columnas 1 a n − 1, porque el 0 nunca tiene pareja: 0 ⊗ b = 0):

```
 n = 4          n = 5            n = 6              n = 8
 ⊗ │ 1 2 3      ⊗ │ 1 2 3 4      ⊗ │ 1 2 3 4 5      ⊗ │ 1 2 3 4 5 6 7
───┼──────     ───┼────────     ───┼──────────     ───┼──────────────
 1 │ 1 2 3      1 │ 1 2 3 4      1 │ 1 2 3 4 5      1 │ 1 2 3 4 5 6 7
 2 │ 2 0 2      2 │ 2 4 1 3      2 │ 2 4 0 2 4      2 │ 2 4 6 0 2 4 6
 3 │ 3 2 1      3 │ 3 1 4 2      3 │ 3 0 3 0 3      3 │ 3 6 1 4 7 2 5
                4 │ 4 3 2 1      4 │ 4 2 0 4 2      4 │ 4 0 4 0 4 0 4
                                 5 │ 5 4 3 2 1      5 │ 5 2 7 4 1 6 3
                                                   6 │ 6 4 2 0 6 4 2
                                                   7 │ 7 6 5 4 3 2 1
```

**¿Quién no tiene pareja?**
- n = 4: el **2** (su fila es 2, 0, 2: no aparece el 1). Parejas: 1↔1, 3↔3.
- n = 5: **todos tienen pareja**: 1↔1, 2↔3, 4↔4.
- n = 6: **2, 3 y 4** no tienen pareja. Parejas: 1↔1, 5↔5.
- n = 7: **todos tienen pareja** (Ejemplo 1.3).
- n = 8: **2, 4 y 6** no tienen pareja. Parejas: 1↔1, 3↔3, 5↔5, 7↔7.

**Conjetura:** «Todo número no nulo tiene pareja con el reloj de n **exactamente cuando n es primo**.»

**Predicción y comprobación:** 9 y 10 no son primos → predicción: fallará; 11 es primo → predicción: funcionará.
- n = 9: el 3 y el 6 no tienen pareja (3·1 = 3, 3·2 = 6, 3·3 = 9 → 0, … los múltiplos de 3 nunca dejan resto 1 al dividir entre 9). ✓ falla.
- n = 10: no tienen pareja 2, 4, 5, 6 y 8. ✓ falla.
- n = 11: todos tienen pareja: 1↔1, 2↔6, 3↔4, 5↔9, 7↔8, 10↔10. (Por ejemplo, 5 · 9 = 45 = 4 · 11 + 1.) ✓ funciona.

**[VERIFICADO POR PROGRAMA]** Para n de 2 a 11, los valores en los que todos tienen pareja son exactamente 2, 3, 5, 7 y 11, los primos.

**¿Por qué falla si n no es primo?** Si n = a · b con a y b entre 2 y n − 1, entonces a ⊗ b = 0 (el resto de dividir n entre n es 0). Supongamos que a tuviera pareja c, con a ⊗ c = 1. Entonces, operando con el reloj de n:
b = b ⊗ 1 = b ⊗ (a ⊗ c) = (b ⊗ a) ⊗ c = 0 ⊗ c = 0,
pero b está entre 2 y n − 1, así que no es 0. **Contradicción:** a no puede tener pareja. (Este argumento usa que ⊗ se puede reagrupar y cambiar de orden igual que la multiplicación normal; lo justificaremos en el capítulo 2.8.)

**La otra mitad** (si n es primo, todos tienen pareja) necesita la *identidad de Bézout* (capítulo 2.7) y se demostrará en el Módulo 13. Por ahora, es una **conjetura bien apoyada** para ti, aunque sea un teorema conocido.

</details>

<details>
<summary>▶ Solución P1</summary>

a) De −3 a 5: 5 − (−3) = 5 + 3 = **8 plantas**. De 4 a −2: el cambio es −2 − 4 = **−6** (6 plantas hacia abajo).

b) Le faltan 4,5 °C para llegar a 0. A 0,75 °C por hora: 4,5 : 0,75 = 450 : 75 = **6 horas** → a las **12:00**.
A las 14:00 han pasado 8 horas: −4,5 + 8 · 0,75 = −4,5 + 6 = **1,5 °C**.
Comprobación: a las 12:00 está a 0 °C y en 2 horas más sube 2 · 0,75 = 1,5 °C ✓.

c) **ℤ** para las plantas bajo tierra y las temperaturas bajo cero (restas como 5 − 8 sin solución en ℕ); **ℚ** (decimales exactos) para 4,5 y 0,75; **ℕ** para contar horas.

</details>

<details>
<summary>▶ Solución P2</summary>

a) 10 · 0,10 = **1,00 €**.

b) El ordenador no guarda 0,1 exactamente, sino una aproximación (en base 2, 1/10 es periódico y el periodo se recorta). Cada suma acumula un error diminuto, y al final se obtiene 0,9999999999999999 en vez de 1. **[VERIFICADO POR PROGRAMA]** con Python 3.13.16.

   ⚠️ **Un detalle que enseña mucho:** si en vez de sumar una a una se usa la función `sum([0.1] * 10)`, en Python 3.12 o posterior el resultado es `1.0` (comprobado aquí con Python 3.13.16), porque desde la versión 3.12 `sum` usa un método de suma más preciso; en versiones anteriores daba `0.9999999999999999`. **El mismo cálculo puede dar resultados distintos según la versión del programa**: por eso, en el Módulo 9, aprenderás a anotar siempre la versión de Python con la que obtienes cada resultado. Pero el problema de fondo no desaparece: `0.1 + 0.2 == 0.3` sigue siendo `False`.

c) **Trabajar en céntimos**, que son números enteros: 2,35 € = 235 céntimos; 0,99 € = 99; 12,10 € = 1210; 0,56 € = 56.
   235 + 99 + 1210 + 56 = **1600 céntimos = 16,00 €**. Con enteros, el ordenador es exacto.
   Comprobación sumando en euros: 2,35 + 0,99 = 3,34; 3,34 + 12,10 = 15,44; 15,44 + 0,56 = 16,00 ✓.

d) Es la misma idea: en GF(7) **todo son enteros** (0, …, 6) y los resultados se obtienen con restos de divisiones enteras, así que el ordenador calcula **sin errores de redondeo**. Por eso los cálculos de códigos sobre GF(7) pueden ser exactos y verificables.

</details>

<details>
<summary>▶ Solución PC</summary>

Numeramos: lunes = 0, martes = 1, miércoles = 2, jueves = 3, viernes = 4, sábado = 5, domingo = 6.

a) 23 = 3 · 7 + **2**. Tres semanas completas nos devuelven al lunes; faltan 2 días: **miércoles**.

b) 100 = 14 · 7 + **2** → **miércoles** (de nuevo resto 2).

c) **Forma 1 (hacia atrás):** 10 = 7 + 3. Retroceder 7 días nos deja en lunes; retroceder 3 más: domingo, sábado, **viernes**.
   **Forma 2 (hacia delante):** retroceder 10 días y luego avanzar 14 (dos semanas) nos deja en el mismo día de la semana que avanzar 4 días desde hoy. Lunes + 4 = **viernes** ✓.
   (Fíjate: −10 = −2 · 7 + 4. El «resto» de −10 entre 7, tomado entre 0 y 6, es 4. Los restos de números negativos se estudian en el capítulo 2.5.)

d) Cada bloque de 7 días nos devuelve exactamente al mismo día de la semana, así que los bloques completos (el cociente) no cambian nada: solo importan los días «sobrantes», es decir, el **resto**.

e) 100/7 = 14,(285714) semanas. La parte decimal es 0,(285714) = **2/7** de semana, es decir, 2 días: ¡exactamente el resto del apartado b! Comprobación: 2/7 = 0,(285714), ya que 20 = 2·7 + 6; 60 = 8·7 + 4; 40 = 5·7 + 5; 50 = 7·7 + 1; 10 = 1·7 + 3; 30 = 4·7 + 2 → resto 2 inicial.
   En general: a/7 = cociente + resto/7.

</details>

---

<a id="s15"></a>
## 15. Preguntas de comprensión

Responde con tus palabras, en 2–5 líneas cada una. No son cálculos: son para comprobar que **entiendes**. Las respuestas modelo están en el anexo final.

1. ¿Por qué se dice que ℚ «resuelve» todas las divisiones (entre números no nulos) pero no todas las raíces cuadradas?
2. Si un número tiene infinitas cifras decimales, ¿es necesariamente irracional? Explícalo con un ejemplo.
3. ¿Qué diferencia hay entre «2 ∈ ℕ» y «{2} ⊂ ℕ»? ¿Son verdaderas las dos?
4. Explica, sin hacer la división, por qué 1/7 tiene que acabar repitiéndose.
5. ¿Por qué un solo contraejemplo basta para demostrar que una afirmación «para todo…» es falsa, pero mil ejemplos no bastan para demostrar que es verdadera?
6. ¿Por qué en la investigación con GF(7) no conviene usar los decimales del ordenador?
7. Un compañero dice: «0,(9) y 1 son números distintos porque se escriben distinto». ¿Qué le responderías?
8. ¿Qué tiene de especial el «reloj de 7» frente al «reloj de 6»?

---

<a id="s16"></a>
## 16. Prueba de dominio

**Instrucciones:** sin mirar el capítulo ni las soluciones. Tiempo recomendado: 40 minutos. Cada pregunta vale 1 punto. Las preguntas marcadas con ★ son **críticas**.

**Criterio para dar el capítulo por dominado:** **8 puntos o más** y **todas las preguntas ★ correctas**. Si no lo consigues, no pasa nada: usa la tabla de diagnóstico, haz los ejercicios de refuerzo y repite la prueba otro día (preferiblemente pidiendo a tu tutor una versión con otros números).

**D1 ★.** Clasifica (ℕ, ℤ, ℚ, 𝕀): −7/7;  √49/2;  0,1(23);  √3;  −0,5.

**D2 ★.** Halla la fracción generatriz irreducible de 0,2(7) y comprueba el resultado dividiendo.

**D3.** Sin dividir, di qué tipo de decimal dan: 7/20;  5/6;  2/9;  15/48.

**D4 ★.** Da un contraejemplo de: «La diferencia de dos números naturales es siempre un número natural».

**D5.** Encuentra un número racional entre −1/3 y −1/4.

**D6.** Ordena de menor a mayor: 0,(6);  2/3;  0,67;  0,6.

**D7.** Verdadero o falso, con justificación: «Todo decimal exacto es un número racional».

**D8 ★.** Explica en tres líneas como máximo por qué un ordenador responde `False` a `0.1 + 0.2 == 0.3`, y qué consecuencia tiene para tus cálculos con GF(7).

**D9.** Para cada ecuación, di el conjunto más pequeño (ℕ, ℤ, ℚ o ℝ) en el que tiene solución: 4x = −6;  x + 10 = 3;  x² = 5.

**D10.** ¿Puede el periodo de a/17 tener 20 cifras? Justifica tu respuesta sin hacer ninguna división.

### Tabla de diagnóstico

Si fallas una pregunta, el problema está en el concepto indicado. Vuelve a la sección, haz el ejercicio de refuerzo y explica en voz alta (o por escrito) en qué consistía tu error.

| Pregunta | Concepto evaluado | Repasa | Refuerzo |
|---|---|---|---|
| D1 | Clasificar números (simplificar primero) | §4.2, Ejemplo 1.1, §5.2 | RF1 |
| D2 | Fracción generatriz de un periódico mixto | §4.3, Prop. 1.6, Ejemplo 1.2 (c), F9 | RF2 |
| D3 | Criterio del denominador (fracción irreducible) | Prop. 1.5, §5.3 | RF3 |
| D4 | Operación cerrada y contraejemplo | §4.5, Prop. 1.2 | RF4 |
| D5 | Densidad de ℚ (punto medio) | Prop. 1.3, F7 | B1 |
| D6 | Orden y equivalencia 0,(6) = 2/3 | §4.4, Ejemplo 1.1 (n.º 7) | RF5 |
| D7 | Decimal exacto ⟹ racional | Prop. 1.6, F8 | A4 a) |
| D8 | Exactitud en el ordenador | Ejemplo 1.3 (a), Ampliación C | P2 |
| D9 | Por qué existe cada conjunto | §3.1 | B6 |
| D10 | Cota del periodo (argumento de los restos) | Prop. 1.4, F10 | B4 |

### Ejercicios de refuerzo

**RF1.** Clasifica: −20/5;  0,0(5);  √50;  √0,25;  3/1.
**RF2.** Fracción generatriz y comprobación: 0,1(6);  3,(7);  0,(142857).
**RF3.** Sin dividir, predice el tipo de decimal y después compruébalo dividiendo: 11/16;  7/15;  5/33.
**RF4.** Da un contraejemplo de cada afirmación: (a) «El cociente de dos naturales (divisor no nulo) es natural.» (b) «El producto de dos irracionales es irracional.» (c) «Todo número negativo es entero.»
**RF5.** Ordena de menor a mayor: −0,(3);  −1/4;  −0,3;  −0,33.

(Soluciones en el anexo final.)

---

<a id="s17"></a>
## 17. Relación con el siguiente capítulo

En este capítulo has visto **qué números existen** y **por qué**. En el **capítulo 1.2 (Números enteros: signos, valor absoluto, orden y jerarquía de operaciones)** aprenderás a **operar** con enteros sin errores: reglas de los signos, paréntesis, prioridad de las operaciones y valor absoluto.

¿Por qué es imprescindible para tu objetivo? Porque toda la aritmética de GF(7) se construye sobre la aritmética de los **enteros**: en el Ejemplo 1.3 y en el problema del calendario ya has visto que el «reloj de 7» consiste en operar con enteros y quedarse con un resto. Y cuando aparezcan restas como 2 − 5 en GF(7), o restos de números negativos (como en el apartado c del problema del calendario), necesitarás dominar los enteros con total seguridad.

A partir del capítulo 1.2, cada capítulo incluirá una sección **«Recupera»** con problemas nuevos sobre capítulos anteriores, para que lo aprendido aquí no se olvide.

**Antes de pasar al capítulo 1.2:**

- [ ] He hecho todos los ejercicios de nivel A y, al menos, B1, B2, B4 y B5.
- [ ] He intentado C1 y C2 (no es obligatorio acertarlos para avanzar, pero sí intentarlos).
- [ ] He respondido las 8 preguntas de comprensión y las he comparado con las respuestas modelo.
- [ ] He superado la prueba de dominio (≥ 8 puntos y todas las ★).
- [ ] He anotado mis errores en `PROGRESO.md`.

---

## Ampliaciones (opcionales en una primera lectura)

<a id="ampA"></a>
### Ampliación A — Demostración de que √2 es irracional (Teorema 1.1)

**Idea del método (reducción al absurdo).** Suponemos lo **contrario** de lo que queremos demostrar y deducimos, paso a paso, algo imposible. Si de una suposición se deduce algo imposible, la suposición era falsa. (Lo estudiarás con todo detalle en el capítulo 10.7.)

**Un hecho que necesitamos: el cuadrado de un número impar es impar.**
- *Con las últimas cifras:* un impar termina en 1, 3, 5, 7 o 9; su cuadrado termina, respectivamente, en 1, 9, 5, 9 o 1 (porque 1·1 = 1, 3·3 = 9, 5·5 = 25, 7·7 = 49, 9·9 = 81, y la última cifra de un producto solo depende de las últimas cifras de los factores). Todas son impares.
- *Con álgebra* (usa una identidad notable que repasarás en el capítulo 3.4): un impar es 2m + 1; su cuadrado es (2m + 1)² = 4m² + 4m + 1 = 2·(2m² + 2m) + 1, que es impar.

En consecuencia: **si a² es par, entonces a es par** (porque si a fuera impar, a² sería impar).

**Demostración.**
1. **Suponemos lo contrario:** √2 es racional. Entonces √2 = a/b con a y b naturales, b ≠ 0, y podemos tomar la fracción **irreducible** (a y b sin divisores comunes mayores que 1).
2. Elevando al cuadrado: 2 = a²/b², es decir, **a² = 2b²**.
3. Entonces a² es par (es 2 por algo). Por el hecho anterior, **a es par**: a = 2c para algún natural c.
4. Sustituyendo: (2c)² = 2b² → 4c² = 2b² → **b² = 2c²**.
5. Entonces b² es par y, por el mismo hecho, **b es par**.
6. Pero si a y b son pares, ambos son divisibles entre 2, y la fracción a/b **no** era irreducible. Esto contradice el paso 1. ∎

Como la suposición «√2 es racional» lleva a una contradicción, es falsa: **√2 es irracional**. Observa que esta demostración vale para **todas** las fracciones a la vez, cosa que ningún programa de ordenador puede hacer probando casos (ejercicio B5).

<a id="ampB"></a>
### Ampliación B — ¿Qué es realmente ℝ?

La Definición 1.6 («los números que se escriben con un decimal») es intuitiva, pero esconde preguntas difíciles: ¿cómo se suman dos decimales infinitos, si no hay «última cifra» por la que empezar? ¿Por qué la recta numérica no tiene «agujeros»? En el siglo XIX, matemáticos como Richard Dedekind y Georg Cantor construyeron ℝ con rigor a partir de ℚ. Esa construcción se estudia en el primer curso universitario de Análisis Matemático.

**Para tu investigación no la necesitarás.** Los códigos sobre GF(7) viven en conjuntos **finitos**. Los números reales aparecerán solo de forma auxiliar: al comparar tamaños (logaritmos, capítulo 4.5) y en algunas cotas asintóticas (Módulo 21).

<a id="ampC"></a>
### Ampliación C — ¿Por qué 0,1 no es exacto en el ordenador?

En base 10, una fracción irreducible da un decimal exacto solo si su denominador tiene únicamente los factores primos de 10, que son 2 y 5 (Propiedad 1.5). En **base 2** pasa lo mismo, pero con los factores primos de 2, que es solo el 2: una fracción da una expresión **exacta en base 2** solo si su denominador es una potencia de 2 (2, 4, 8, 16, …).

Como 1/10 tiene denominador 10 = 2 · 5, y el 5 no es potencia de 2, **en base 2 es periódico**. Haciendo la «división larga en base 2» (multiplicando el resto por 2 en lugar de por 10) se obtiene:

1/10 = 0,0(0011) en base 2 = 0,0001100110011… en base 2.

**[VERIFICADO POR PROGRAMA]** `verificar_cap_1_1.py` calcula este desarrollo con la misma función que usa para la base 10, cambiando solo la base.

El ordenador guarda solo 53 cifras binarias significativas (en el formato habitual de los `float`), así que recorta el periodo y almacena un número muy próximo a 0,1, pero no igual. Lo estudiarás en el capítulo 8.7.

---

## Anexo — Respuestas de comprensión, prueba de dominio y refuerzo

> ⚠️ No abras este anexo hasta haber hecho la prueba de dominio completa.

<details>
<summary>▶ Respuestas modelo de las preguntas de comprensión (§15)</summary>

1. Porque ℚ es cerrado para la división (Prop. 1.2): el cociente de dos fracciones (divisor no nulo) es otra fracción. Pero hay raíces, como √2, cuyo valor no es ninguna fracción (Teorema 1.1). Para tenerlas hace falta ampliar hasta ℝ.
2. No. 1/3 = 0,333… tiene infinitas cifras y es racional. Lo que caracteriza a los irracionales es ser infinitos **y no periódicos**.
3. «2 ∈ ℕ» dice que el **número** 2 es un elemento de ℕ. «{2} ⊂ ℕ» dice que el **conjunto** cuyo único elemento es el 2 está contenido en ℕ. Las dos son verdaderas, pero relacionan objetos de distinto tipo.
4. En la división larga entre 7, los restos solo pueden ser 0, 1, …, 6. Si saliera el 0, la división terminaría; si no sale, solo hay 6 restos posibles (1, …, 6), y en cuanto se repite uno, todo lo que viene después se repite, porque cada paso depende solo del resto anterior.
5. Una afirmación «para todo» dice que **no hay ninguna** excepción: una sola excepción la hace falsa. Pero los casos posibles suelen ser infinitos, y por muchos que compruebes siempre quedan infinitos sin comprobar; solo un razonamiento general cubre todos los casos a la vez.
6. Porque los decimales del ordenador (`float`) son aproximaciones y pueden dar resultados falsos (0.1 + 0.2 ≠ 0.3). En GF(7) todo son enteros y restos, con los que el ordenador es exacto; así los resultados son verificables.
7. Que un mismo número puede tener varias escrituras (como 1/2 y 2/4). La resta 10x − x con x = 0,999… da 9x = 9, x = 1. Además, intuitivamente: si fueran distintos, habría algún número entre ellos (su punto medio), y no hay ninguna expresión decimal que quede entre 0,999… y 1.
8. Con el reloj de 7, todo número distinto de 0 tiene pareja (un número que multiplicado por él da 1), así que se puede dividir entre cualquier número no nulo, y el producto de dos números no nulos nunca es 0. Con el reloj de 6, 2 ⊗ 3 = 0 y el 2, el 3 y el 4 no tienen pareja. La diferencia es que 7 es primo y 6 no.

</details>

<details>
<summary>▶ Soluciones de la prueba de dominio (§16)</summary>

**D1 ★.** −7/7 = −1 → ℤ (y ℚ, ℝ; no ℕ). √49/2 = 7/2 → ℚ (no ℤ). 0,1(23) → periódico → ℚ. √3 → 3 no es cuadrado perfecto → 𝕀. −0,5 = −1/2 → ℚ (no ℤ).

**D2 ★.** x = 0,2777…; 10x = 2,777…; 100x = 27,777…; 100x − 10x = 25 → 90x = 25 → x = 25/90 = **5/18**. (Regla F9: (27 − 2)/90 = 25/90 ✓.)
Comprobación: 50 = 2·18 + 14; 140 = 7·18 + 14 → el resto 14 se repite → 0,2(7) ✓.

**D3.** 7/20: 20 = 2²·5 → **exacto** (0,35). 5/6: 6 = 2·3 → **periódico mixto** (0,8(3)). 2/9: 9 = 3² → **periódico puro** (0,(2)). 15/48 = 5/16 (¡simplificar!): 16 = 2⁴ → **exacto** (0,3125).

**D4 ★.** Por ejemplo, 3 − 7 = −4 ∉ ℕ. (Cualquier resta de un natural menos otro mayor sirve.)

**D5.** Con denominador 24: −1/3 = −8/24 y −1/4 = −6/24. Entre ellos: **−7/24** (también vale el punto medio, que es justamente −7/24). Comprobación: −8/24 < −7/24 < −6/24 ✓.

**D6.** 0,(6) = 2/3 = 0,666… Entonces **0,6 < 0,(6) = 2/3 < 0,67**. (0,6 < 0,666… porque la segunda cifra decimal 0 < 6; 0,666… < 0,67 porque la segunda cifra decimal 6 < 7.)

**D7.** **Verdadero.** Un decimal exacto con m cifras decimales es N/10^m (por ejemplo, 2,35 = 235/100), que es una fracción de enteros con denominador no nulo (Prop. 1.6).

**D8 ★.** Respuesta modelo: «El ordenador guarda los decimales en base 2, donde 0,1 y 0,2 son periódicos, así que solo guarda aproximaciones; al sumar, el pequeño error hace que el resultado no sea exactamente 0,3. En GF(7) hay que usar solo enteros (y restos), con los que el ordenador es exacto.» Se considera correcta si menciona **aproximación/redondeo** y **usar enteros**.

**D9.** 4x = −6 → x = −3/2 → **ℚ**. x + 10 = 3 → x = −7 → **ℤ**. x² = 5 → x = ±√5 → **ℝ**.

**D10.** **No.** Al dividir entre 17 hay como mucho 16 restos no nulos (1, …, 16), y en cuanto uno se repite empieza el periodo. Por tanto, el periodo tiene **como mucho 16 cifras** (Prop. 1.4). (De hecho, para 1/17 tiene exactamente 16.)

</details>

<details>
<summary>▶ Soluciones de los ejercicios de refuerzo</summary>

**RF1.** −20/5 = −4 → ℤ. 0,0(5) → periódico → ℚ (es 1/18). √50 → 49 < 50 < 64, no es cuadrado perfecto → 𝕀. √0,25 = 0,5, porque 0,5 · 0,5 = 0,25 → ℚ (no ℤ). 3/1 = 3 → ℕ.

**RF2.**
- 0,1(6): 10x = 1,666…; 100x = 16,666…; 90x = 15; x = 15/90 = **1/6**. Comprobación: 10 = 1·6 + 4; 40 = 6·6 + 4 → 0,1(6) ✓.
- 3,(7): x = 3,777…; 10x = 37,777…; 9x = 34; x = **34/9**. Comprobación: 34 = 3·9 + 7; 70 = 7·9 + 7 → 3,(7) ✓.
- 0,(142857): x = 142857/999999 = **1/7**, porque 999999 = 7 · 142857. Comprobación: es el desarrollo de 1/7 (ver tabla de C1) ✓.

**RF3.** 11/16: 16 = 2⁴ → exacto: **0,6875**. 7/15: 15 = 3·5 → mixto: **0,4(6)**. 5/33: 33 = 3·11 → puro: **0,(15)**.

**RF4.** (a) 3 : 2 = 3/2 ∉ ℕ. (b) √2 · √2 = 2 ∈ ℚ. (c) −1/2 es negativo y no es entero.

**RF5.** En decimal: −0,333…; −0,25; −0,3; −0,33. Entre negativos, el que está más lejos del 0 es el menor: **−0,(3) < −0,33 < −0,3 < −1/4**.

</details>

---

## Referencias del capítulo

- G. H. Hardy y E. M. Wright, *An Introduction to the Theory of Numbers*, Oxford University Press (6.ª ed., revisada por D. R. Heath-Brown y J. H. Silverman, 2008). Contiene la demostración de la irracionalidad de √2 y un estudio completo de las expresiones decimales de los racionales (longitud del periodo). *Referencia clásica; datos bibliográficos citados de memoria, no verificados en línea en esta sesión.*
- D. Goldberg, «What Every Computer Scientist Should Know About Floating-Point Arithmetic», *ACM Computing Surveys*, 23(1), 1991, pp. 5–48. Explicación detallada de los `float`. *Referencia clásica; no verificada en línea en esta sesión.*
- Documentación oficial de Python, «Floating-Point Arithmetic: Issues and Limitations»: https://docs.python.org/3/tutorial/floatingpoint.html — *el enlace no se pudo abrir desde el entorno de redacción; la página existe en la documentación oficial, pero comprueba el enlace tú mismo.*
- Ministerio de Educación y Formación Profesional, *Real Decreto 217/2022, de 29 de marzo*, por el que se establece la ordenación y las enseñanzas mínimas de la ESO (saberes básicos de Matemáticas: sentido numérico). *Citado de memoria; no verificado en línea en esta sesión.*

Todas las afirmaciones «verificadas por programa» de este capítulo se pueden reproducir ejecutando:

```
python3 codigo/verificaciones/verificar_cap_1_1.py
```

---

## Registro personal del capítulo 1.1

Copia esta ficha en `PROGRESO.md` cuando termines:

```
Capítulo 1.1 — Conjuntos de números
Fecha de inicio:                Fecha de la prueba de dominio:
Puntuación prueba de dominio:  __/10    ¿Todas las ★ correctas? Sí / No
Ejercicios hechos:  A1 A2 A3 A4 A5 A6 | B1 B2 B3 B4 B5 B6 | C1 C2 | P1 P2 PC
Ejercicios fallados y concepto:
Preguntas de comprensión que me costaron:
¿Dominado?  Sí / No (repetir prueba el día: ______)
```
