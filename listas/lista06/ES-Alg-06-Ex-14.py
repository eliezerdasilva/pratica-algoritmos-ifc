'''
14. Precedência de operadores. Escreva uma função chamada precedencia que retorna um
inteiro representando a precedência de um operador matemático. Uma string contendo o
operador será passada para a função como seu único parâmetro. Sua função deve retornar 1
para + e -, 2 para * e / e 3 para ^. Se a string passada para a função não for um desses
operadores, a função deve retornar -1. Inclua um programa principal que lê um operador do
usuário e exibe a precedência do operador ou uma mensagem de erro indicando que a
entrada não era um operador.
'''
def precedencia(operador):
    if operador in ['+', '-']:
        return 1
    elif operador in ['*', '/']:
        return 2
    elif operador == '^':
        return 3
    else:
        return -1

def main():
    operador = input("Digite um operador matemático (+, -, *, /, ^): ")
    result = precedencia(operador)
    
    if result != -1:
        print(f"A precedência do operador {operador} é {result}.")
    else:
        print("Entrada inválida. Por favor, insira um operador válido.")

if __name__ == "__main__":
    main()
