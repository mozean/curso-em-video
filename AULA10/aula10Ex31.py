# Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

print('<><><> VALOR DA VIAGEM <><><>')

distancia = float(input('Insira a distância em Km: '))
valor_1 = 0.5*distancia
valor_2 = 0.45*distancia

if distancia <= 200:
  print(f'PARA UMA VIAGEM DE {distancia} km VOCÊ PAGARÁ R$ {valor_1:.2f}!')
else:
  print(f'PARA UMA VIAGEM DE {distancia} VOCÊ PAGARÁ R$ {valor_2:.2f}')