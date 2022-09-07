#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#-1 para binário
#-2 para octal
#-3 para hexadecimal

numero = int(input('Digite um número inteiro: '))
opcao = int(input('Escolha as opções abaixo:\n1- Para converter em binário\n2- Para converter em octal\n3- Para converter em hexadecimal\nOpção selecionada: '))

if opcao == 1:
    print('O número {} em binário é: {}'.format(numero, bin(numero)))
elif opcao == 2:
    print('O número {} em octal é: {}'.format(numero, oct(numero)))
elif opcao == 3:
    print('O número {} em hexadecimal é: {}'.format(numero, hex(numero)))
else:
    print('Opção inválida, tente novamente.')
    