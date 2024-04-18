'''
Números ordinais. Palavras como primeiro, segundo e terceiro são chamadas de números 
ordinais. Neste exercício, você deve escrever uma função que recebe um inteiro como seu 
único parâmetro e retorna uma string contendo o número ordinal em português como seu 
único resultado. Sua função deve lidar com números inteiros entre 1 e 12 (inclusive). Ela deve 
retornar uma string vazia se um valor fora desse intervalo for fornecido como um parâmetro. 
Inclua um programa principal que demonstra sua função exibindo cada inteiro de 1 a 12 e seu 
respectivo número ordinal.
'''

def numero_ordinal(numero):
    if numero == 1:
        return "primeiro"
    elif numero == 2:
        return "segundo"
    elif numero == 3:
        return "terceiro"
    elif numero == 4:
        return "quarto"
    elif numero == 5:
        return "quinto"
    elif numero == 6:
        return "sexto"
    elif numero == 7:
        return "sétimo"
    elif numero == 8:
        return "oitavo"
    elif numero == 9:
        return "nono"
    elif numero == 10:
        return "décimo"
    elif numero == 11:
        return "undécimo"
    elif numero == 12:
        return "décimo segundo"
    else:
        return ""

ordinais = int(input("Informe um número de 1 a 12"))
result = numero_ordinal(ordinais)
print(f"O número {ordinais} em ordinal é {result}")


