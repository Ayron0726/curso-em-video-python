#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar no serviço militar.
#Se é hora de se alistar.
#Se já passou o tempo de alistamento
from datetime import date

ano_nascimento = int(input('Digite seu ano de nascimento: '))

idade = date.today().year - ano_nascimento
idalist = idade

if idalist < 0:
    passou = 

if idade < 18:
    print('Ainda vai se alistar')
    print('Falta {} anos para o alistamento'.format())
elif idade == 18:
    print('Hora de se alistar')
else:
    print('Já passou o tempo do alistamento')