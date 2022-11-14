#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. -Para salários superiores a R$1.250,00, calcule um aumento de 10%. -Para os inferiores ou iguais, o aumento é de 15%.

print('<><><> AUMENTO DO SALÁRIO <><><>')

salario = float(input('Insira um valor: '))
aumento1 = salario*0.15
aumento2 = salario*0.1

if salario <= 1250:
  print(f'Seu salário terá um aumento de R$ {aumento1:.2f} e passará de R$ {salario:.2f} para R$ {(salario + aumento1):.2f}')

else:
  print(f'Seu salário terá um aumento de R$ {aumento2:.2f} e passará de R$ {salario:.2f} para R$ {(salario + aumento2):.2f}.')