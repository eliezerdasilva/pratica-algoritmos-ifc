'''

'''
def ordenar_crescente(lista):
    lista.sort()
    for num in lista:
        if num != 0:
            print(num)

numeros = []
while True:
    num = int(input("Digite um número (0 para sair): "))
    if num == 0:
        break
    numeros.append(num)

print("Números em ordem crescente:")
ordenar_crescente(numeros)
