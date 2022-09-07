#Desenvolva um programa que pergunte a distância de uma viagem em KM. Calcule o preço da passagem, 
# cobrando R$0.50 por KM para viagens até 200KM e R$0.45 para viagens mais longas.

km = int(input('Digite a distância da viagem em Km: '))
if km <= 200:
    valor = km * 0.50
    print('O valor da sua passagem é: R${:.2f}'.format(valor))
else:
    valor = km * 0.45
    print('O valor da sua passagem é: R${:.2f}'.format(valor))