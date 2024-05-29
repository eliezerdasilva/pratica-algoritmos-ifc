'''
Busca reversa. Escreva uma função chamada buscaReversa, que encontra todas as chaves 
de um dicionário que estão mapeadas para um determinado valor. A função deve receber 
como parâmetros um dicionário e um valor para ser buscado no dicionário. A função deve 
retornar uma lista (possivelmente vazia) com as chaves encontradas. Escreva uma função 
main para demonstrar sua função. Note que a função deve funcionar independentemente de 
ela retornar múltiplas chaves, uma única chave, ou nenhuma chave.
'''
def buscaReversa(dicionario, valor):
    chaves_encontradas = []
    for chave, val in dicionario.items():
        print(chave,val)
        if val == valor:
            chaves_encontradas.append(chave)
    return chaves_encontradas

def main():
    dicionario = {'a': 1, 'b': 2, 'c': 2, 'd': 3, 'e': 2}
    valor = 2
    chaves = buscaReversa(dicionario, valor)
    
    if chaves:
        print(f"Chaves encontradas para o valor {valor}: {chaves}")
    else:
        print(f"Nenhuma chave encontrada para o valor {valor}")

if __name__ == "__main__":
    main()
