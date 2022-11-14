# Faça um programa que leia um número inteiro e mostre sua tabuada.
print()
print('<<<<<< TABUADA 1ª FORMA >>>>>>')
print()
numero = int(input('Insira um valor: '))
print()

intervalo = [1,2,3,4,5,6,7,8,9,10]

print(f'TABUADA DO NÚMERO {numero}:')
for multiplicador in intervalo:
  tabuada = numero*multiplicador
  print(f'{numero}*{multiplicador} = {tabuada}')

print()
#SEGUNDA FORMA
print('<<<<<< TABUADA 2ª FORMA >>>>>>')
print()

print(f'TABUADA DO NÚMERO {numero}:')

for mult in range(1,11):
  tabu = numero*mult
  print(f'{numero}*{mult} = {tabu}')

# MOZEAN RODRIGUES