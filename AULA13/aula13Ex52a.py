# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

import time
t1 = time.time()

print('********** NÚMEROS PRIMOS **********')

num = int(input('Insira um valor: '))
num = num**num
soma = 0

for div in range(2,num):
  resto = num%div
  if resto != 0:
    ver = bool(resto)
    if ver == True:
      soma +=1

if soma == num - 2:
  print(f'O número {num} é um número Primo!')
else: 
  print(f'O número {num} não é um número Primo!')

tempoExec = time.time() - t1
print("Tempo de execução: {} segundos".format(tempoExec))