# VERIFICAR O MAIOR, MENOR EM ENTRADAS:
'''
Use o >> if <<< e diz que o maior, menor valor é o primeiro e depois faz outro >>> if <<< dizendo que se a próxima entrada for maior, menor valor recebe ele.
'''
# EXEMPLO:
for idade in range(1,4):
  idades = int(input('Digite sua idade: '))
  if idade == 1:
    maior = idades
    menor = idades
  if idades > maior:
    maior = idades
  if idades < menor:
    menor = idades
    
print(f'O maior valor informado é {maior} e o menor valor é {menor}
