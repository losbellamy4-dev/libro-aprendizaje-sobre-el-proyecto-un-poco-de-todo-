# Apéndice D — Bibliografía comentada

> **Regla de honestidad:** cada referencia indica su **estado de verificación**. No se ha inventado
> ninguna referencia, pero no todas se han podido comprobar en línea al redactar el libro. Antes de
> citar una fuente en un trabajo propio, **ábrela y compruébala tú mismo** (autores, título, año,
> páginas). Aprender a hacerlo forma parte del Módulo 28.

**Leyenda de estado**

| Estado | Significado |
|---|---|
| 🟢 **Verificada (búsqueda web, 12/10/2026)** | Se ha confirmado por búsqueda web que existe y los datos indicados coinciden. Lo que no se pudo confirmar se señala aparte. |
| 🟡 **Clásica, citada de memoria** | Obra de referencia muy conocida en su campo; los datos se han escrito de memoria y **no** se han comprobado en línea en esta sesión. |
| 🔴 **Enlace no comprobado** | El enlace no se pudo abrir desde el entorno de redacción. |

---

## 1. Teoría de códigos (libros de texto)

Ordenados de más accesible a más avanzado. Los usarás a partir de la Parte V.

1. 🟡 **R. Hill**, *A First Course in Coding Theory*, Oxford University Press (Clarendon Press), 1986.
   Probablemente el texto más amable para empezar; trata códigos lineales sobre GF(q), matrices generadoras y de control, y cotas. **Recomendado como primer libro de códigos.**
2. 🟡 **S. Ling y C. Xing**, *Coding Theory: A First Course*, Cambridge University Press, 2004.
   Muy claro; incluye campos finitos, códigos cíclicos, BCH y Reed–Solomon con muchos ejercicios.
3. 🟡 **W. C. Huffman y V. Pless**, *Fundamentals of Error-Correcting Codes*, Cambridge University Press, 2003.
   Referencia estándar de nivel universitario: cotas, códigos cíclicos, códigos sobre GF(q), enumeradores de pesos. Lo usarás en los Módulos 21, 22 y 27.
4. 🟡 **J. H. van Lint**, *Introduction to Coding Theory*, Springer (Graduate Texts in Mathematics 86), 3.ª ed., 1999.
   Conciso y riguroso; para cuando domines las demostraciones (Módulo 10 en adelante).
5. 🟡 **F. J. MacWilliams y N. J. A. Sloane**, *The Theory of Error-Correcting Codes*, North-Holland, 1977.
   La «enciclopedia» clásica de la teoría de códigos. Para consultar, no para aprender desde cero.
6. 🟡 **A. E. Brouwer**, «Bounds on the size of linear codes», en V. S. Pless y W. C. Huffman (eds.), *Handbook of Coding Theory*, Elsevier, 1998.
   Origen de las tablas de mejores códigos lineales conocidos que después continuó M. Grassl (ver §3).

## 2. Campos finitos, álgebra y matemáticas discretas

7. 🟡 **R. Lidl y H. Niederreiter**, *Introduction to Finite Fields and Their Applications*, Cambridge University Press, ed. revisada, 1994.
   Para el Módulo 16. (Existe una obra más extensa de los mismos autores, *Finite Fields*, en la colección *Encyclopedia of Mathematics and its Applications*, vol. 20, CUP.)
8. 🟡 **G. H. Hardy y E. M. Wright**, *An Introduction to the Theory of Numbers*, Oxford University Press, 6.ª ed. (revisada por D. R. Heath-Brown y J. H. Silverman), 2008.
   Teoría de números clásica: irracionalidad, decimales periódicos, congruencias, Fermat. Capítulos 1.1, Módulos 2 y 14.
9. 🟡 **G. Strang**, *Introduction to Linear Algebra*, Wellesley-Cambridge Press (varias ediciones).
   Álgebra lineal con mucha intuición, para el Módulo 12 (trabaja sobre los reales; la versión sobre campos finitos la verás en el Módulo 13).
10. 🟡 **K. H. Rosen**, *Discrete Mathematics and Its Applications*, McGraw-Hill (varias ediciones).
    Lógica, conjuntos, combinatoria, inducción, aritmética modular. Módulos 5, 10, 11 y 14.
11. 🟡 **D. J. Velleman**, *How to Prove It: A Structured Approach*, Cambridge University Press (3.ª ed., 2019).
    El mejor libro para aprender a leer y escribir demostraciones. Módulo 10.
12. 🟡 **G. Pólya**, *How to Solve It*, Princeton University Press, 1945. Traducción española: *Cómo plantear y resolver problemas*, Editorial Trillas.
    Método general de resolución de problemas. Capítulo 3.11 y Módulo 30.

## 3. Tablas de códigos, bases de datos y artículos relacionados con GF(7)

13. 🟢 **M. Grassl**, *Bounds on the minimum distance of linear codes and quantum codes* (tablas en línea), http://www.codetables.de
    **Verificado:** búsquedas web confirman que las tablas existen, que las mantiene Markus Grassl y que continúan las tablas de A. E. Brouwer; la documentación de SageMath indica que su función de consulta a esta base admite los cuerpos de 2, 3, 4, 5, **7**, 8 y 9 elementos. 🔴 La página no se pudo abrir directamente desde el entorno de redacción. **Es la referencia principal para saber si un código [n, k, d]₇ mejora lo conocido** (Módulos 21.8, 28.8).
