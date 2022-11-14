'''
Exercício Python 045: Crie um programa que faça o computador jogar Jokenpô com você.
'''

import random
import time

print('\033[1;41;35m<><><><><> JO KEN PO <><><><><>\033[m')

print('''
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 3 ] TESOURA
''')

jogador = int(input('Qual a sua jogada? '))

opcao = ['PEDRA','PAPEL','TESOURA']

pc = random.choice(opcao)

comp = opcao.index(pc)

print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.8)
print('PO!!!')

print(15*'~')

if jogador == comp:
  print(f'Computador jogou {pc}.')
  print(f'Você jogou {opcao[jogador]}')
  print(15*'~')
  print('EMPATE')

elif jogador == 0 and comp ==2:
  print(f'Computador jogou {pc}.')
  print(f'Você jogou {opcao[jogador]}')
  print(10*'~')
  print('Você Venceu!')

elif jogador == 1 and comp ==0:
  print(f'Computador jogou {pc}.')
  print(f'Você jogou {opcao[jogador]}')
  print(10*'~')
  print('Você Venceu!')

elif jogador == 2 and comp ==1:
  print(f'Computador jogou {pc}.')
  print(f'Você jogou {opcao[jogador]}')
  print(10*'~')
  print('Você Venceu!')

else:
  print(f'Computador jogou {pc}.')
  print(f'Você jogou {opcao[jogador]}')
  print(10*'~')
  print('''Computador Venceu!
Perdeu, Otário.''')