#  Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

print('<><><> COMPARAÇÃO DE VALORES <><><>')

n1 = float(input('Insira um valor: '))
n2 = float(input('Insira um valor: '))
n3 = float(input('Insira um valor: '))


# MAIOR
if n1 > n2 and n1>n3:
  print(f'{n1} é o maior valor.')

if n2>n1 and n2>n3:
  print(f'{n2} é o maior valor ')

if n3>n2 and n3>n1:
  print(f'{n3} é o maior valor')

# INTERMEDIARIO

if n2>n1>n3 or n3>n1>n2:
  print(f'{n1} é o valor intermediário.')

if n1>n2>n3 or n3>n2>n1:
  print(f'{n2} é o valor intermediário.')

if n2>n3>n1 or n1>n3>n2:
  print(f'{n3} é o valor intermdiário.')


# MENOR

if n1 < n2 and n1 < n3:
  print(f'{n1} é o menor valor.')

if n2<n1 and n2<n3:
  print(f'{n2} é o menor valor.')

if n3<n2 and n3<n1:
  print(f'{n3} é o menor valor.')
