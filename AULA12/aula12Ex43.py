'''
Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
'''

print('\033[1;41;35m<><><><><> ÍNDICE DE MASSA CORPORAL <><><><><>\033[m')

massa = float(input('Insira sua massa em Kg: '))
altura = float(input('Insira sua altura em metros: '))

imc = massa / pow(altura,2)

if imc < 18.5:
  print(f'Seu IMC é {imc:.2f} e você está Abaixo do Peso!')

elif imc < 25:
  print(f'Seu IMC é {imc:.2f} e você está no Peso Ideal!')

elif imc < 30:
  print(f'Seu IMC é {imc:.2f} e você está com Sobrepeso!')

elif imc < 40:
  print(f'Seu IMC é {imc:.2f} e você está com Obesidade!')

else:
  print(f'Seu IMC é {imc} e você está com Obesidade Mórbida!')