'''
Adapte seu programa da questão anterior para que ele receba uma quantidade indefinida de 
notas até que o usuário pressione <enter> sem fornecer nenhuma nota

'''
soma = 0
maior = float('-inf') 
menor = float('inf')  
contador = 0

while True:
    x  = input("Digite um número inteiro: ")
    
    if x == "":
        break
    numero = int(x)
    soma += numero
    maior = max(maior, numero)
    menor = min(menor, numero)
    contador += 1

media = soma / contador

print("Média dos números:", media)
print("Maior número:", maior)
print("Menor número:", menor)
