'''

'''
def remove_extremos(lista, n):
    if len(lista) < 4:
        print("Erro: Insira pelo menos 4 valores.")
        return lista
    sorted_lista = sorted(lista)
    print(sorted_lista)
    nova_lista = sorted_lista[n:-n]
    
    return nova_lista

def main():
    valores = [int(x) for x in input("Digite os valores separados por espaço: ").split()]
    nova_lista = remove_extremos(valores, 2)    
    print("Lista com extremos removidos:", nova_lista)
        

if __name__ == "__main__":
    main()
