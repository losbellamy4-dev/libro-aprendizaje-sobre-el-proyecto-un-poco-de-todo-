#!/usr/bin/env python3
"""
verificar_cap_1_1.py — Comprobación independiente de los cálculos del
Capítulo 1.1 («Los conjuntos de números: N, Z, Q y R»).

¿PARA QUÉ SIRVE?
    Todos los resultados numéricos del capítulo se han calculado a mano.
    Este programa los vuelve a calcular por un procedimiento distinto
    (el ordenador, con aritmética EXACTA de fracciones) para detectar
    posibles errores. Es la misma filosofía que usarás en tu investigación:
    un resultado importante se comprueba siempre por un segundo camino.

¿CÓMO SE USA?
    python3 verificar_cap_1_1.py

    Si todo es correcto, cada bloque imprime «OK» y al final aparece
    «TODAS LAS COMPROBACIONES SUPERADAS». Si algo no coincide, el programa
    se detiene con un AssertionError que dice qué cálculo ha fallado.

REQUISITOS
    Solo la biblioteca estándar de Python 3 (no hay que instalar nada).

NOTA PARA EL ESTUDIANTE
    Todavía no necesitas entender este código. Podrás leerlo línea a línea
    cuando termines los Módulos 6 y 7. Por ahora basta con ejecutarlo y ver
    que todas las comprobaciones salen «OK».
"""

from fractions import Fraction as F
from math import isqrt


# ---------------------------------------------------------------------------
# 1. HERRAMIENTAS
# ---------------------------------------------------------------------------

def desarrollo(fraccion, base=10):
    """Desarrollo de una fracción en la base indicada mediante la DIVISIÓN
    LARGA, exactamente como se hace a mano.

    Devuelve (signo, parte_entera, anteperiodo, periodo), donde anteperiodo
    y periodo son cadenas de cifras ('' si no hay).

    Idea clave (Propiedad 1.4 del capítulo): al dividir entre b solo hay b
    restos posibles (0, 1, ..., b-1). En cuanto un resto se repite, las
    cifras empiezan a repetirse: ahí empieza el periodo.
    """
    a, b = fraccion.numerator, fraccion.denominator   # Fraction garantiza b > 0
    signo = "-" if a < 0 else ""
    a = abs(a)
    parte_entera, resto = divmod(a, b)
    cifras = []
    posicion_del_resto = {}           # resto -> posición de la cifra que genera
    while resto != 0 and resto not in posicion_del_resto:
        posicion_del_resto[resto] = len(cifras)
        cifra, resto = divmod(resto * base, b)
        cifras.append(str(cifra))
    if resto == 0:                    # la división termina: decimal exacto
        return signo, parte_entera, "".join(cifras), ""
    inicio = posicion_del_resto[resto]
    return signo, parte_entera, "".join(cifras[:inicio]), "".join(cifras[inicio:])


def restos_division_larga(a, b):
    """Lista de restos que aparecen al dividir a entre b (0 < a < b), empezando
    por el propio a, hasta que un resto se repite o sale 0."""
    restos = []
    r = a
    while r != 0 and r not in restos:
        restos.append(r)
        r = (r * 10) % b
    return restos


def a_texto(fraccion):
    """Escribe el decimal con coma española y el periodo entre paréntesis.
    Ejemplos: 0,41(6)   2,(18)   0,175   -3"""
    signo, entera, ante, per = desarrollo(fraccion)
    if not ante and not per:
        return f"{signo}{entera}"
    texto = f"{signo}{entera}," + ante
    if per:
        texto += f"({per})"
    return texto


def tipo(fraccion):
    """'entero', 'exacto', 'periódico puro' o 'periódico mixto'."""
    _, _, ante, per = desarrollo(fraccion)
    if not per:
        return "exacto" if ante else "entero"
    return "periódico mixto" if ante else "periódico puro"


