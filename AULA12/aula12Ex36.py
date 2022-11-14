# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
print('\033[1;45;35m<><><><><> SIMULAÇÃO DE EMPRÉSTIMO <><><><><>\033[m')
# Pergunte o valor da casa.
valor = float(input('Valor da Casa: R$ '))

# o salário do comprador
salario = float(input('Qual o seu salário?: R$ '))

# em quantos anos ele vai pagar
anos = int(input('Em quantos anos pretendes pagar?: R$ '))

# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

prestacao = valor/(anos*12)

if prestacao > 0.3*salario:
  print(f'\033[31mInfelizmente seu empréstimo de R$ {valor:.2f} para a compra da casa em {anos} anos com parcelas de R$ {prestacao:.2f} não foi aprovado!\033[m')
else:
  print(f'\033[32mParabéns! Seu empréstimo de R$ {valor:.2f} para a compra da casa em {anos} anos com parcelas de R$ {prestacao:.2f}\033[m')