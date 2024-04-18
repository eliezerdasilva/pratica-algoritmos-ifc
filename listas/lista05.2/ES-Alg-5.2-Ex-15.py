'''
Dígitos hexadecimais e decimais. Escreva duas funções chamadas hex2int e int2hex, que 
devem fazer a conversão entre dígitos hexadecimais (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E e 
F) e números inteiros de base 10 . A função hex2int é responsável por converter uma string 
contendo um único dígito hexadecimal em um inteiro de base 10, enquanto a função int2hex 
é responsável por converter um inteiro entre 0 e 15 em um único dígito hexadecimal. Cada 
função pegará o valor a ser convertido como seu único parâmetro e retornará o valor 
convertido como o único resultado da função. Certifique-se de que a função hex2int funcione 
corretamente para letras maiúsculas e minúsculas. Observação: se você não sabe como 
converter números entre bases diferentes, veja o quadro explicativo ao final da lista de 
exercícios
'''

def hex2int(hex_digit):
   
    hex_digit = hex_digit.upper() 
    if hex_digit.isdigit():  
        return int(hex_digit)
    elif hex_digit >= 'A' and hex_digit <= 'F':
        return ord(hex_digit) - ord('A') + 10
    else:
        return None 


def int2hex(integer):
    if integer >= 0 and integer <= 9:  
        return str(integer)
    elif integer >= 10 and integer <= 15:
        return chr(integer - 10 + ord('A'))
    else:
        return None  


hex_digit = input("Digite um dígito hexadecimal: ")
print("O valor em decimal é:", hex2int(hex_digit))

integer = int(input("Digite um número inteiro entre 0 e 15: "))
print("O valor em hexadecimal é:", int2hex(integer))
