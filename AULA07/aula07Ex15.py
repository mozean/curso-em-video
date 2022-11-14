# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

print(5*'X','Aluguel de Carros',5*'X')

print()

dias = int(input('Quantos dias de aluguel?: '))
distancia = float(input('Quantos Km rodados?: '))
v_dia = 60
v_km = .15

valor = dias*v_dia+distancia*v_km

print()

print(f'O valor do aluguel de um carro que ficou alugado por {dias} dias e rodou {distancia} Km é igual a R$ {valor:.2f}.')

# MOZEAN RODRIGUES
