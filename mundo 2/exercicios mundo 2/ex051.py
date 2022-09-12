#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10
#primeiros termos dessa progressão.

#a1: primeiro termo
#an: termo que se quer descobrir
#n: posição que o termo ocupa
#r: razão
#Fórmula an = a1 + (n - 1) * r

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 1
for i in range(0, 10):
    pa = (a1 + (i - 1)) * r
    cont += i
    print('Termo número {} = {}'.format(cont, pa))
print('FIM')