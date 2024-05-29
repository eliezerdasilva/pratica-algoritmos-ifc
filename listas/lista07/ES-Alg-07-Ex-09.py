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
        if sum([cartela['B'][i], cartela['I'][i], cartela['N'][i], cartela['G'][i], cartela['O'][i]]) == 0:
            return True
    
    # Verificar colunas
    for coluna in cartela:
        if sum(cartela[coluna]) == 0:
            return True
    
    # Verificar diagonais
    if sum([cartela['B'][0], cartela['I'][1], cartela['N'][2], cartela['G'][3], cartela['O'][4]]) == 0:
        return True
    if sum([cartela['B'][4], cartela['I'][3], cartela['N'][2], cartela['G'][1], cartela['O'][0]]) == 0:
        return True
    
    return False

def gerar_chamadas_bingo():
    chamadas = []
    for letra, inicio in zip("BINGO", range(1, 76, 15)):
        chamadas.extend([f"{letra}{i}" for i in range(inicio, inicio + 15)])
    random.shuffle(chamadas)
    return chamadas

def jogar_bingo():
    cartela = criar_cartela_bingo()
    chamadas = gerar_chamadas_bingo()
    chamadas_realizadas = 0

    for chamada in chamadas:
        letra = chamada[0]
        numero = int(chamada[1:])
        marcar_numero(cartela, numero)
        chamadas_realizadas += 1
        if cartela_vencedora(cartela):
            break
    
    return chamadas_realizadas

def simular_partidas(num_partidas=1000):
    resultados = [jogar_bingo() for _ in range(num_partidas)]
    minimo = min(resultados)
    maximo = max(resultados)
    media = sum(resultados) / num_partidas
    return minimo, maximo, media

def main():
    minimo, maximo, media = simular_partidas()
    print(f"Mínimo de chamadas para vencer: {minimo}")
    print(f"Máximo de chamadas para vencer: {maximo}")
    print(f"Média de chamadas para vencer: {media:.2f}")

if __name__ == "__main__":
    main()

