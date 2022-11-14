# O SORTEIO 2
titulo = 'ORDEM DE APRESENTAÇÃO'
import random

alunos = ['Mozean','Maciel','Rebca','Aurilene']

print(5*'<>',titulo,5*'<>')
print()
random.shuffle(alunos)

print(f'A ordem de apresentação será:')

posicoes = range(1,5)

for posicao in posicoes:
  print(posicao)
    continue
for aluno in alunos:
  print(aluno)

'''
for posicao in posicoes:
  posicao
  aluno

print(posicao, aluno)
print()
print(f'Quem apagará a lousa será o(a): {lista}')
'''

for num in range(5):
    if num == 3:
        print("Encontrei o 3")
        # Executa o continue, pulando para o próximo laço
        continue
    else:
        print(num)

    print("Estou abaixo do IF")
