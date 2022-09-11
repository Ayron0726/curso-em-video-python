#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status
#de acordo com a tabela abaixo:
#-Abaixo de 18.5: Abaixo do peso
#-Entre 18.5 e 25: Peso ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#-Acima de 40: Obesidade mórbida

from math import pow

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (pow(altura, 2))

if imc > 0 and imc < 18.5:
    print('Seu IMC está em {:.2f} e você está abaixo do peso'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC está em {:.2f} e você está com peso ideal'.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu IMC está em {:.2f} e você está com sobrepeso'.format(imc))
elif imc > 30 and imc <= 40:
    print('Seu IMC está em {:.2f} e você está com obesidade'.format(imc))
else:
    print('Seu IMC está em {:.2f} e você está com obesidade mórbida')