def tipo_predicho(fraccion):
    """Predicción SIN dividir, usando solo el denominador de la fracción
    irreducible (Propiedad 1.5). Es un procedimiento distinto de tipo()."""
    b = fraccion.denominator          # Fraction ya está simplificada
    if b == 1:
        return "entero"
    resto_b = b
    tiene_2_o_5 = False
    for p in (2, 5):
        while resto_b % p == 0:
            resto_b //= p
            tiene_2_o_5 = True
    if resto_b == 1:
        return "exacto"
    return "periódico mixto" if tiene_2_o_5 else "periódico puro"


def generatriz(parte_entera, anteperiodo, periodo):
    """Fracción generatriz de  parte_entera,anteperiodo(periodo)  (número >= 0).

    Regla general (se deduce en el capítulo restando 10^k·x - 10^j·x):
        x = E + (AP - A) / (10^len(A) · (10^len(P) - 1))
    donde AP es el número formado por anteperiodo y periodo seguidos.
    Es un procedimiento INDEPENDIENTE de la división larga de desarrollo().
    """
    E = F(parte_entera)
    A = int(anteperiodo) if anteperiodo else 0
    if not periodo:                                   # decimal exacto
        return E + F(A, 10 ** len(anteperiodo))
    AP = int(anteperiodo + periodo)
    return E + F(AP - A, 10 ** len(anteperiodo) * (10 ** len(periodo) - 1))


def es_cuadrado_perfecto(n):
    return n >= 0 and isqrt(n) ** 2 == n


def ok(mensaje):
    print(f"OK  {mensaje}")


# ---------------------------------------------------------------------------
# 2. COMPROBACIONES DEL CAPÍTULO
# ---------------------------------------------------------------------------

def comprobar_ejemplo_1_1():
    # Números de la lista que son racionales (se representan como fracciones exactas)
    assert F(-12, 4) == -3
    assert F(75, 100) == F(3, 4)
    assert generatriz(0, "", "6") == F(2, 3)
    assert isqrt(9) == 3 and es_cuadrado_perfecto(9)
    assert not es_cuadrado_perfecto(5)          # sqrt(5) irracional (Prop. 1.7)
    assert isqrt(16) == 4
    assert F(2, 5) == F(4, 10)                  # 2/5 = 0,4: racional no entero
    ok("Ejemplo 1.1 (clasificación)")


def comprobar_ejemplo_1_2():
    casos = {F(7, 40): ("0,175", "exacto"),
             F(5, 12): ("0,41(6)", "periódico mixto"),
             F(3, 7): ("0,(428571)", "periódico puro")}
    for fr, (texto, t) in casos.items():
        assert a_texto(fr) == texto, (fr, a_texto(fr))
        assert tipo(fr) == t == tipo_predicho(fr), fr
    # Restos de la división 3 : 7 (aparecen todos los restos no nulos 1..6)
    assert restos_division_larga(3, 7) == [3, 2, 6, 4, 5, 1]
    # Fracciones generatrices calculadas a mano
    assert generatriz(0, "41", "6") == F(375, 900) == F(5, 12)
    assert generatriz(0, "175", "") == F(7, 40)
    assert generatriz(0, "", "428571") == F(3, 7)
    assert F(7, 40) == F(175, 1000)            # 40·25 = 1000
    ok("Ejemplo 1.2 (fracción <-> decimal)")


