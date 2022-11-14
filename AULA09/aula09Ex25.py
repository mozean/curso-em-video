# Faça um programa que identifica se existe tal nome possui silva.

print('XXXX Encontre a Palavra XXXX')
nome = input('Digite uma nome: ')
sobre = 'silva' in nome.lower()
print(sobre)

### Minha Forma #####

'''
print('XXXX Encontre a Palavra XXXX')
nome = input('Digite uma nome: ')
nome = nome.lower()

sobre = 'Silva'
encontre = int(nome.find(sobre.lower()))


if encontre == -1:
  print('Não possui Silva no nome')
else:
  print('Sim. Possui Silva no nome.')

'''