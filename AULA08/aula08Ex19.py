# O SORTEIO
titulo = 'QUEM APAGARÁ A LOUSA?'
import random
import math
lista = ['Mozean','Maciel','Rebca','Aurilene']

print(5*'<>',titulo,5*'<>')
print()
aluno = random.choice(lista)

print()
print(f'Quem apagará a lousa será o(a): {aluno}')