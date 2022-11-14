# Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('<<<<< ADIVINHE O NÚMERO >>>>>')

print('''
Sou seu computador e pensei em um número de 1 a 10. Tente adivinhar que número é esse.
''')

pc = randint(1,10)

jogador = int(input('Digite seu palpite: ').strip())

cont = 1

while jogador != pc:
  if jogador < pc:
    jogador = int(input('Mais... Insira um novo palpite: ').strip())
  elif jogador > pc:
    jogador = int(input('Menos... Insira um novo palpite: ').strip())
  cont +=1

print(f'Você venceu com {cont} tentativas. Parabéns!')