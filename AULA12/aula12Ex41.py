'''
Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
'''

import datetime

print('\033[1;45;35m<><><><><> CLASSIFICAÇÃO DO ATLETA <><><><><>\033[m')
# Pergunte o valor da casa.
'''idade = datetime.date.year
print(idade)'''

atual = datetime.date.today().year
ano = int(input('Insira seu ano de nascimento: '))
idade = atual - ano

if idade <= 9:
    print(f'O Atleta tem: {idade} anos.')
    print('Classificação do Atleta: MIRIM.')
elif 9 < idade <= 14:
    print(f'O Atleta tem: {idade} anos.')
    print('Classificação do Atleta: INFANTIL.')
elif 14 < idade <= 19:
    print(f'O Atleta tem: {idade} anos.')
    print('Classificação do Atleta: JÚNIOR.')
elif 19 < idade <= 25:
    print(f'O Atleta tem: {idade} anos.')
    print('Classificação do Atleta: SÊNIOR.')
else:
    print(f'O Atleta tem: {idade} anos.')
    print('Classificação do Atleta: MASTER.')
