'''
Cartela de bingo. Uma cartela de bingo é formada por 5 linhas e 5 colunas. As colunas são 
rotuladas com as letras B, I, N, G e O. Existem 15 números diferentes que podem aparecer 
abaixo de cada letra. Abaixo do B podem aparecer os números de 1 a 15; abaixo do I os 
números de 16 a 30, abaixo do N os números de 31 a 45 e assim por diante. Escreva uma 
função que cria uma cartela de bingo e a armazena em um dicionário. As chaves do dicionário 
são as letras  B, I, N, G e O. Os valores devem ser listas de 5 números cada, que aparecem 
abaixo de cada letra na cartela. A função deve retornar o dicionário. Escreva uma segunda 
função que recebe o dicionário e exibe a cartela de bingo com as colunas rotuladas 
apropriadamente. Escreva um programa main que gere e exiba uma cartela de bingo usando 
suas funções

'''
import random

def criar_cartela_bingo():
    cartela = {
        'B': random.sample(range(1, 16), 5),
        'I': random.sample(range(16, 30), 5),
        'N': random.sample(range(31, 45), 5),
        'G': random.sample(range(46, 60), 5),
        'O': random.sample(range(61, 75), 5)
    }
    return cartela

def exibir_cartela_bingo(cartela):
    print(" B   I   N   G   O")
    for i in range(5):
        for letra in 'BINGO':
            print(f"{cartela[letra][i]:2}", end="  ")
        print()

def main():
    cartela = criar_cartela_bingo()
    exibir_cartela_bingo(cartela)

if __name__ == "__main__":
    main()
