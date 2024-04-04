'''
Escreva um programa Python que imprima a seguinte seqüência de números inteiros: 100, 95, 
90, 85, 80... etc até no mínimo o número 0
'''
numero = 100  # Inicializa o número como 100

# Enquanto o número for maior ou igual a 0, imprime-o e decrementa-o
while numero >= 0:
    print(numero)
    numero -= 5  # Decrementa o número em 5
