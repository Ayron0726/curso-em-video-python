#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Digite a quantidade de kilometros percorridos: '))
dias = int(input('Digite a quantidade de dias de locação: '))
total = (km * 0.15) + (dias * 60)

print('Você rodou {:.2f}KM e usou o carro por {} dias, o total a pagar é de R${:.2f}'.format(km, dias, total))