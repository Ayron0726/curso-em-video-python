#Entre o colchete e a letra (m) seguir conforme abaixo
#Primeiro código do estilo "style"(Código do comportamento, negrito, sublinhado) seguido de ";"
#Segundo código do texto "text" (informa a cor do texto) seguido de ";"
#Terceiro código do fundo "background" (informa a cor do fundo)
#Estyle = "0" - estilo nenhum
#Text = "33" -
#Back = "44"

\033[0;33;44m

#Códigos para style (0 = none, 1 = negrito, 4 = sublinhado, 7 = inverte as configurações(o que colocou para fundo vai para letra e vice versa))
#Códigos para text (30 = branco, 31 = vermelho, 32 = verde, 33 = amarelo, 34 = azul, 35 = magenta, 36 = ciano, 37 = cinza)
#Códigos de back (40 = branco, 41 = vermelho, 42 = verde, 43 = amarelo, 44 = azul, 45 = magenta, 46 = ciano, 47 = cinza)

\033[0;30;41m #Letra branca e fundo vermelho
\033[4;33;44m #Letra amarela e fundo azul
\033[1;35;43m #Letra magenta e fundo amarelo
\033[30;42m #letra branca e fundo verde
\033[m #Desfaz a configuraçao deixando padrão
\033[7;30m #Inversão, pega a cor preto e coloca na letra, e cor branco no fundo

print('\033[4;30;45mOlá mundo!\033[m')#Coloca o \033[m no final para a coloração ir só até o funal da frase
a = 3
b = 5
print('Os valores são \033[32;40m{}\033[m e \033[31;40m{}\033[m'.format(a, b))#para fechar o local que será exibido com cor deve iniciar com \033[m e fechar com \033[m EX: \033[1;31;43m \033[m

nome = 'Ayron'

cores = {'limpa' : '\033[m', #Coleção - método para chamar uma cor sem precisar digitar manualmente
        'azul' : '\033[34m', 
        'amarelo' : '\033[33m', 
        'pretoebranco': '\033[7;40m'}

print('Olá muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))#Abrindo e fechando código de cor no print com o {}.format
print('Olá! Muito prazer em te conhecer, {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))

