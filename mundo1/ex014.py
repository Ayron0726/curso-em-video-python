#Escreva um programa que converta um temperatura digitada em C e converta para F.

c = float(input('Informe a temperatura em C°: '))
f = (c * 1.8) + 32
print('A temperatura de {}°C corresponde a {:.1f}°F'.format(c, f))