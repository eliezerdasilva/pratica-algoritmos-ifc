'''
'''
def remover_duplicatas(lista):
    lista_unicas = set()
    resultado = []
                    
    for palavra in lista:
        if palavra not in lista_unicas:
            lista_unicas.add(palavra)
            resultado.append(palavra)

    return resultado


if __name__ == "__main__":
   
    lista = []
    while True:
        palavra = input("Digite uma palavra (ou deixe em branco para sair): ")
        if palavra == "":
            break
        lista.append(palavra)


    palavras_sem_duplicatas = remover_duplicatas(lista)


    print("Palavras sem duplicatas:")
    for palavra in palavras_sem_duplicatas:
        print(palavra)
