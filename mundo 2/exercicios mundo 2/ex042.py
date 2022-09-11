#Refaça o desafio dos triângulos acrescentando o recurso de mostrar que tipo de triângulo será mostrado:
#-Equilátero: todos os lados são iguais.
#Isósceles: dois lados iguais
#-Escaleno: todos os lados diferentes

print('-=' * 20)
print('Analisador de Triângulos')
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if r1 == r2 == r3: #and r1 == r3 and r2 == r1 and r2 == r3 and r3 == r1 and r3 == r2:
        print('Com as medidas informadas é possível formar um triângulo EQUILÁTERO')
    elif r1 == r2 or r3 == r1 or r3 == r2:
        print('Com as medidas informadas é possível formar um triângulo ISÓSCELES')
    else:
        #r1 != r2 != r3 != r1 fórmula para o escaleno
        print('Com as medidas informadas é possível formar um triângulo ESCALENO')        
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')
