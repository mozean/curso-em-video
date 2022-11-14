'''
Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''
import datetime

print('\033[1;41;32m<><><><><> ALISTAMENTO MILITAR <><><><><>\033[m')
# Pergunte o valor da casa.
ano = int(input('Qual seu ano de nascimento? '))
atual = datetime.date.today().year
idade = atual - ano
faltam = 18 - idade
passou = idade - 18

if idade < 18:
  print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
  print(f'Ainda faltam {faltam} anos para o alistamento.')
  print(f'Seu alistamento será em {atual + faltam}.')

elif idade == 18:
  print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
  print('Você tem que se alistar IMEDIATAMENTE!')

else:
  print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')
  print(f'Você já deveria ter se alistado há {passou} anos.')
  print(f'Seu alistamento foi em {atual - passou}.')