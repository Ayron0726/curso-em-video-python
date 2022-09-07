#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar
#o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('\033[1;33m-=\033[m' * 70)
print('Banco da PQP')
print('\033[1;33m-=\033[m' * 70)

valor_casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valodor do seu salário: R$'))
anos = int(input('Em quantos anos deseja pagar: '))
meses = anos * 12
parcela = valor_casa / meses

if parcela <= ((salario * 30) / 100):
    print('Seu empréstimo será aprovado!')
    print('Com base no seu salario de R${:.2f}, sua parcela será de R${:.2f}'.format(salario, parcela))
else:
    print('Infelizmente não conseguimos aprovar o seu financiamento ;-(')
    print('Sua parcela excedeu o valor e ficaria no valor de R${:.2f} ultrapassando o limite do salário'.format(parcela))