#Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

print(10*'-', 'TABUADA COM FOR', 10*'-')

numero = int(input('Digite um valor inteiro: '))

for mult in range(1,11):
  print(f'{numero} * {mult:02} = ',end='')
  print(numero*mult)