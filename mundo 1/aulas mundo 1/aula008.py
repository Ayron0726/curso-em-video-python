from math import sqrt, floor, ceil, trunc
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz))) #floor arredonda para baixo
print('A raiz de {} é igual a {:.2f}'.format(num, ceil(raiz))) #floor arredonda para cima
print('A raiz de {} tem a sua parte inteira = {}'.format(num, trunc(raiz)))#mostra somete a parte inteira antes da vírgula

import random #números aleatórios
num = random.randint(1, 10)#range para números aleatórios
print(num)