def comprobar_ejemplo_1_3():
    # Coma flotante: el ordenador NO es exacto con 0,1 y 0,2
    assert 0.1 + 0.2 != 0.3
    assert repr(0.1 + 0.2) == "0.30000000000000004"
    assert F(1, 10) + F(2, 10) == F(3, 10)       # con fracciones exactas sí
    # Sumar 0.1 diez veces, una a una, con un bucle:
    total = 0.0
    for _ in range(10):
        total += 0.1
    assert total != 1.0 and repr(total) == "0.9999999999999999"
    # ¡Ojo con las versiones! Desde Python 3.12, la función sum() usa una suma
    # "compensada" más precisa y en este caso concreto devuelve 1.0.
    # (Comprobado al redactar el libro con Python 3.13.)
    import sys
    if sys.version_info >= (3, 12):
        assert sum([0.1] * 10) == 1.0
    # 1/10 en base 2 es periódico: 0,0(0011)
    assert desarrollo(F(1, 10), base=2) == ("", 0, "0", "0011")
    # Tablas "con reloj de 7" y "con reloj de 6"
    assert (4 + 5) % 7 == 2 and (6 + 6) % 7 == 5 and (3 * 5) % 7 == 1
    tabla7 = [[(a * b) % 7 for b in range(7)] for a in range(7)]
    assert tabla7[2] == [0, 2, 4, 6, 1, 3, 5]
    assert tabla7[3] == [0, 3, 6, 2, 5, 1, 4]
    assert tabla7[4] == [0, 4, 1, 5, 2, 6, 3]
    assert tabla7[5] == [0, 5, 3, 1, 6, 4, 2]
    assert tabla7[6] == [0, 6, 5, 4, 3, 2, 1]
    for a in range(1, 7):                        # cada fila no nula es una
        assert sorted(tabla7[a][1:]) == [1, 2, 3, 4, 5, 6]   # reordenación de 1..6
    inversos7 = {a: b for a in range(1, 7) for b in range(1, 7) if a * b % 7 == 1}
    assert inversos7 == {1: 1, 2: 4, 3: 5, 4: 2, 5: 3, 6: 6}
    tabla6 = [[(a * b) % 6 for b in range(6)] for a in range(6)]
    assert tabla6[2] == [0, 2, 4, 0, 2, 4]
    assert tabla6[3] == [0, 3, 0, 3, 0, 3]
    assert (2 * 3) % 6 == 0
    ok("Ejemplo 1.3 (exactitud, tablas módulo 7 y módulo 6)")


def comprobar_ejercicios_nivel_A():
    # A1
    assert F(15, 3) == 5 and F(125, 1000) == F(1, 8)
    assert generatriz(0, "", "12") == F(4, 33)
    assert es_cuadrado_perfecto(25) and not es_cuadrado_perfecto(10)
    assert F(-6, 3) == -2                        # -sqrt(36)/3
    assert F(3141592, 1000000) == F(392699, 125000)
    # A3
    esperado = {F(3, 8): "0,375", F(7, 9): "0,(7)", F(13, 6): "2,1(6)",
                F(9, 25): "0,36", F(4, 11): "0,(36)"}
    for fr, texto in esperado.items():
        assert a_texto(fr) == texto, (fr, a_texto(fr))
        assert tipo(fr) == tipo_predicho(fr)
    # A4
    assert generatriz(0, "45", "") == F(9, 20)
    assert generatriz(0, "", "5") == F(5, 9)
    assert generatriz(2, "", "18") == F(24, 11)
    assert generatriz(0, "3", "12") == F(309, 990) == F(103, 330)
    assert generatriz(1, "0", "6") == F(96, 90) == F(16, 15)
    for fr, texto in {F(9, 20): "0,45", F(5, 9): "0,(5)", F(24, 11): "2,(18)",
                      F(103, 330): "0,3(12)", F(16, 15): "1,0(6)"}.items():
        assert a_texto(fr) == texto, (fr, a_texto(fr))
    # A5: -2,5 < -sqrt(4) < -3/2 < 0,(3) < 1,7 < 7/4
    lista = [F(-25, 10), F(-2), F(-3, 2), F(1, 3), F(17, 10), F(7, 4)]
    assert lista == sorted(lista)
    # A6 (contraejemplos)
    assert 2 - 5 < 0 and F(1, 2).denominator != 1
    ok("Ejercicios de nivel A")


