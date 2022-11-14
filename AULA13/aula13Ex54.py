# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

import datetime

print('QUEM É MAIOR OU MENOR DE IDADE?')

menor = 0
maior = 0

idades = []

for ano in range(1,8):
  ano = int(input(f'Ano de Nascimento da {ano}ª pessoa: '))
  idade = datetime.date.today().year - ano
  if idade < 18:
    menor += 1
  else:
    maior +=1

  idades.append(idade)

print(f'''Neste grupo de pessoas existem {menor} menores de idade e
{maior} maiores de idade.''')

for idade in idades:
  print(f'O {idades.index(idade)+1}º tem {idade} anos.')