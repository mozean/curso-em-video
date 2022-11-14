#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

print('\033[1;45;35m<><><><><> CONVERSOR DE BASE NUMÉRICA <><><><><>\033[m')
# Pergunte o valor da casa.
numero = int(input('Insira um valor: '))

print('''Escolha a base de conversão: 
Opção 1: Base Binária
Opção 2: Base Octal
Opção 3: Base Hexadecimal''')

opcao = int(input('Insira opção desejada: '))

# BASE BINÁRIA

if opcao == 1:
  print(f'O número {numero} em base binária vale: {bin(numero)[2:]}')
  
elif opcao == 2:
  print(f'O número {numero} em base octal vale: {oct(numero)[2:]}')

elif opcao == 3:
  print(f'O número {numero} em base hexadecimal vale: {hex(numero)[2:]}')

else:
  print('Opção Inválida. Tente novamente!')