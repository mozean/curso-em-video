'''
Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
'''

print('\033[1;45;35m<><><><><> MÉDIA FINAL <><><><><>\033[m')
# Pergunte o valor da casa.
ap1 = int(input('Insira a nota da Avaliação 1: '))

ap2 = int(input('Insira a nota da Avaliação 2: '))

media = (ap1 + ap2)/2

if media < 5:
  print(f'Sua média é {media} e você está REPROVADO!!!')
elif media < 7:
  print(f'Sua média é {media} e voce está de RECUPERAÇÃO!!!')

elif 9 < media <= 10:
  print(f'Sua média é {media} e você está APROVADO!!! Parabéns!')
  print('O miserável é um GÊNIO!!!')

else:
  print(f'Sua média é {media} e você está APROVADO!!! Parabéns!')