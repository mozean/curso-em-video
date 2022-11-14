#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

print('<><><> VERIFICADOR DE PARIDADE <><><>')
numero = float(input('Insira um número inteiro: '))
resto = numero%2

if resto == 0:
  print(f'O NÚMERO {numero} É PAR!')
else:
  print(f'O NÚMERO {numero} É IMPAR!')