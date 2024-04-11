'''
Faça uma função chamada sorteia_dado(), que deve retornar um número inteiro aleatório 
entre um 1 e 6 (inclusive). Para gerar os números aleatórios, pesquise sobre a biblioteca 
random do Python.
'''
import random
def sorteia_dado():
    return random.randint(1, 6)
resultado = sorteia_dado()
print(resultado)