'''
Abaixo e acima da média. Escreva um programa que leia números do usuário até que uma
linha em branco seja inserida. Seu programa deve exibir a média de todos os valores inseridos
pelo usuário. Em seguida, o programa deve exibir todos os valores abaixo da média, seguidos
por todos os valores médios (se houver), seguidos por todos os valores acima da média. Uma
mensagem apropriada deve ser exibida antes de cada lista de valores.
'''
def ler_numeros():
    numeros = []
    while True:
        entrada = input("Digite um número (ou deixe em branco para encerrar): ")
        if entrada == "":
            break
        numeros.append(float(entrada))
    return numeros

def calcular_media(numeros):
    return sum(numeros) / len(numeros) if numeros else 0

def separar_valores(numeros, media):
    abaixo_media = []
    media_valor = []
    acima_media = []

    for num in numeros:
        if num < media:
            abaixo_media.append(num)
        elif num == media:
            media_valor.append(num)
        else:
            acima_media.append(num)

    return abaixo_media, media_valor, acima_media

def main():
    numeros = ler_numeros()
    if not numeros:
        print("Nenhum número foi inserido.")
        return

    media = calcular_media(numeros)
    print("Média:", media)

    abaixo_media, media_valor, acima_media = separar_valores(numeros, media)

    print("\nValores abaixo da média:")
    print(abaixo_media if abaixo_media else "Nenhum")

    print("\nValores médios:")
    print(media_valor if media_valor else "Nenhum")

    print("\nValores acima da média:")
    print(acima_media if acima_media else "Nenhum")

if __name__ == "__main__":
    main()
