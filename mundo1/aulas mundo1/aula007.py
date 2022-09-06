n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))

print('A soma entre {} e {} é: {}'.format(n1, n2, n1 + n2))

print('\n',pow(4,3))#potenciação
print('\n',4 ** 3)#potenciação
print('\n',81 ** (1/2))#raíz quadrada
print('\n',127 ** (1/3))#raíz cúbica

print('oi' + 'olá')
print('oi' * 5)
print('=' * 20)

nome = str(input('Qual é o seu nome?:'))
print('\nPrazer em te conhecer {:20}!'.format(nome))#a formatação na mácara informa que o conteúdo deve ser alinhado dentro do parâmetro informado.
print('\nPrazer em te conhecer {:>20}!'.format(nome))#a formatação na mácara informa que o conteúdo deve ser alinhado dentro do parâmetro informado nesse caso à direita dos espaços.
print('\nPrazer em te conhecer {:<20}!'.format(nome))#a formatação na mácara informa que o conteúdo deve ser alinhado dentro do parâmetro informado nesse caso à esquerda dos espaços.
print('\nPrazer em te conhecer {:^20}!'.format(nome))#a formatação na mácara informa que o conteúdo deve ser alinhado dentro do parâmetro informado nesse caso centralizado entre os espaços.
print('\nPrazer em te conhecer {:=^20}!'.format(nome))#a formatação na mácara informa que o conteúdo deve ser alinhado dentro do parâmetro informado nesse caso centralizado entre os espaços e imprimindo sinais de = nos espaços em branco.

n3 = int(input('\nUm valor: '))
n4 = int(input('\nOutro valor: '))
s = n3 + n4
m = n3 * n4
d = n3 / n4
di = n3 // n4
e = n3 ** n4
print('A soma é: {}\n o produto é: {}\n e a divisão é: {:.2f}'.format(s, m, d), end='>>>')
print('Divisão inteira: {}\n e potência: {}'.format(di, e))
