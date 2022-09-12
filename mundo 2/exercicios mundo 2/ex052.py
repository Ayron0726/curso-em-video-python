#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

n = int(input('Digite um número inteiro: '))
if n % 1 == 0:
    print('{} é um número primo'.format(n))