def comprobar_ejercicios_nivel_B():
    # B1
    m = (F(3, 7) + F(4, 9)) / 2
    assert m == F(55, 126) and F(3, 7) < m < F(4, 9)
    assert F(3, 7) == F(216, 504) and F(4, 9) == F(224, 504)
    assert F(218, 504) == F(109, 252) and F(219, 504) == F(73, 168)
    for k in (217, 218, 219):
        assert F(3, 7) < F(k, 504) < F(4, 9)
    # B2
    assert F(21, 56) == F(3, 8) and F(33, 120) == F(11, 40)
    assert F(6, 15) == F(2, 5) and F(35, 42) == F(5, 6)
    for fr, t in {F(21, 56): "exacto", F(33, 120): "exacto", F(9, 14): "periódico mixto",
                  F(6, 15): "exacto", F(35, 42): "periódico mixto"}.items():
        assert tipo(fr) == tipo_predicho(fr) == t, fr
    assert a_texto(F(9, 14)) == "0,6(428571)" and a_texto(F(5, 6)) == "0,8(3)"
    # B3: 0,(9) = 1 ; 0,4(9) = 1/2 ; 2,(9) = 3
    assert generatriz(0, "", "9") == 1
    assert generatriz(0, "4", "9") == F(1, 2)
    assert generatriz(2, "", "9") == 3
    # La división larga nunca produce periodo 9 (comprobado para b <= 300)
    for b in range(2, 301):
        for a in range(1, b):
            periodo = desarrollo(F(a, b))[3]
            assert set(periodo) != {"9"}, (a, b)
    # B4: 1/13 = 0,(076923); restos 1, 10, 9, 12, 3, 4
    assert a_texto(F(1, 13)) == "0,(076923)"
    assert restos_division_larga(1, 13) == [1, 10, 9, 12, 3, 4]
    # B6
    assert F(5, 3).denominator == 3 and F(-3, 2) == F(-15, 10)
    ok("Ejercicios de nivel B")


def comprobar_ejercicios_nivel_C():
    # C1: longitud del periodo de 1/p
    periodos = {}
    for p in (3, 7, 11, 13, 17, 19, 23):
        periodos[p] = len(desarrollo(F(1, p))[3])
        assert (p - 1) % periodos[p] == 0       # el periodo divide a p - 1
    assert periodos == {3: 1, 7: 6, 11: 2, 13: 6, 17: 16, 19: 18, 23: 22}
    assert a_texto(F(1, 17)) == "0,(0588235294117647)"
    assert a_texto(F(1, 19)) == "0,(052631578947368421)"
    assert a_texto(F(1, 23)) == "0,(0434782608695652173913)"
    # C2: ¿para qué n todo número no nulo tiene "pareja" b con a·b ≡ 1 (mod n)?
    def todos_tienen_pareja(n):
        return all(any(a * b % n == 1 for b in range(1, n)) for a in range(1, n))
    resultado = {n: todos_tienen_pareja(n) for n in range(2, 12)}
    assert [n for n, v in resultado.items() if v] == [2, 3, 5, 7, 11]
    sin_pareja = {n: [a for a in range(1, n)
                      if not any(a * b % n == 1 for b in range(1, n))]
                  for n in (4, 6, 8, 9, 10)}
    assert sin_pareja == {4: [2], 6: [2, 3, 4], 8: [2, 4, 6], 9: [3, 6],
                          10: [2, 4, 5, 6, 8]}
    parejas11 = {a: b for a in range(1, 11) for b in range(1, 11) if a * b % 11 == 1}
    assert parejas11 == {1: 1, 2: 6, 3: 4, 4: 3, 5: 9, 6: 2, 7: 8, 8: 7, 9: 5, 10: 10}
    parejas5 = {a: b for a in range(1, 5) for b in range(1, 5) if a * b % 5 == 1}
    assert parejas5 == {1: 1, 2: 3, 3: 2, 4: 4}
    ok("Ejercicios de nivel C")


def comprobar_problemas():
    # Problema de aplicación 1
    assert 5 - (-3) == 8 and -2 - 4 == -6
    assert F(45, 10) / F(75, 100) == 6
    assert F(-45, 10) + 8 * F(75, 100) == F(3, 2)
    # Problema de aplicación 2 (céntimos)
    assert 235 + 99 + 1210 + 56 == 1600
    assert F(235, 100) + F(99, 100) + F(1210, 100) + F(56, 100) == 16
    # Problema combinado (calendario). 0 = lunes, 1 = martes, ...
    dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
    assert divmod(23, 7) == (3, 2) and dias[(0 + 23) % 7] == "miércoles"
    assert divmod(100, 7) == (14, 2) and dias[(0 + 100) % 7] == "miércoles"
    assert dias[(0 - 10) % 7] == "viernes"       # Python da restos >= 0
    assert a_texto(F(100, 7)) == "14,(285714)" and a_texto(F(2, 7)) == "0,(285714)"
    ok("Problemas de aplicación y problema combinado")


