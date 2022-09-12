#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, 
#indo de 10 até 0, com uma pausa de 1 segundo.

from time import sleep

print('Contagem regressiva...')
for c in range(11, 0, -1):
    print(c - 1) #, end = (' '))
    sleep(1)
print('Feliz ano novo!!')