14. 🟢 **«Some results on the structure of constacyclic codes and new linear codes over GF(7) from quasi-twisted codes»**, *Advances in Mathematics of Communications*, 11(1), 2017, pp. 245–258. DOI: 10.3934/amc.2017016. Página del editor: https://www.aimsciences.org/article/doi/10.3934/amc.2017016
    **Verificado:** revista, volumen, páginas y DOI; según el resumen, los autores encuentran 41 códigos cuasitwisted sobre GF(7) con mejores parámetros que los mejores códigos lineales conocidos entonces, y obtienen otros mediante la Construcción X, acortamiento y pinchado. 🟡 **Autores no confirmados en la búsqueda**; según mi conocimiento son N. Aydin, N. Connolly y M. Grassl: compruébalo en la página del editor. **Directamente relacionado con tu investigación** (Módulos 22.9, 27, 29).
15. 🟢 **E. Z. Chen y N. Aydin**, «A database of linear codes over F₁₃ with minimum distance bounds and new quasi-twisted codes from a heuristic search algorithm», *Journal of Algebra Combinatorics Discrete Structures and Applications*, 2015.
    **Verificado:** título y revista. Ejemplo de cómo se construye una base de datos de códigos con búsquedas heurísticas (Módulo 26). Trata otro cuerpo (13 elementos), pero el método es el mismo.

## 4. Complejidad del cálculo de la distancia mínima

16. 🟢/🟡 **A. Vardy**, «The intractability of computing the minimum distance of a code», *IEEE Transactions on Information Theory*, 1997.
    **Verificado:** existencia y resultado (calcular la distancia mínima de un código lineal es un problema NP-difícil, como habían conjeturado Berlekamp, McEliece y van Tilborg en 1978), por las citas de otros artículos. 🟡 Volumen y páginas no confirmados (de memoria: vol. 43, n.º 6, pp. 1757–1766). Capítulo 19.8.
17. 🟢 **I. Dumer, D. Micciancio y M. Sudan**, «Hardness of approximating the minimum distance of a linear code», *IEEE Transactions on Information Theory*, 49(1), 2003, pp. 22–37.
    **Verificado.** Extiende el resultado de Vardy: ni siquiera **aproximar** la distancia mínima es fácil (bajo hipótesis de complejidad). Capítulo 19.8 (ampliación).

## 5. Programación y cálculo numérico

18. 🔴 **Documentación oficial de Python**: https://docs.python.org/3/ — en particular, el tutorial «Floating-Point Arithmetic: Issues and Limitations», https://docs.python.org/3/tutorial/floatingpoint.html
    El enlace no se pudo abrir desde el entorno de redacción; es la documentación oficial y debería estar disponible. Módulos 6–9.
19. 🟡 **D. Goldberg**, «What Every Computer Scientist Should Know About Floating-Point Arithmetic», *ACM Computing Surveys*, 23(1), 1991, pp. 5–48.
    Por qué los `float` no son exactos. Capítulos 1.1 y 8.7 (lectura avanzada).
20. 🟡 **T. H. Cormen, C. E. Leiserson, R. L. Rivest y C. Stein**, *Introduction to Algorithms*, MIT Press (4.ª ed., 2022).
    Referencia de algoritmos y complejidad. Módulo 8 (ampliación).

## 6. Software de álgebra que se usará para verificación independiente (Módulo 28)

21. 🟡 **SageMath** (software libre de matemáticas), https://www.sagemath.org — incluye funciones de teoría de códigos y una consulta a las tablas de codetables.de (ver n.º 13).
22. 🟡 **Magma** (sistema comercial de álgebra computacional, Universidad de Sídney). Es el programa que se usa habitualmente para calcular las tablas de mejores códigos conocidos. Referencia: W. Bosma, J. Cannon y C. Playoust, «The Magma algebra system I: The user language», *Journal of Symbolic Computation*, 24, 1997.

## 7. Currículo escolar

23. 🟡 **Real Decreto 217/2022, de 29 de marzo**, por el que se establece la ordenación y las enseñanzas mínimas de la Educación Secundaria Obligatoria (BOE). Marco de los saberes básicos de Matemáticas de ESO. La concreción para Andalucía la establece la normativa autonómica correspondiente (no consultada en esta sesión).

---

## Fuentes por capítulo

| Capítulo | Fuentes |
|---|---|
| 1.1 | Hardy y Wright (8); Goldberg (19); documentación de Python (18); Real Decreto 217/2022 (23). Todos los cálculos: verificados con `codigo/verificaciones/verificar_cap_1_1.py`. |

## Registro de verificaciones de fuentes

| Fecha | Fuente | Método | Resultado |
|---|---|---|---|
| 12/10/2026 | codetables.de (13) | Búsqueda web + intento de acceso directo | Existencia y mantenimiento confirmados por fuentes secundarias; acceso directo fallido (DNS). |
| 12/10/2026 | Artículo GF(7) cuasitwisted (14) | Búsqueda web | Revista, volumen, páginas, DOI y resumen confirmados; autores no confirmados. |
| 12/10/2026 | Chen y Aydin, F₁₃ (15) | Búsqueda web | Título y revista confirmados. |
| 12/10/2026 | Vardy 1997 (16) | Búsqueda web | Existencia y resultado confirmados; volumen y páginas no. |
| 12/10/2026 | Dumer–Micciancio–Sudan (17) | Búsqueda web | Confirmado. |
| 12/10/2026 | docs.python.org (18) | Acceso directo | Fallido (DNS) desde el entorno de redacción. |
