#Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
#e condição de pagamento:
#-à vista dinheiro/cheque: 10% de desconto
#à vista no cartão: 5% de desconto
#em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros

print('{:^40}'.format('Lojas não sei')) #Centraliza e preenche os espaços com

preco = float(input('Digite o preço das compras: R$'))
opcao = int(input('Escolha a opção de pagamento\n1- À vista dinheiro/cheque(10% de desconto)\n2- À vista no cartão(5% de desconto)\n3- Em até 2x no cartão(preço normal)\n4- 3x ou mais no cartão(20% de juros)\nOpção selecionada: '))

if opcao == 1:
    print('O valor de R${:.2f} com 10% de desconto à vista é R${:.2f}'.format(preco, preco - ((preco * 10) / 100)))
elif opcao == 2:
    print('O valor de R${:.2f} com 5% de desconto à vista no cartão é R${:.2f}'.format(preco, preco - ((preco * 5) / 100)))
elif opcao == 3:
    print('O valor de R${:.2f} parcelado em 2x ficará em parcelas de R${:.2f}'.format(preco, preco / 2))
elif opcao == 4:
    parcelas = int(input('Digite a quantidade de parcelas: '))
    if parcelas >= 3 and parcelas <= 12:
        pagar = (preco + (preco * 20) / 100) / parcelas
        print('O valor de R${:.2f} parcelado em {}x ficará com parcelas de R${:.2f}'.format(preco, parcelas, pagar))
    elif parcelas < 3 and parcelas > 12:
        print('Tente outra opção')
    else:
        print('Opção indisponível')
else:
    print('Opção inválida')