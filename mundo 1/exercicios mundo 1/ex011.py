#Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade de tinta necessária para pita-la, sabendo que cada litro de tinta, pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digie a altura da paredeem metros: '))
area = (largura * altura) /2
print('Você irá precisar de {:.1f} litros de tinta'.format(area))