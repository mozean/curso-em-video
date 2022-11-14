#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. -Para salários superiores a R$1.250,00, calcule um aumento de 10%. -Para os inferiores ou iguais, o aumento é de 15%.

print('<><><> EXISTÊNCIA DE UM TRIÂNGULO <><><>')

lado1 = float(input('Insira um valor: '))
lado2 = float(input('Insira um valor: '))
lado3 = float(input('Insira um valor: '))


if lado1 > lado2 + lado3 or lado2 > lado1 + lado3 or lado3 > lado1 + lado2:
  print(f'O triângulo de lados {lado1},{lado2} e {lado3} não existe!')
else:
  print(f'O triângulo de lados {lado1},{lado2} e {lado3} existe!')