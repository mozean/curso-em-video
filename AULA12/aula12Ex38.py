'''
Exercício Python 038: Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

print('\033[1;45;35m<><><><><> COMPARAÇÃO DE DOIS NÚMEROS <><><><><>\033[m')
# Pergunte o valor da casa.
numero1 = int(input('Insira o 1º valor: '))

numero2 = int(input('Insira o 2º valor: '))

if numero1 > numero2:
  print(f'O primeiro valor é maior')
elif numero1 < numero2:
  print(f'O segundo valor é maior')

else:
  print('Não existe valor maior, os dois são iguais.')