# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usúario venceu ou perdeu.
import random
from time import sleep

print('\033[0;31m<><><> ADIVINHE O NÚMERO <><><>\033[m')
numero = int(input('\033[0;32mDigite um número entre 0 e 5: \033[m'))
correto = random.randint(0,5)

print('PROCESSANDO...') 
sleep(1)

print('PROCESSANDO...') 
sleep(1)

print('PROCESSANDO...') 
sleep(1)

if numero == correto:
  print('ACERTOU, MISERÁVEL. PARABÉNS!')
else:
  print(f'QUE PENINHA, VOCÊ ERROU! O NÚMERO CORRETO ERA {correto} TENTE NOVAMENTE.')