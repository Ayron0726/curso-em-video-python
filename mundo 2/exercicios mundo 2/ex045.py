#Crie um programa que faça o computador jogar jokenpô com você.

from random import randint
from time import sleep

itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada: '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 25)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 25)
if computador == 0: # Computador jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('JOGADOR VENCE')
    elif jogador == 2:
        print('COMPUTADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 1: # Computador jogou PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCE')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR VENCE')
    else:
        print('JOGADA INVÁLIDA')
elif computador == 2: # Computador jogou TESOURA
    if jogador == 0:
        print('JOGADOR VENCE')
    elif jogador == 1:
        print('COMPUTADOR VENCE')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')

""" Meu código
from random import choice
from time import sleep

print('=' * 70)
print('Jogo do pedra, papel e tesoura!')
opcao = int(input('Escolha uma opção:\n[ 1 ]- Pedra\n[ 2 ]- Papel\n[ 3 ]- Tesoura\nOpção selecionada: '))
print('Processando....')
sleep(2)

if opcao == 1:
    jogador = 'Pedra'
elif opcao == 2:
    jogador = 'Papel'
elif opcao == 3:
    jogador = 'Tesoura'
else:
    print('Opção inválida')

n1 = 'Pedra'
n2 = 'Papel'
n3 = 'Tesoura'
lista = n1, n2, n3
escolhido = choice(lista)

if escolhido == 'Pedra' and jogador == 'Tesoura':
    print('Você perdeu, eu escolhi {} e você escolheu {}'.format(escolhido, jogador))
elif escolhido == 'Papel' and jogador == 'Pedra':
    print('Você perdeu, eu escolhi {} e você escolheu {}'.format(escolhido, jogador))
elif escolhido == 'Tesoura' and jogador == 'Papel':
    print('Você perdeu, eu escolhi {} e você escolheu {}'.format(escolhido, jogador))
elif jogador == 'Pedra' and escolhido == 'Tesoura':
    print('Você ganhou, escolhi {} e você {}, parabéns!'.format(escolhido, jogador))
elif jogador == 'Papel' and escolhido == 'Pedra':
    print('Você ganhou, escolhi {} e você {}, parabéns!'.format(escolhido, jogador))
elif jogador == 'Tesoura' and escolhido == 'Papel':
    print('Você ganhou, escolhi {} e você {}, parabéns!'.format(escolhido, jogador))
elif jogador == escolhido:
    print('Empatamos kkkkk, tente novamente')"""
