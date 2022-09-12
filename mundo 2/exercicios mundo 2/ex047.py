#Crie um programa que mostre na tela todos os números pares que estão na intervalo entre 1 e 50.

for i in range(1, 51):
    if i % 2 == 0:
        print('{} é par'.format(i))
print('fim')