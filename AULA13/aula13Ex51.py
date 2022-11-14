# Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('10 TERMOS DE UMA PA')

a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for posicao in range(1,11):
  an = a1 + (posicao-1)*r
  print(an, end = ' -> ' )

print('FIM!')