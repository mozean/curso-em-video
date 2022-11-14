'''
Exercício Python 042: Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

import datetime

print('\033[1;45;35m<><><><><> CLASSIFICAÇÃO DE TRIÂNGULOS <><><><><>\033[m')

lado1 = float(input('Insira o lado 1: '))
lado2 = float(input('Insira o lado 2: '))
lado3 = float(input('Insira o lado 3: '))

equi = lado1 == lado2 == lado3
iso = lado1 == lado2 or lado1 == lado3 or lado2 == lado3
esc = lado1 != lado2 != lado3

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1 and equi:
  print(f'O triângulo de lados {lado1}, {lado2} e {lado3} Existe e é EQUILÁTERO!')

elif lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1 and iso:
  print(f'O triângulo de lados {lado1}, {lado2} e {lado3} Existe e é ISÓSCELES!')

elif lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado2 + lado1 and esc:
  print(f'O triângulo de lados {lado1}, {lado2} e {lado3} Existe e é ESCALENO!')

else:
  print(f'O triângulo de lados {lado1}, {lado2} e {lado3} não existe!')