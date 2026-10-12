# Código del libro

Todos los programas usan **solo la biblioteca estándar de Python 3**. No hay que instalar nada más.

## Carpetas

| Carpeta | Contenido |
|---|---|
| `ejemplos/` | Programas cortos que aparecen dentro de los capítulos (sección «Rincón del ordenador» o ejemplos de código). |
| `verificaciones/` | Un programa por capítulo que **recalcula por un procedimiento independiente** todos los resultados numéricos del capítulo (ejemplos, ejercicios, soluciones, prueba de dominio). |

A partir del Módulo 13 aparecerá una carpeta con la **biblioteca del proyecto** (operaciones sobre GF(7), matrices, rango, distancia mínima) y sus pruebas unitarias.

## Cómo ejecutar

Desde la carpeta raíz del repositorio:

```
python3 codigo/ejemplos/cap_1_1_rincon_del_ordenador.py
python3 codigo/verificaciones/verificar_cap_1_1.py
```

Si un programa de verificación termina con `TODAS LAS COMPROBACIONES SUPERADAS`, los cálculos del capítulo coinciden con el segundo procedimiento. Si alguno falla, el programa se detiene e indica qué cálculo no coincide.

## Registro de ejecuciones

| Fecha | Programa | Versión de Python | Resultado |
|---|---|---|---|
| 12/10/2026 | `verificaciones/verificar_cap_1_1.py` | 3.13.16 | Todas las comprobaciones superadas |
| 12/10/2026 | `ejemplos/cap_1_1_rincon_del_ordenador.py` | 3.13.16 | Salida idéntica a la mostrada en el capítulo 1.1 |

## Limitaciones conocidas

- Algunas salidas con números decimales (`float`) pueden variar entre versiones de Python. Ejemplo documentado en el capítulo 1.1: `sum([0.1] * 10)` da `1.0` desde Python 3.12 y `0.9999999999999999` en versiones anteriores. Los programas de verificación tienen esto en cuenta.
- Los programas de verificación comprueban los **cálculos** del libro; no sustituyen a las demostraciones. Cuando una comprobación cubre solo un número finito de casos de una afirmación general, el libro lo etiqueta como **[VERIFICADO POR PROGRAMA]** (evidencia, no demostración).
