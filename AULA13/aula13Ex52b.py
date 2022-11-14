# Exercício Python 52: Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
import time
t1 = time.time() ## TEMPO DE PROCESSAMENTO

print('********** NÚMEROS PRIMOS **********')

num = int(input('Insira um valor: '))
num = num

soma = 0

for div in range(2,num):
  resto = num%div
  if resto == 0:
    soma +=1
    break
if soma == 0:
  print(f'{num} é um número Primo!')
else: 
  print(f'{num} não é um número Primo!')


# TEMPO DE PROCESSAMENTO
tempoExec = time.time() - t1
print("Tempo de execução: {} segundos".format(tempoExec))