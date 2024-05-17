'''
Números perfeitos. Um número inteiro positivo n é chamado de número perfeito se a soma 
de todos os divisores de n é igual a n. Por exemplo, 28 é um número perfeito porque seus 
divisores são 1, 2, 4, 7 e 14; e 1+2+4+7+14=28. Escreva uma função para verificar se um 
número é perfeito. A função deve receber somente um número inteiro positivo e retornar True 
se ele for perfeito ou False caso contrário. Escreva uma função main para identificar e imprimir 
todos os números perfeitos de 1 a 10.000. Obs.: você pode usar o código do exercício anterior 
para lhe ajudar nesta tarefa
'''

def divisores(n):
    lista_divisores = []
    for i in range(1, n):
        if n % i == 0:
            lista_divisores.append(i)
    return lista_divisores

def eh_perfeito(n):
    soma_divisores = sum(divisores(n))
    return soma_divisores == n

def main():
    for i in range(1, 10001):
        if eh_perfeito(i):
            print(i, "é um número perfeito.")

if __name__ == "__main__":
    main()
