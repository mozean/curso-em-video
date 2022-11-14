'''
Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.
'''

from time import sleep

print('\033[1;41;35m<><><> ANALISADOR E CALCULADOR DE NÚMEROS <><><>\033[m')

valor1 = float(input('Insira o 1º valor: '))
valor2 = float(input('Insira o 2º valor: '))

opcao = 0

while opcao != 5:
  
  print('''
\033[31mESCOLHA SUA OPÇÃO:\033[m
  [ 1 ] somar

  [ 2 ] multiplicar

  [ 3 ] maior

  [ 4 ] novos números

  [ 5 ] sair do programa
  ''')

  opcao = int(input('Insira a opção desejada: '))
  
  if opcao == 1:
    soma = valor1 + valor2
    print(f'\033[1;42mO resultado de {valor1} + {valor2} é {soma}\033[m')
  
  elif opcao == 2:
    mult = valor1 * valor2
    print(f'\033[1;42mO resultado de {valor1} × {valor2} é {mult}\033[m')  
  elif opcao == 3:
    if valor1 > valor2:
      print(f'\033[1;42mO valor {valor1} é maior que {valor2}.\033[m')
    elif valor1 < valor2:
      print(f'\033[1;42mO valor {valor2} é maior que {valor1}.\033[m')
    else:
      print(f'\033[1;42mAmbos os números possuem o mesmo valor.\033[m')

  elif opcao == 4:
    valor1 = float(input('Insira o 1º valor: '))
    valor2 = float(input('Insira o 2º valor: '))
    
  else:
    print('Opção inválida. Tente novamente.')

  print(15*'=-=')

print('Finalizando...')
sleep(3)

print('''
\033[1;46mObrigado por utilizar nosso programa!
Desenvolvido por Mozean Rodrigues.\033[m
''')