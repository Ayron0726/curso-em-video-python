#Faça um programa que leia uma frase pelo teclado e mostre:
#1 - Quantas vezes aparece a letra "A"
#2 - Em que posição ela aparece a primeira vez
#3 - Em que posição ela aparece a última vez

frase = str(input('Digite uma frase: ')).strip().upper()

print('Número de vezes que aparece a letra (a): {}'.format(frase.count('A')))
print('Em que posição ela aparece a primeira vez: {}'.format(frase.find('A')+1))#O +1 serve para mostra a posição Ex: posição 0 fica 0 + 1 = posição 1
print('Em que posição ela aparece pela última vez: {}'.format(frase.rfind('A')+1))#O rfind vai começar a procurar da direita ara esquerda da string.