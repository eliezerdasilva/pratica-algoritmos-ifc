'''
Faça um programa Python que calcule os quadrados e cubos dos números de 0 a 10 e 
imprima os valores resultantes no formato de tabela, como segue:
'''
for numero in range(11):
    quadrado = numero ** 2
    cubo = numero ** 3
    print(f"{numero:6} | {quadrado:8} | {cubo:5}")