def comprobar_prueba_de_dominio_y_refuerzo():
    # D1
    assert F(-7, 7) == -1 and F(7, 2) == F(isqrt(49), 2)
    assert not es_cuadrado_perfecto(3)
    # D2
    assert generatriz(0, "2", "7") == F(25, 90) == F(5, 18)
    assert a_texto(F(5, 18)) == "0,2(7)"
    # D3
    for fr, t in {F(7, 20): "exacto", F(5, 6): "periódico mixto",
                  F(2, 9): "periódico puro", F(15, 48): "exacto"}.items():
        assert tipo(fr) == tipo_predicho(fr) == t, fr
    assert F(15, 48) == F(5, 16)
    # D5
    assert F(-1, 3) < F(-7, 24) < F(-1, 4)
    # D6: 0,6 < 0,(6) = 2/3 < 0,67
    assert generatriz(0, "", "6") == F(2, 3) and F(6, 10) < F(2, 3) < F(67, 100)
    # D10: el periodo de a/17 tiene como mucho 16 cifras
    assert max(len(desarrollo(F(a, 17))[3]) for a in range(1, 17)) == 16
    # Refuerzo RF1
    assert F(-20, 5) == -4 and es_cuadrado_perfecto(49) and not es_cuadrado_perfecto(50)
    assert F(5, 10) ** 2 == F(25, 100)
    assert generatriz(0, "0", "5") == F(1, 18)
    # RF2
    assert generatriz(0, "1", "6") == F(1, 6)
    assert generatriz(3, "", "7") == F(34, 9)
    assert generatriz(0, "", "142857") == F(1, 7)
    # RF3
    for fr, texto in {F(11, 16): "0,6875", F(7, 15): "0,4(6)", F(5, 33): "0,(15)"}.items():
        assert a_texto(fr) == texto and tipo(fr) == tipo_predicho(fr)
    # RF5: -0,(3) < -0,33 < -0,3 < -1/4
    lista = [F(-1, 3), F(-33, 100), F(-3, 10), F(-1, 4)]
    assert lista == sorted(lista)
    ok("Prueba de dominio y ejercicios de refuerzo")


def comprobar_propiedad_1_5_masivamente():
    """Resultado verificado por programa: la predicción por el denominador
    coincide con la división larga para TODAS las fracciones a/b con
    1 <= a < b <= 500 (evidencia computacional, no demostración)."""
    total = 0
    for b in range(2, 501):
        for a in range(1, b):
            fr = F(a, b)
            assert tipo(fr) == tipo_predicho(fr), fr
            total += 1
    ok(f"Propiedad 1.5 comprobada en {total} fracciones (evidencia, no demostración)")


def comprobar_raiz_de_2_sin_denominador_pequeno():
    """Ejercicio B5: ninguna fracción a/b con 1 <= b <= 1000 cumple (a/b)^2 = 2.
    Esto es EVIDENCIA, no una demostración (hay infinitos denominadores)."""
    for b in range(1, 1001):
        a = isqrt(2 * b * b)          # único candidato posible: a^2 cerca de 2b^2
        assert a * a != 2 * b * b
    ok("Ningún a/b con b <= 1000 tiene cuadrado 2 (evidencia del ejercicio B5)")


if __name__ == "__main__":
    comprobar_ejemplo_1_1()
    comprobar_ejemplo_1_2()
    comprobar_ejemplo_1_3()
    comprobar_ejercicios_nivel_A()
    comprobar_ejercicios_nivel_B()
    comprobar_ejercicios_nivel_C()
    comprobar_problemas()
    comprobar_prueba_de_dominio_y_refuerzo()
    comprobar_propiedad_1_5_masivamente()
    comprobar_raiz_de_2_sin_denominador_pequeno()
    print("\nTODAS LAS COMPROBACIONES SUPERADAS")
