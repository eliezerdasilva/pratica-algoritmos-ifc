'''
Conversão arbitrária de base numérica. Escreva um programa que permita ao usuário 
converter um número de uma base para base 10 e vice-versa. Seu programa deve suportar 
bases entre 2 (binário) e 16 (hexadecimal) para o número de entrada e o número de resultado. 
Divida seu programa em várias funções, incluindo uma função que converte de uma base 
arbitrária em uma base 10, uma função que converte de uma base 10 em uma base arbitrária. 
A primeira função deve receber como parâmetros uma string com o número a ser convertido 
para base 10, e o valor da base deste número (portanto, de 2 a 16) e deve retornar como 
resultado o número convertido na base 10. A segunda função deve receber como parâmetros 
um numero na base 10 e a base para qual queremos converter o número. Como resultado, a 
função deve retornar uma string com o número convertido. Além disso, faça um programa 
principal que lê as bases e o número de entrada do usuário. Você pode encontrar parte da 
solução deste problema no exercício anterior e nos exercícios 14 e 15 da lista 4
'''

def convert_to_base_10(number, base):
   
    decimal = 0
    power = len(number) - 1
    for digit in number:
        decimal += int(digit, base) * (base ** power)
        power -= 1
    return decimal


def convert_from_base_10(decimal, base):

    result = ""
    while decimal > 0:
        remainder = decimal % base
        result = str(remainder) + result
        decimal //= base
    return result


try:
    base_from = int(input("Digite a base do número de entrada (entre 2 e 16): "))
    if base_from < 2 or base_from > 16:
        raise ValueError("Base inválida")
    number = input("Digite o número a ser convertido: ")
    base_to = int(input("Digite a base para a qual deseja converter (entre 2 e 16): "))
    if base_to < 2 or base_to > 16:
        raise ValueError("Base inválida")
       
    decimal_number = convert_to_base_10(number, base_from)
    result = convert_from_base_10(decimal_number, base_to)
        
    print("Resultado da conversão:", result)
except ValueError as ve:
    print("Erro:", ve)


