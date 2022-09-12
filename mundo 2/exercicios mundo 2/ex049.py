#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora
#utilizando um laço for.

n = int(input('Digite um número: '))
print('-=' *25)
print('Tabuada de {}'.format(n))
print('-=' * 25)
for i in range(0, 11):
    print('{}  x {:2} = {}'.format(n, i, (n * i)))
