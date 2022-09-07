#Escreva um programa que leia um valor em metros e o exiba convertiddo em centímetros e milímetros.

metros = float(input('Digite o valor em metros: '))
print('Valor em decímetros: {}'.format(metros * 10))
print('Valor em centímetros: {}'.format(metros * 100))
print('Valor em milímetros: {}'.format(metros * 1000))
print('Valor em decâmetros: {}'.format(metros / 10))
print('Valor em hectômetro: {}'.format(metros / 100))
print('Valor em kilometros: {}'.format(metros / 1000))
