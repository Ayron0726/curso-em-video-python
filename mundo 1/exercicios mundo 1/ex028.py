#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar 
# descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep#importar o método sleep para criar um atraso na execução.

computador = randint(0, 5)

print('-+-'*20)
print('Vou pensar e um número entre 0 e 5. Tente adivinhar... ')
print('-+-'*20)

jogador = int(input('Em que número eu pensei? '))
print('Processando....')
sleep(2)#Cria um atraso para seguir o resto do bloco, tem que importar (time)

if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}'.format(computador, jogador))
