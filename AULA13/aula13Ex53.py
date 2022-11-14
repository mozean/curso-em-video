# Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

'''APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''

print('\033[1;31m <><><> FRASES PALÍNDROMAS <><><>\033[m')

frase = str(input('Digite uma palavra ou uma frase: ')).upper().strip()
dividido = frase.split()

junto = ''.join(dividido)
invertido = junto[::-1]

print(f'O inverso de {frase} é {invertido}')

if junto == invertido:
  print('Temos um PALÍNDROMO!')
else:
  print('Não temos um PALÍNDROMO!')