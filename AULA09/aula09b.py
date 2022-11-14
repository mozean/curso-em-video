# Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(), title(), strip(), junção com join().

titulo = str(5*'<>'+'ANÁLISE TEXTUAL'+5*'<>')
print(titulo)
frase = input('Escreva algo: ')

titulo = str('DESCUBRA QUANTA VEZES APARECE A LETRA DESEJADA')
print(titulo)

letra = input('Insira a letra desejada: ')

contagem_letras = frase.upper().lower().count(letra)

print(f'A letra {letra}: aparece {contagem_letras} vezes em {frase.upper()}.')

print('Deseja continuar? Sim 1 ou Não (2)')
continuar = int(input('Digite a opção desejada: '))

"""while continuar ==1:
  return(frase) """