'''
Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

print('\033[1;41;35m<><><><><> CONDIÇÕES DE PAGAMENTOS <><><><><>\033[m')

preco = float(input('Preço das Compras: R$ '))

print('''
[ 1 ] à vista dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] em até 2x no cartão
[ 4 ] 3x ou mais no cartão
''')

opcao = int(input('Qual a forma de pagamento? '))

if opcao == 1:
  avista = preco * 0.9
  print(f'Sua compra de R$ {preco} vai curstar R$ {avista} no final.')

elif opcao == 2:
  avista_cartao = preco * 0.95
  print(f'Sua compra de R$ {preco} vai curstar R$ {avista_cartao} no final.')
  
elif opcao == 3:
  parcela = int(input('Em quantas vezes? '))
  valor_parcela = preco/parcela
  print(f'Sua compra será parcelada em {parcela}x de R$ {valor_parcela:.2f} SEM JUROS. Ao final, sua compra de R$ {preco:.2f} vai custar R$ {parcela*valor_parcela:.2f}')

elif opcao == 4:
  parcela = int(input('Em quantas vezes? '))
  valor_parcela = (preco/parcela)*1.2
  print(f'Sua compra será parcelada em {parcela}x de R$ {valor_parcela:.2f} SEM JUROS. Ao final, sua compra de R$ {preco:.2f} vai custar R$ {parcela*valor_parcela:.2f}.')