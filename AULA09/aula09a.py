# Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

frase = input('Escreva algo: ')

# Quantidade de Caracteres

caracteres = len(frase)

print(caracteres)

# Escreva um programa que descreva sua entrada de nomes.

frase = input('Escreva algo: ')

comprimento = len(frase)
maiuscula = frase.upper()
minuscula = frase.lower()
cap = frase.capitalize() # somente primeira letra em maiúscula de cada palavra.

title = frase.title() # primeira letra em maiúscula sem alterar as outras.

nospace = frase.strip() #sem espaços extras

nospaceleft = frase.lstrip() #sem espaços extras à esquerda.

nospaceright = frase.rstrip() #sem espaços extras à direita.

split = frase.split() # divide uma cadeia de caracteres em listas.

troca = frase.replace() #troca de palavras

juntarsplit = '_'.join(split)

print(f'Tamanho: {comprimento} caracteres')
print()
print(f'Maiúscula: {maiuscula}')
print()
print(f'Minúscula: {minuscula}')
print()
print(f'Capitalizaçao: {cap}')
print()
print(f'Título: {title}')
print()
print(f'Sem epaços: {nospace}')
print()
print(f'Sem espaços à esquerda:  {nospaceleft}')
print()
print(f'Sem espaços à direita: {nospaceright}')
print()
print(f'Separa cadeia em listas: {split}')
print()
print(f'Juntar Split: {juntarsplit}')

'''
# Qtde determinada letra

m = frase.count('m')
o = frase.count('o')
z = frase.count('z')
e = frase.count('e')
a = frase.count('a')
n = frase.count('n')

r = frase.count('r')
d = frase.count('d')
i = frase.count('i')
g = frase.count('g')
u = frase.count('u')
s = frase.count('s')

l = frase.count('l')
v = frase.count('v')


print('m:',m)
print('o:',o)
print('z:',z)
print('e:',e)
print('a:',a)
print('n:',n)

print('r:',r)
print('d:',d)
print('i:',i)
print('g:',g)
print('u:',u)
print('s:',s)

print('l:',l)
print('v:',v)
'''
