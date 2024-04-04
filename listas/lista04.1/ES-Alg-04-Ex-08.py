'''
aça um programa Python que peça 10 números inteiros e apresente: a média, o maior e o 
menor dentre os 10 números fornecidos.
'''
soma = 0
maior = float('-inf')
menor = float('inf')  
contador = 0

while contador < 10:
    numero = int(input("Digite um número inteiro: "))
    soma += numero
    maior = max(maior, numero)
    menor = min(menor, numero)
    contador += 1

media = soma / 10

print("Média dos números:", media)
print("Maior número:", maior)
print("Menor número:", menor)