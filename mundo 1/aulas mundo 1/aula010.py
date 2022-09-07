'''tempo = int(input('Quantos anos tem o seu carro?: '))

if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('---Fim---')

tempo = int(input('Quantos anos tem o seu carro?: '))
print('carro novo'if tempo <=3 else 'carro velho')
print('---Fim---')

nome = str(input('Digite o seu nome: ')).strip()
if nome == 'Ayron':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
    print('Bom dia {}'.format(nome))'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segundo nota: '))
m = (n1 + n2)/2

print('Sua média foi {:.1f}'.format(m))
print('PARABÉNS!' if m >=6 else 'ESTUDE MAIS!')

if m >= 6:
    print('Sua média foi boa PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
