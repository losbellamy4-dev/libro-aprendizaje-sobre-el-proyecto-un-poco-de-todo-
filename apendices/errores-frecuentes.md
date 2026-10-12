# Apéndice C — Errores frecuentes y cómo corregirlos

> Lista acumulada de todos los capítulos. Para cada error: qué se hace mal, por qué está mal y cómo
> detectarlo. Úsala como lista de comprobación antes de entregar un ejercicio o un resultado.
> Los errores **personales** (los tuyos) se anotan aparte, en [`PROGRESO.md`](../PROGRESO.md).

## Capítulo 1.1 — Conjuntos de números

| Código | Error | Por qué está mal | Cómo detectarlo / corregirlo |
|---|---|---|---|
| 1.1-E1 | Clasificar −12/4 como «no entero» por estar escrito como fracción. | Lo que decide es el valor: −12/4 = −3. | Simplifica siempre antes de clasificar. |
| 1.1-E2 | «Infinitas cifras decimales ⟹ irracional.» | 1/3 = 0,333… es racional. | ¿Hay un bloque que se repite? Entonces es racional. |
| 1.1-E3 | π = 3,14 o π = 22/7. | Son aproximaciones racionales de un irracional. | Usa ≈. |
| 1.1-E4 | 0,(9) < 1. | 0,(9) = 1. | Resta 10x − x. |
| 1.1-E5 | «Toda raíz cuadrada es irracional.» | √9 = 3. | Comprueba si es un cuadrado perfecto. |
| 1.1-E6 | Escribir 2 ⊂ ℕ. | ⊂ relaciona conjuntos; ∈ relaciona elemento y conjunto. | 2 ∈ ℕ, {2} ⊂ ℕ. |
| 1.1-E7 | −7 > −3. | Entre negativos, el más alejado de 0 es el menor. | Calcula la diferencia: −3 − (−7) = 4 > 0, luego −7 < −3. |
| 1.1-E8 | Generatriz de un periódico mixto como si fuera puro (0,41(6) = 416/999). | Se ignora el anteperiodo. | Comprueba dividiendo la fracción obtenida. |
| 1.1-E9 | Aplicar el criterio del denominador sin simplificar (21/56). | El criterio exige fracción irreducible. | Simplifica primero. |
| 1.1-E10 | Tomar ejemplos como demostración. | Los casos son infinitos. | Etiqueta como conjetura hasta tener una demostración. |
| 1.1-E11 | Dividir entre 0 o creer que 0/5 no existe. | a/0 no está definido; 0/5 = 0. | ¿Qué número multiplicado por el divisor da el dividendo? |
| 1.1-E12 | Escribir `0,75` en Python. | Python usa punto decimal. | En el código: `0.75`. |
| 1.1-E13 | Comparar `float` con `==`. | Los `float` son aproximaciones. | En GF(7), solo enteros; para fracciones exactas, `Fraction`. |
| 1.1-E14 | Confundir una cota con el valor exacto. | «Como mucho b − 1» no significa «exactamente b − 1». | Distingue ≤ de =. |
| 1.1-E15 | Suponer que un programa da el mismo resultado en cualquier versión. | `sum([0.1]*10)` da `1.0` en Python ≥ 3.12 y `0.9999999999999999` en versiones anteriores. | Anota siempre la versión con la que obtienes un resultado. |
