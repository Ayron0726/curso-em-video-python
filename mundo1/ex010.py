#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Considere US$1.00 = 3.27

dinheiro = float(input('Digite quanto você tem em dinheiro: '))
print('Você pode comprar {:.2f} dólares'.format(dinheiro / 3.27))
