'''
Palíndromo. Uma string é considerada um palíndromo se, de trás para frente, ela for idêntica 
à string original. Por exemplo: “arara”, “osso”, “radar”. Escreva um programa Python usando 
laço de repetição para determinar se uma palavra fornecida pelo usuário é ou não é um 
palíndromo. Seu programa deve exibir uma mensagem informando o resultado
'''
palavra = input("Digite uma palavra: ")

palavra_reversa = ""

for i in range(len(palavra) - 1, -1, -1):
    palavra_reversa += palavra[i]


if palavra == palavra_reversa:
    print(f"A palavra '{palavra}' é um palíndromo.")
else:
    print(f"A palavra '{palavra}' não é um palíndromo.")