# MOSTRE A PARTE INTEIRA
import math

print(10*'<>','MOSTRE A PARTE INTEIRA',10*'<>')
print()
numero = float(input('Insira um número: '))
print()
inteiro = math.sqrt(numero)

print(f'A parte ineteira de {inteiro} é {math.trunc(inteiro)}')