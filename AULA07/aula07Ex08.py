# Transforme metros em Centímetros e vice versa.

print('CONVERSOR DE MEDIDAS')
print()

print('Para Inserir o valor em:')
print('Metros (m) , digite 1')
print('Centímetros (m), digite 2')
print('Milímetros (mm), digite 3')

print()

opcao = int(input('Digite a opção desejada: '))
print()

if opcao == 1:
  metro = float(input('Digite o valor em metros: '))
  centimetro = 100*metro
  milimetro = 1000*metro
  print()
  print(f'{metro} m é igual a {centimetro} cm ou {milimetro} mm')

elif opcao == 2:
  centimetro = float(input('Insira o valor em centímetros: '))
  metro = centimetro/100
  milimetro = 10*centimetro
  print()
  print(f'{centimetro} cm é igual a {metro} m ou {milimetro}')

elif opcao == 3:
  milimetro = float(input('Insira o valor em milímetros: '))
  metro = milimetro/1000
  centimetro = milimetro/10
  print()
  print(f'{milimetro} mm é igual a {metro} m ou {centimetro} cm')