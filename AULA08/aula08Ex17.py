# CALCULE A HIPOTENUSA
import math

print(10*'<>','CÁLCULO DA HIPOTENUSA',10*'<>')
print()
cat1 = float(input('Insira o 1º cateto: '))
cat2 = float (input('Insira o 2º cateto: '))
hip = math.sqrt(cat1**2+cat2**2)
print()

print(f'A Hipotenusa de um triâgulo retângulo cujos catetos valem {cat1} e {cat2} é {hip:.2f}')