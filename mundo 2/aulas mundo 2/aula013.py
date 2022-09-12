#Laço for

'''for g in range(0, 3):
    if g == 1:
        print('Pega moeda')
    else:
        print('Passo')
        print('Pula')
        print('Passo')
        print('Pega')

for h in range(0, 6): # Contando do zero, vai considerar as 6 posições. Se for começar do 1 ele vai até 5
    print(h)
    print('Oi')
print('FIM')
for i in range(6, 0, -1): # Consideração da iteração, nesse caso, de trás pra frente.
    print(i)
for j in range(0, 7, 2): # Imprimindo com saltos de 2 em 2
    print(j)

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p): #Começa do inicio = k, fim + 1 = l e pula de acordo com o passo = m
    print(c)
print('Fim')# O que está fora do for ele segue normalmente'''
s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    s += n # Mesmo que declarar(s = s + n)
print('O somatório de todos os valores foi {}'.format(s))



