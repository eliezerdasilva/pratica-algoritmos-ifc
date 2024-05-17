'''

'''

def divisores(n):
    lista_divisores = []
    for i in range(1, n):
        if n % i == 0:
            lista_divisores.append(i)
    return lista_divisores

def main():
    numero = int(input("Digite um número inteiro positivo: "))
    if numero < 1:
        print("Por favor, digite um número inteiro positivo.")
        return
    lista = divisores(numero)
    print("Divisores de", numero, "são:", lista)

if __name__ == "__main__":
    main()
