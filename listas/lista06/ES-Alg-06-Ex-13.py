'''
Contagem de elementos. A biblioteca padrão de funções do Python possui um método
chamado count, que determina quantas vezes um determinado valor ocorre em uma lista.
Neste exercício você deve criar uma nova função chamada countRange que deve determinar
e retornar a quantidade de elementos em uma lista que são maiores ou iguais a um valor
mínimo e menores que um valor máximo. Sua função deve receber três parâmetros: a lista (de
números), o valor mínimo e o valor máximo. Ela deve retornar um valor inteiro maior ou igual a
zero. Escreva uma função main demonstrando o funcionamento de sua função.
'''
def countRange(lista, minimo, maximo):
    elemento = []
    
    for x in lista:
        if minimo <= x & x < maximo:
            elemento.append(x)
    return elemento

def main():
    numeros = [int(x) for x in input("Digite os números separados por espaço: ").split()]
    minimo = int(input("Digite o valor mínimo: "))
    maximo = int(input("Digite o valor máximo: "))
    resultado = countRange(numeros, minimo, maximo)
    print(f"Elementos entre {minimo} e {maximo}: {resultado}")

if __name__ == "__main__":
    main()
