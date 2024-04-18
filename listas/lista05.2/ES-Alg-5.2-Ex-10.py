'''
Números primos. Um número inteiro positivo é primo se e somente se ele for divisível apenas 
por 1 e por ele mesmo. Escreva uma função que recebe um valor inteiro positivo e retorna 
True se ele for primo ou False se ele não for. Escreva um programa principal que leia um 
número inteiro do usuário e exiba uma mensagem indicando se ele é ou não primo.
'''
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# Programa principal
num = int(input("Digite um número inteiro positivo: "))
if is_prime(num):
    print(f"{num} é um número primo.")
else:
    print(f"{num} não é um número primo.")
