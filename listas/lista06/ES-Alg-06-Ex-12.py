'''
A lista está ordenada? Escreva uma função que determina se uma lista de valores está ou
não em ordem de classificação (crescente ou decrescente). A função deve receber a lista
como parâmetro e retornar True se a lista já estiver classificada. Caso contrário, ele deve
retornar False. Escreva um programa principal que leia uma lista de números do usuário e use
sua função para relatar se a lista é classificada.
'''
def esta_ordenada(lista, crescente=True):
    if crescente:
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
               
                return False
    else:
        for i in range(len(lista) - 1):
            if lista[i] < lista[i + 1]:
               
                return False
    return True

numeros = [int(x) for x in input("Digite os números separados por espaço: ").split()]

if esta_ordenada(numeros, crescente=True):
    print("A lista está ordenada de forma crescente.")
elif esta_ordenada(numeros, crescente=False):
    print("A lista está ordenada de forma decrescente.")
else:
    print("A lista não está ordenada.")

