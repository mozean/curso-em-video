# Calculadora de descontos ou aumentos do salário.

s = 'DO SALÁRIO'
#DEFINIÇÃO DE UMA FUNÇÃO
def esp(): 
  print()

esp()
print(f'<<< CALCULADORA {s} >>>')

esp()

print('<<< O QUE DESEJAS CALCULAR? >>>')
print ('DESCONTO, digite 1')
print ('AUMENTO, digite 2')

opcao = int(input('Insira a opção desejada: '))
print()

if opcao == 1:
  print('CALCULAR DESCONTO '+s)
  print() 
  valor = float(input('Insira seu salário: R$ '))
  print()
  taxa = float(input('Taxa do desconto em %: '))
  print()
  desconto = valor*taxa/100
  preco_final = valor - desconto
  print(f'R$ {valor:.2f} com desconto de {taxa}% é igual a R$ {preco_final:.2f}.')
  print(f'Você terá uma diminuição de R$ {desconto:.2f} em seu salário.')

elif opcao == 2:
    print('CALCULAR AUMENTO '+s)
    print()
    valor = float(input('Insira o valor R$ '))
    print()
    taxa = float(input('Taxa do aumento em %: ')) 
    aumento = valor*taxa/100
    preco_final = valor + aumento
    print()
    print(f'R$ {valor:.2f} com aumento de {taxa}% é igual a R$ {preco_final:.2f}.')
    print(f'Você terá um aumento de R$ {aumento:.2f} em seu salário.')