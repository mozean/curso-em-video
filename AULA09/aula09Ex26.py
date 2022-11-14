# Faça um program que leia uma frase pelo teclado:

frase = str(input('Insira uma frase: ')).lower().strip()
print('Entrada: ',frase)

# Quantas vezes aparece a letra 'a'
a = frase.count('a')
print('Quantas vezes aparece a letra a:',a)

# Posição do primeiro 'a'
primeiro_a = frase.find('a')

print('Posição do primeiro a:',primeiro_a)

# Posição do último 'a'
ultimo_a = frase.rfind('a')
print('Posição do último a:',ultimo_a)

'''
#SEGUNDA FORMA
frase_invertida = frase[::-1]
ultimo_a = frase_invertida.lower().find('a')
ultimo_a = len(frase)-ultimo_a
print('Posição do último a:',ultimo_a)
'''


