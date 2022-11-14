# Escreva um programa que leia a velocidade de um carro. -Se ele ultrapassar 80Km/, mostre uma mensagem dizendo que ele foi multado. -A multa vai custar R$7,00 por cada Km acima do limite.

print('<><><> VERIFICADOR DE MULTAS <><><>')
velocidade = float(input('Insira a velocidade do veículo: '))

if velocidade < 80:
  print('ISSO AÍ. CONTINUE RESPEITANDO O LIMITE DE VELOCIDADE.')
else:
  excesso = velocidade - 80
  multa = excesso*7
  print(F'QUE PENINHA. VOCÊ ULTRAPASSOU O LIMITE MÁXIMO EM {excesso} km E PAGARÁ R$ {multa:.2f} DE MULTA!')