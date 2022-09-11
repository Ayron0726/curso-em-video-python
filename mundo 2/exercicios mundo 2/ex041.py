#A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um
#atleta e mostre sua categoria, de acordo com a idade:
#Até 9 anos: MIRIM
#Até 14 anos: INFANTIL
#Até 19 anos: JUNIOR
#Até 20 anos: SÊNIOR
#Acima: MASTER
from datetime import date
ano_nasc = int(input('Digite o ano do seu nascimento: '))
categoria = date.today().year - ano_nasc

if categoria > 0 and categoria <= 9:
    print('O atleta tem {} anos e a sua categoria é: MIRIM'.format(categoria))
elif categoria > 9 and categoria <= 14:
    print('O atleta tem {} anos e a sua categoria é: INFANTIL'.format(categoria))
elif categoria > 14 and categoria <= 19:
    print('O atleta tem {} anos e a sua categoria é: JÚNIOR'.format(categoria))
elif categoria == 20:
    print('O atleta tem {} anos e a sua categoria é: SÊNIOR'.format(categoria))
elif categoria > 20:
    print('O atleta tem {} anos e a sua categoria é: MASTER'.format(categoria))
else:
    print('Opção inválida')
    