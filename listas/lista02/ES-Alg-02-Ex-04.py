'''
Crie um programa que obtém 3 números inteiros do usuário e os 
exibe de forma ordenada do menor para o maior. Use as funções min e max para encontrar o 
menor valor e o maior valor. Dica: o valor do meio pode ser obtido pela soma dos três valores, 
subtraída do maior e do menor.
'''

n1 = int(input("Informe um número inteiro"))
n2 = int(input("Informe um número inteiro"))
n3 = int(input("Informe um número inteiro"))

nMenor = min(n1, n2, n3)
nMaior = max(n1, n2, n3)

# Calculando o valor do meio
nMeio = n1 + n2 + n3 - nMenor - nMaior
print(" A sequencia é :",nMenor,nMeio,nMaior)