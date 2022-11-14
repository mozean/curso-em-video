# Faça um programa que leia um nome completo e mostre o primeiro e último nome separados.

frase = input('Insira seu nome completo: ')
print('Nome Completo: ',frase)

separado = frase.split()

# Primeiro nome.
print('Primeiro Nome: ',separado[0])

#Ultimo Nome
print(f'Seu último nome é: {separado[len(separado)-1]}')


'''
#SEGUNDA FORMA
inverter = frase[::-1]
separado = inverter.split()
separado = separado[0]
separado = separado[::-1]
print('Último Nome: ',separado)
'''