#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "SANTO"

cidade = input('Digite o nome da cidade: ').strip()
cidade = cidade.upper()
print('A cidade {} começa com com a palavra SANTO?: {}'.format(cidade, cidade[:5].upper() == 'SANTO'))
