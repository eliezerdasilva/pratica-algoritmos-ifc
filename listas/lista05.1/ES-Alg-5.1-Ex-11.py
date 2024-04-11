'''
Usando a função do item anterior, faça um programa que lê dois inteiros positivos a e b e 
responda se a é permutação de b

Um número a é dito permutação de um número b se os dígitos de a formam uma permutação 
dos dígitos de b. 
Exemplo: 5412434 é uma permutação de 4321445, mas não é uma permutação de 4312455.  
Obs.: Considere que o dígito 0 (zero) não aparece nos números.
'''
def conta_digitos(n, d):
    count = 0
    for digit in str(n):
        if int(digit) == d:
            count += 1
    return count

def eh_permutacao(a, b):
    if len(str(a)) != len(str(b)):
        return False
    
    for digit in range(1, 10):
        if conta_digitos(a, digit) != conta_digitos(b, digit):
            return False
    
    return True

a = int(input("Digite o número a: "))
b = int(input("Digite o número b: "))

if eh_permutacao(a, b):
    print(f"{a} é uma permutação de {b}.")
else:
    print(f"{a} não é uma permutação de {b}.")
