#Crie um programa que leia o nome completo de uma pessoa e mostre:
#1 - O nome com todas as letras maiúsculas
#2 - O nome com todas as letras minúsculas
#3 - Quantas letras ao todo (sem considerar os espaços)
#4 - Quantas letras tem o primeiro nome

nome = str(input('Digite o nome completo: ')).strip()#Desconsidera os espaços no início e fim da frase

print('Nome com todas letras maiúsculas: {}'.format(nome.upper()))
print('Nome comtodas as letras minúsculas: {}'.format(nome.lower()))
print('Quantidade de letras sem espaços: {}'.format(len(nome) - nome.count(' ')))#Verifica o tamnho da frase e tira os espaços.
dividido = nome.split()
print('A quantidade de letras do primeiro nome: {}'.format(len(dividido[0])))