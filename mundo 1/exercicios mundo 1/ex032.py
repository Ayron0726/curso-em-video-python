#Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
# Fórmula = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)

from datetime import date#Biblioteca para pegar data e hora do sistema

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ao atual: '))
if ano == 0:
    ano = date.today().year#Pega o ano da máquina
if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
    print('{} É BISSEXTO!'.format(ano))
else:
    print('{} NÃO É BISSEXTO!'.format(ano))