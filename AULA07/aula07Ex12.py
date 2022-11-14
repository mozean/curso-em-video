# Calculadora de descontos ou aumentos.

print() #espaço
print('<<< CALCULADORA DE AUMENTOS OU DESCONTOS >>>')
print() #espaço

print('<<< O QUE DESEJAS CALCULAR? >>>')
print ('DESCONTO, digite 1')
print ('AUMENTO, digite 2')

opcao = int(input('Insira a opção desejada: '))
print()

if opcao == 1:
  print('CALCULAR DESCONTO')
  print()
  valor = float(input('Insira o valor R$ '))
  print()
  taxa = float(input('Taxa do desconto em %: '))
  print()
  desconto = valor*taxa/100
  preco_final = valor - desconto
  print(f'R$ {valor:.2f} com desconto de {taxa}% é igual a R$ {preco_final:.2f}.')
  print(f'Você economizará R$ {desconto:.2f}')

elif opcao == 2:
    print('CALCULAR AUMENTO')
    print()
    valor = float(input('Insira o valor R$ '))
    print()
    taxa = float(input('Taxa do aumento em %: ')) 
    aumento = valor*taxa/100
    preco_final = valor + aumento
    print()
    print(f'R$ {valor:.2f} com aumento de {taxa}% é igual a R$ {preco_final:.2f}.')
    print(f'Você pagará R$ {aumento:.2f} a mais.')