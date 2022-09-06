
#Fatiamento

frase = str('Curso em Vídeo Python')

print(frase[9])#Imprime o item 9 (V)
print(frase[9:13])#Pega os itens mas não trás o último, para pegar adiciona mais 1 ex: [9:14] (Víde)
print(frase[9:21])#Imprime toda a frase pois está adicionando o último elemento (Vídeo Python)
print(frase[9:21:2])#Pega todos os itens mas imprime pulando de 2 em 2 (VdoPto)
print(frase[:5])#Imprime pegando do início e vai até o caractere 5 - 1 (Curso)
print(frase[15:])#Imprime começando do 15 mas vai até o final (Python)
print(frase[9::3])#Imprime começando do 9 e pula de 3 em 3 (VePh)
print(frase [::2])#Pega todos os itens da string mas imprime somente pulando de 2 em 2 (Croe íe yhn)

#Análise

print(len(frase))#Comprimento (Qual o comprimento da frase?) (21)
print(frase.count('o'))#Contar quantas letra (o) minúsculas tem a frase (3)
print(frase.count('o', 0, 13))#conta as letras (o) na frase com fatiamento, considerando da posição 0 até a 13 - 1 (1)
print(frase.find('deo'))#mostra em qual posição que começou a combinação (deo) na frase (11).
print(frase.find('Android'))#Retorna que não existe essa palavra dentro da string, o seu valor é -1 (-1).
print(frase.rfind('o'))#Procura a letra 'o' na string da direita para esquerda.
print('curso' in frase)#Consulta se dentro da frase tem a palavra (curso) o retorno poderá ser True ou False (False).


#Transformação

print(frase.replace('Python', 'Android'))#Vai trocar o nome (Python) por (Android) somente no momento do print, se for para mudar tem que fazer (frase = frase.replace('Python', 'Android'))(Curso em Vídeo Android)
print(frase.upper())#O que já é maiúsculoo ele mantém, e transforma tudo em maiúsculo (CURSO EM VÍDEO PYTHON).
print(frase.lower())#Mantém o que é minúsculo e tranforma tudo para minúsculo (curso em vídeo python).
print(frase.capitalize())#Coloca todos os caracteres em minúsculos e deixa somente o primeiro em maiúsculo (Curso em vídeo python).
print(frase.title())#Conta as palavras com base nos espaços e muda a primeira letra de cada palavra para maiúscula (Curso Em Vídeo Python).

frase = str('   Aprenda Python  ')

print(frase.strip())#Remove todos os espaços inúteis no início e fim (Aprenda Python).
print(frase.rstrip())#Remove os espaços do lado direito da string (r = right) (   Aprenda Python)
print(frase.lstrip())#Remove os espaços do lado esquerdo da string (l = left) (Aprenda Python   )

frase = str('Curso em Vídeo Python')

print(frase.split())#Divide a string em pedaços com base nas palavras e, cada pedaço começa na posição 0, nesse caso formando novas strings, formando uma lista ['Curso', 'em', 'Vídeo', 'Python'] Listas em Python são separadas por colchetes[].
print('-'.join(frase))#Junta os itens da strings usando '-' para separar (C-u-r-s-o- -e-m- -V-í-d-e-o- -P-y-t-h-o-n).

print("""\nWelcome! Are you completely new to programming? 
about why and how to get started with Python. Fortunately 
an experienced programmer in any programming language 
(Whatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!\n""" )#Imprimir um texto inteiro.

print(frase.upper().count('O'))#Transforma a string em maiúculo e retorna quantas letras (O) tem (3).
print(len(frase.strip()))#Imprime o tamanho da string mas sem os espaços (21).

dividido = frase.split()
print(dividido[0])#Após divisão e transformação da string em lista, ele mostra o item na posição 0 da lista (Curso)
print(dividido[2] [3])#Pega a posição 2 da lista [Vídeo] e pega a posição número 3 do item, no caso a letra (e)

