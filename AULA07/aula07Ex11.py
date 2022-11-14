# Calcular a área de uma parede e quanto será necessário de tinta para pintá-la.
print()
print('<<< ÁREA E QTDE DE TINTA >>>')

print()

altura = float(input('Insira a altura em m: '))
largura = float(input('Insira a largura em m: '))
rendimento = float(input('Rendimento da tinta escolhida em m²/litro: '))

area = altura * largura
volume = area/rendimento

print()

print(f'--> A área da sua parede é de {area:.2f} m² e serão necessários {volume:.2f} litros da tinta de sua escolha. <--')
