'''
Formatando uma lista. Quando escrevemos uma lista em português, geralmente separamos
os itens por vírgula e colocamos a conjunção “e" entre os dois últimos itens, a não ser que a
lista só tenha um item. Considere as listas abaixo:
maçãs
maçãs e laranjas
maçãs, laranjas e bananas
maçãs, laranjas, bananas e limões
Escreva uma função que receba como parâmetro uma lista de strings e retorne uma única
string contendo todos os itens da lista formatados conforme mostrado acima. Apesar dos
exemplos acima terem no máximo 4 itens, sua função deve se comportar corretamente para
listas de qualquer tamanho. Escreva uma função main demonstrando o funcionamento de sua
função.
'''
def formatar_lista(lista):
    tamanho = len(lista)
    print(tamanho)
    if tamanho == 0:
        return ''
    elif tamanho == 1:
        return lista[0]
    elif tamanho == 2:
        return ' e '.join(lista)
    else:
        return ', '.join(lista[:-1]) + ' e ' + lista[-1]

def main():
    lista = []
    elemento = input("Digite um elemento da lista (ou deixe em branco para terminar): ")
    while elemento:
        lista.append(elemento)
        elemento = input("Digite um elemento da lista (ou deixe em branco para terminar): ")

    print("Lista formatada:", formatar_lista(lista))

if __name__ == "__main__":
    main()
