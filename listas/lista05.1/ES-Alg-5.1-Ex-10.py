'''
 Faça uma função chamada conta_digitos(n, d) que dados um inteiro n e um inteiro d, 0 < d 
<= 9, devolve quantas vezes o dígito d aparece em n.
'''
def conta_digitos(n, d):
    dstr = str(d)
    nstr = str(n)
    contador = 0
    for digito in nstr:
        if digito == dstr:
            contador += 1
    return contador
n = int(input("Informe N"))
d = int(input("Informe D"))
ocorrencias = conta_digitos(n, d)
print(f'O dígito {d} aparece {ocorrencias} vezes em {n}.')
