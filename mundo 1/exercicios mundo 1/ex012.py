#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço com 5% de desconto.

preco = float(input('Digite o preço da mercadoria: '))
print('O novo preço com 5% de desconto é: {:.2f}'.format(preco - (preco * 0.05)))