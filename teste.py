import datetime

print('QUEM É MAIOR OU MENOR DE IDADE?')

menor = 0
maior = 0

idades = []
nomes = []

for ano in range(1,4):
  nome = str(input('Digite seu Nome: '))
  ano = int(input(f'Ano de Nascimento da {ano}ª pessoa: '))
  idade = datetime.date.today().year - ano
  if idade < 18:
    menor += 1
  else:
    maior +=1

  idades.append(idade)
  nomes.append(nome)

print(f'''Neste grupo de pessoas existem {menor} menores de idade e
{maior} maiores de idade.''')

for idade in idades:
  print(f'{nomes[idades.index(idade)]} tem {idade} anos.')