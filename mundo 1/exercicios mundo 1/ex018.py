#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))
print('O ângulo de {}° tem o seno de: {:.2f}'.format(angulo, sin(radians(angulo))))
print('O ângulo de {}° tem o cosseno de: {:.2f} '.format(angulo, cos(radians(angulo))))
print('O ângulo de {}° tem a tangente de: {:.2f} '.format(angulo, tan(radians(angulo))))