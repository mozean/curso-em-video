# Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.

sexo = str(input('Informe seu Sexo [M/F]: ')).strip().upper()

while sexo not in 'MF':
 sexo = str(input('Opção Inválida. Informe seu sexo corretamente: ')).strip().upper()

if sexo == 'M':
  print('Sexo Masculino registrado com sucesso.')
else:
  print('Sexo Feminino registrado com sucesso.')