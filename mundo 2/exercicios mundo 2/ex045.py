#Crie um programa que faça o computador jogar jokenpô com você.

from random import choice
from time import sleep

print('=' * 70)
print('Jogo do pedra, papel e tesoura!')
opcao = int(input('Escolha uma opção:\n1- Pedra\n2- Papel\n3- Tesoura\nOpção selecionada: '))
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
    print('Empatamos kkkkk, tente novamente')
