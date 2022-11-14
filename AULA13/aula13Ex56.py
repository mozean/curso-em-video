# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

print('<><><><> ANALISADOR COMPLETO <><><><>')

nomes = []
idades = []
homens = []
idades_homens = []
mulheres = []
idades_mulheres = []

for pessoa in range(1,5):
  print(f'****** Cadastro da {pessoa}ª Pessoa ******')
  print('XXX INFORME SEU NOME XXX')
  print('>>>',end='')
  nome = str(input('>>> '))
  print('XXX INFORME SUA IDADE XXX')
  print('>>>',end='')
  idade = int(input())
  
  print('XXX INFORME SEU SEXO XXX')
  print('[ 1 ] Masculino')
  print('[ 2 ] Feminino')
  sexo = int(input('Insira a opção de sexo: '))
  nomes.append(nome)
  idades.append(idade)

  # HOMEM MAIS VELHO
  if sexo == 1:
    homens.append(nome)
    idades_homens.append(idade)

    # MULHER ABAIXO DE 20 ANOS
  if sexo == 2 and idade < 20:
    mulheres.append(nome)

# HOMEM
idade_max = max(idades_homens,key=int)
posicao_idade = idades_homens.index(idade_max)
homem_mais_velho = homens[posicao_idade]

# MULHER
mulher_menor = len(mulheres)

# MÉDIA DAS IDADES
media = sum(idades)/5

print (f'''
A média de idade desse grupo é de {media} anos.
O homem mais velho do grupo é o {homem_mais_velho} e ele tem {idades_homens[posicao_idade]} anos.
Existem {mulher_menor} mulher(es) menor(es) de 20 anos.
''')