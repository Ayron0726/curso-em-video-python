#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#Se ele ainda vai se alistar no serviço militar.
#Se é hora de se alistar.
#Se já passou o tempo de alistamento
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano_nascimento = int(input('Digite seu ano de nascimento: '))

idade = date.today().year - ano_nascimento

if idade < 18:
    print('Falta {} anos para o alistamento'.format(18 - idade))
elif idade == 18:
    print('Hora de se alistar')
else:
    print('Já passou {} anos do alistamento'.format(idade - 18))