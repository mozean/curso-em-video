numero = input('Digite algo: ')
alnum = numero.isalnum()
tipo = type(numero)

print('O tipo primitivo desse valor é {}'.format(tipo))

if alnum == True:
  print('Valor alfanumérico!')
else:
  print('Não é um valor alfanumérico')

alpha = numero.isalpha()

if alpha == True:
  print('É uma letra!')

else:
  print('Não é uma letra!')

num = numero.isnumeric
if num == True:
  print('É um número!')

else:
  print('Não é um número!')