# Faça um programa que identifica se existe tal cidade inicia com Santo

print('XXXX Encontre a Palavra XXXX')
cidade = str(input('Digite uma cidade: ')).strip()

ver = cidade[0:5].upper() == 'SANTO'

print(ver)

#### 2ª FORMA ######
'''
print('XXXX Encontre a Palavra XXXX')
cidade = input('Digite uma cidade: ')
cidade = cidade.lower()

encontre = int(cidade.find('santo'))

if encontre == 0:
  print('Começa com a palavra Santo.')
else:
  print('Não começa com a palavra Santo.')
  '''