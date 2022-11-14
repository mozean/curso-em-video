# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

print('<><><> DESCUBRA SE O ANO É BISSEXTO <><><>')

ano = int(input('Insira um valor em anos: '))

resto_1 = ano%400
resto_2 = ano%100
resto_3 = ano%4

if resto_1 == 0:
  print(f'O ANO {ano} COM CERTEZA É BISSEXTO.')

if resto_2 > 0 and resto_3 == 0:
  print(f'O ANO {ano} É BISSEXTO.')

if resto_3 > 0:
  print(f'O ANO {ano} NÃO É BISSEXTO.')