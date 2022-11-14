# CONVERSOR DE DOLÁRES EM REAIS OU O CONTRÁRIO

print()
print('<<< CONVERSOR DE MOEDAS >>>')
print('Para converter:')
print('Dólares em Reais, digite 1.')
print('Reais em Dólares, digite 2.')
print()

opcao = int(input('Insira a opção desejada: '))

if opcao == 1:
  print('<<< DÓLAR (U$) em REAL (R$) >>>')
  dolar = float(input('Insira o valor em Dólares U$ '))
  real = dolar*5.29
  print(f'U$ {dolar} = R$ {real:.2f}')

elif opcao == 2:
  print('<<< REAL (R$) em DÓLAR (U$) >>>')
  real = float(input('Insira o valor em Real R$ '))
  dolar = real/5.29
  print(f'R$ {real} = U$ {dolar:.2f}')