#Exercício Python 50: Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

print('SOMA DE 6 PARES')
qtde = 0
sum = 0
for valor in range(1,7):
  par = int(input(f'Insira o {valor}º valor: '))
  if par%2==0:
    sum += par
    qtde += 1
print (f'A soma dos {qtde} números pares da lista é {sum}.')