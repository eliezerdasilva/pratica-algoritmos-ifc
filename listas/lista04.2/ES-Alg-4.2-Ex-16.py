'''
Cara ou coroa. Qual é o menor número de vezes que você precisa sortear uma moeda para 
ter três resultados consecutivos iguais de cara ou de coroa? Qual é o número máximo de 
sorteios necessários? Quantos sorteios precisamos em média? Neste exercício vamos 
explorar estas questões criando um programa que simula várias séries de sorteios de cara ou 
coroa. 

Crie um programa que utilize o gerador de números randômicos do Python para simular o 
sorteio de uma moeda várias vezes. A moeda simulada deve ser justa, ou seja, deve ter a 
mesma probabilidade de gerar cara e coroa. Seu programa deve continuar simulando sorteios 
até que ocorra uma sequencia de 3 caras ou de 3 coroas consecutivas. Exiba A para cada vez 
que ocorrer cara e O para cada vez que ocorrer coroa, com todos os resultados sendo 
exibidos na mesma linha. Então exiba a quantidade de sorteios que levou para chegar a três 
resultados iguais consecutivos. Quando seu programa executar, ele deve fazer esta simulação 
10 vezes e, ao final, mostrar a quantidade média de sorteios necessária. Abaixo segue um 
exemplo de saída do programa

A O O O (4 sorteios) 
A A O O A O A O O A A O A O O A O O O (19 sorteios) 
O O O (3 sorteios) 
O A A A (4 sorteios) 
A A A (3 sorteios) 
O A O O A O A A O O A A O A O A A A (18 sorteios) 
A O O A A A (6 sorteios) 
A O A A A (5 sorteios) 
O O A O O A O A O A A A (12 sorteios) 
O A O O O (5 sorteios) 
Na média, foram necessários 7.9 sorteios
'''
import random

# Lista para armazenar o número de sorteios em cada simulação
num_sorteios_lista = []

# Realizar 10 simulações
for _ in range(10):
    # Inicializar contadores para cada simulação
    sorteios = 0
    sequencia_atual = 0
    resultados = []

    # Enquanto não tivermos uma sequência de 3 resultados iguais consecutivos
    while sequencia_atual < 3:
        # Sortear cara (A) ou coroa (O)
        resultado = random.choice(["A", "O"])
        resultados.append(resultado)

        # Atualizar a sequência atual
        if len(resultados) >= 2 and resultados[-1] == resultados[-2]:
            sequencia_atual += 1
        else:
            sequencia_atual = 0

        # Incrementar o número de sorteios
        sorteios += 1

    # Exibir os resultados e adicionar o número de sorteios à lista
    print(" ".join(resultados), f"({sorteios} sorteios)")
    num_sorteios_lista.append(sorteios)

# Calcular a média de sorteios necessários
media_sorteios = sum(num_sorteios_lista) / len(num_sorteios_lista)

# Exibir a média de sorteios necessários
print(f"Na média, foram necessários {media_sorteios:.1f} sorteios")
