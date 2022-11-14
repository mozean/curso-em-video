#Exercício Python 48: Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500.

print('Todos os números que são múltiplos de três 1< x <500.')
sum = 0
for mult in range(3,501,2):
  if mult%3 == 0:
    sum += mult

print(f'A soma de todos os números x que são múltiplos de três e 1< x <500 é {sum}.')