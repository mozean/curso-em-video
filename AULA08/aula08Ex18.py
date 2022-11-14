# SENO, COSSENO E TANGENTE DE UM ÂNGULO
import math

print(5*'<>','SENO, COSSENO E TANGENTE DE UM ÂNGULO',5*'<>')
print()
angulo = (float(input('Insira o valor do ânulo em graus: ')))
radiano = math.radians(angulo)

sen = math.sin(radiano)
cos = math.cos(radiano)
tan = math.tan(radiano)

print()

print(5*'<>',f'SENO, COSSENO E TANGENTE DE UM ÂNGULO DE {angulo}º',5*'<>')

print()

print(f'SENO: {sen:.2f}')
print(f'COSSENO: {cos:.2f}')
print(f'TANGENTE: {tan:.2f}')