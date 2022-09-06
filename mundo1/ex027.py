#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza
#Primeiro = Ana
#Último = Souza

nome = str(input('Digite o seu nome completo: ')).strip().lower()
dividido = nome.split()
print('Primeiro: {}'.format(dividido [0]))
print('Segundo: {}'.format(dividido[len(dividido)-1]))#Mostra o nome na posição do tamanho da string -1
