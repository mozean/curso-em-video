# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print('COMPARADOR DE PESOS')
massas = []

for massa in range(1,6):
  massa = float(input(f'Insira a massa da {massa}ª pessoa em Kg: '))
  massas.append(massa)

if massas[0] < massas[1] and massas[0]< massas[2] and massas[0] < massas[3] and massas[0] < massas[4]:
  print(f'{massas[0]} é o menor peso!')

elif massas[1]< massas[2] and massas[1] < massas[3] and massas[1] < massas[4]:
  print(f'{massas[1]} é o menor peso!')

elif massas[2] < massas[3] and massas[2] < massas[4]:
   print(f'{massas[2]} é o menor peso!')

elif massas[3] < massas[4]:
   print(f'{massas[3]} é o menor peso!')

else:
  print(f'{massas[4]} é o menor peso!')

if massas[0] > massas[1] and massas[0]> massas[2] and massas[0] > massas[3] and massas[0] > massas[4]:
  print(f'{massas[0]} é o maior peso!')

elif massas[1]> massas[2] and massas[1] > massas[3] and massas[1] > massas[4]:
  print(f'{massas[1]} é o maior peso!')

elif massas[2] > massas[3] and massas[2] > massas[4]:
   print(f'{massas[2]} é o maior peso!')

elif massas[3] > massas[4]:
   print(f'{massas[3]} é o maior peso!')

else:
  print('Todos os pesos são iguais.')