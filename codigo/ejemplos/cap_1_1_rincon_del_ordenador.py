# Rincón del ordenador — Capítulo 1.1
# Objetivo: ver con tus propios ojos que los decimales del ordenador (float)
# no son exactos, que las fracciones exactas sí lo son, y probar la
# "suma y el producto con reloj de 7".

print(0.1 + 0.2)              # suma con decimales "de ordenador" (float)
print(0.1 + 0.2 == 0.3)       # ¿es exactamente igual a 0.3?

from fractions import Fraction
print(Fraction(1, 10) + Fraction(2, 10))               # suma EXACTA de fracciones
print(Fraction(1, 10) + Fraction(2, 10) == Fraction(3, 10))

print((4 + 5) % 7)            # suma "con reloj de 7": resto de dividir 9 entre 7
print((3 * 5) % 7)            # producto "con reloj de 7": resto de dividir 15 entre 7
