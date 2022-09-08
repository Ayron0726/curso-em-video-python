#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final,
#de acordo com a média atingida:
#-Média abaixo de 5.0: REPROVADO
#-Média entre 5.0 e 6.9: RECUPERAÇÃO
#-Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5.0:
    print('Sua média foi {} e seu status é: \033[1;31mREPROVADO!\033[m'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média foi {} e seu status é: \033[1;33mRECUPERAÇÃO!\033[m'.format(media))
elif media >= 7:
    print('Sua média foi {} e seu status é: \033[1;32mAPROVADO!\033[m'.format(media))