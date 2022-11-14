# Faça um programa que leia números de 1 a 9999 e mostre na tela cada um dos dígitos separados.

print('Ordens de um Número')
numero = int(input('Digite um número: '))
print('Ordens do Número: ',numero)

numero = f'{numero:04}'
numero = str(numero)

# UNIDADES
print(f'UNIDADE: {numero[3]}')
# DEZENAS
print(f'DEZENA: {numero[2]}')

#CENTENAS
print(f'CENTENA: {numero[1]}')
#MILHARES
print(f'MILHAR: {numero[0]}')