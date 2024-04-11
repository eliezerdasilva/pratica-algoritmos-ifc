'''
Usando a função do exercício anterior, faça um programa que lê dois inteiros positivos a e b e 
verifica se o menor deles é segmento do outro
'''
def encaixa(a, b):
    str_a = str(a)
    str_b = str(b)
    letB = len(str_b)
    if len(str_a) < letB:
        return False
    for i in range(letB):
        if str_a[-(i + 1)] != str_b[-(i + 1)]:
            return False
    return True

def eh_segmento(a, b):
    if a < b:
        return encaixa(b, a)
    else:
        return encaixa(a, b)

# Função para verificar se um número é segmento do outro
def verifica_segmento(a, b):
    if eh_segmento(b, a):
        print(f"{b} é segmento de {a}")
    elif eh_segmento(a, b):
        print(f"{a} é segmento de {b}")
    else:
        print("Um não é segmento do outro")

# Leitura dos números a e b
a = int(input("Informe o primeiro número positivo: "))
b = int(input("Informe o segundo número positivo: "))

# Verifica se um número é segmento do outro
verifica_segmento(a, b)
