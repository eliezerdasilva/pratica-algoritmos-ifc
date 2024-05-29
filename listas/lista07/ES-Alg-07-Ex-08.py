'''
Jogo de Bingo. Neste exercício você vai simular o jogo de Bingo para apenas uma cartela. 
Começa gerando uma lista de todas as chamadas válidas de bingo (B1 até O75). Depois que 
a lista estiver pronta, você pode embaralhar seus elementos chamando a função shuffle do 
módulo random do Python. Então seu programa deve ir utilizando os valores da lista para 
anunciar os números sorteados e zerar os números correspondentes na cartela até que ela 
contenha uma linha, coluna ou diagonal zerada. No seu programa principal, faça uma 
simulação de 1.000 partidas (sempre com uma nova cartela) e mostre o número mínimo, o 
máximo e a média de chamadas até que se tenha uma cartela vencedora. Utilize seu código 
dos dois exercícios anteriores e não se esqueça de criar novas funções sempre que você 
identificar algum procedimento que pode ser melhor organizado dentro de uma função

'''
import random

def criar_cartela_bingo():
    cartela = {
        'B': random.sample(range(1, 16), 5),
        'I': random.sample(range(16, 31), 5),
        'N': random.sample(range(31, 46), 5),
        'G': random.sample(range(46, 61), 5),
        'O': random.sample(range(61, 76), 5)
    }
    return cartela

def exibir_cartela(cartela):
    print(" B   I   N   G   O")
    for i in range(5):
        print(f"{cartela['B'][i]:2} {cartela['I'][i]:3} {cartela['N'][i]:3} {cartela['G'][i]:3} {cartela['O'][i]:3}")

def marcar_numero(cartela, numero):
    for coluna in cartela:
        if numero in cartela[coluna]:
            cartela[coluna][cartela[coluna].index(numero)] = 0

def cartela_vencedora(cartela):
    # Verificar linhas
    for i in range(5):
        if sum(cartela['B'][i], cartela['I'][i], cartela['N'][i], cartela['G'][i], cartela['O'][i]) == 0:
            return True
    
    # Verificar colunas
    for coluna in cartela:
        if sum(cartela[coluna]) == 0:
            return True
    
    # Verificar diagonais
    if sum(cartela['B'][0], cartela['I'][1], cartela['N'][2], cartela['G'][3], cartela['O'][4]) == 0:
        return True
    if sum(cartela['B'][4], cartela['I'][3], cartela['N'][2], cartela['G'][1], cartela['O'][0]) == 0:
        return True
    
    return False

def main():
    # Gerar e exibir cartelas de exemplo
    print("Cartela 1 (Linha Horizontal Vencedora):")
    cartela1 = criar_cartela_bingo()
    for i in range(5):
        marcar_numero(cartela1, cartela1['B'][i])
        marcar_numero(cartela1, cartela1['I'][i])
        marcar_numero(cartela1, cartela1['N'][i])
        marcar_numero(cartela1, cartela1['G'][i])
        marcar_numero(cartela1, cartela1['O'][i])
    exibir_cartela(cartela1)
    print("Vencedora?" , cartela_vencedora(cartela1))
    print()

    print("Cartela 2 (Coluna Vertical Vencedora):")
    cartela2 = criar_cartela_bingo()
    for coluna in cartela2:
        for i in range(5):
            marcar_numero(cartela2, cartela2[coluna][i])
    exibir_cartela(cartela2)
    print("Vencedora?" , cartela_vencedora(cartela2))
    print()

    print("Cartela 3 (Diagonal Vencedora):")
    cartela3 = criar_cartela_bingo()
    for i in range(5):
        marcar_numero(cartela3, cartela3[list(cartela3.keys())[i]][i])
    exibir_cartela(cartela3)
    print("Vencedora?" , cartela_vencedora(cartela3))
    print()

    print("Cartela 4 (Não Vencedora):")
    cartela4 = criar_cartela_bingo()
    marcar_numero(cartela4, cartela4['B'][0])
    marcar_numero(cartela4, cartela4['I'][1])
    marcar_numero(cartela4, cartela4['N'][2])
    marcar_numero(cartela4, cartela4['G'][3])
    marcar_numero(cartela4, cartela4['O'][4])
    exibir_cartela(cartela4)
    print("Vencedora?" , cartela_vencedora(cartela4))
    print()

if __name__ == "__main__":
    main()
