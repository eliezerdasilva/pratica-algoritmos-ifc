'''
 As posições das casas em tabuleiros de xadrez são identificadas 
por uma letra e um número. A letra identifica a coluna e o número define a linha, conforme a 
figura abaixo

Escreva um programa Python que receba do usuário um posição. Use um comando if para 
determinar se a coluna informada começa com quadrado preto ou branco. Então, use 
aritmética de inteiros para determinar a cor do quadrado da linha correspondente. Por 
exemplo, se o usuário entrou com o valor a1, então seu programa deve informar que o 
quadrado é preto. Se o usuário entrou com o valor d5, então seu programa deve informar que 
o quadrado é branco. Seu programa pode assumir que o usuário vai entrar valores válidos, 
não sendo necessário verificar eventuais erros de input

'''

posicao = input("Informe a posição no tabuleiro de xadrez(A1): ")
coluna = posicao[0]
linha = int(posicao[1])

if coluna in 'aceg':
    cor_coluna = 'preto'
else:
    cor_coluna = 'branco'
    
if cor_coluna == 'preto':
    if linha % 2 == 0:
        cor_quadrado = 'branco'
    else:
        cor_quadrado = 'preto'
else:
    if linha % 2 == 0:
        cor_quadrado = 'preto'
    else:
        cor_quadrado = 'branco'

print("O quadrado em", posicao, "é", cor_quadrado)
