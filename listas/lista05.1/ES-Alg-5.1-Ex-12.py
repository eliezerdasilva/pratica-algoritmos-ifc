'''
Construa uma função chamada "encaixa" que, dados dois inteiros positivos a e b, verifica se b 
corresponde aos últimos dígitos de a. 
Exemplos: 
a  b 
567890  890  => encaixa 
1243  1243  => encaixa 
2457  245 => não encaixa 
457  2457 => não encaixa
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

def verifica_segmento(a, b):
    if eh_segmento(a, b):
        print(f"{b} é segmento de {a}")
    elif eh_segmento(b, a):
        print(f"{a} é segmento de {b}")
    else:
        print("Um não é segmento do outro")


a = int(input("Informe o primeiro número positivo: "))
b = int(input("Informe o segundo número positivo: "))


verifica_segmento(a, b)

