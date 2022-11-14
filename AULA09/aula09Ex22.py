# Programa que leia o nome completo de uma pessoa e mostre:
# com todas maiusculas
#minusclas
#quantidade de letras (sem espaços)
# quantas letras o primeiro nome

print(5*'X', 'ANALISE SEU NOMES', 5*'X')

#      MAIUSCULAS
nome = input('Insira seu nome: ')
print(f'Nome com letras maiúsculas: {nome.upper()}')

#        MINÚSCULAS
print(f'Nome com letras minúsculas: {nome.lower()}')

#       QUANTIDADE DE LETRAS

'''
separado = nome.split()
junte = ''.join(separado)

print(f'Quantidade de letras do seu nome: {len(junte)}')
'''
print('Quantidade de letras do seu nome: ',len(''.join(nome.split())))

#    Quantidade de Letras 1º Nome
primeiro_nome = nome.split()[0]
print(f'Quantidade de letras do 1º nome: {len(primeiro_nome)}')