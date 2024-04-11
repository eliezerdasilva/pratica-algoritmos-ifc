'''
Usando a função da questão anterior, crie um novo programa que lance o dado 1 milhão de 
vezes. Conte e imprima quantas vezes cada número saiu. A probabilidade deu certo? Ou seja, 
a porcentagem dos numeros sorteados foi parecida
'''

import random

def lancar_dado():
    return random.randint(1, 6)

def contar_ocorrencias(n):
    contagem = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    for _ in range(n):
        resultado = lancar_dado()
        contagem[resultado] += 1
    return contagem

n_lancamentos = 1000000
ocorrencias = contar_ocorrencias(n_lancamentos)

for numero, contagem in ocorrencias.items():
    print(numero,contagem)
    percentual = (contagem / n_lancamentos) * 100
    print(f"Número {numero}: {contagem} vezes ({percentual:.2f}% das ocorrências)")
