#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis.

tipo = input('Digie alguma coisa: ')

print('\nO tipo primitivo desse valor é: ', type(tipo))
print('\nSó tem espaços?:',tipo.isspace())#informa se o que foi digitado são espaços
print('\nÉ um número?:',tipo.isnumeric())#informa se o conteúdo é numérico (só números)
print('\nÉ alfabético?:',tipo.isalpha())#informa se é alfabético (só letras)
print('\nÉ alfanumérico?:',tipo.isalnum())#informa se é alfanumérico (letras e números)
print('\nEstá em maiúsculo?:',tipo.isupper())#informa se todas as letras são maiúsculas (somentes todas maiúsculas)
print('\nEstá em minúsculo:',tipo.islower())#informa se todas as letras são minúsculas (somentes todas minúsculas)
print('\nEstá captalizado?:',tipo.istitle())#informa se tem letras maiúsculas e minúsclas junto
