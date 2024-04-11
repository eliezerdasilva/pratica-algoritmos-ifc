'''
Faça uma função que recebe um número inteiro n>0 e devolve o número de dígitos de n.
'''
def contar_digitos(n):
    
    return len(str(n))


numero = int(input("Informe um numero real"))
if numero > 0 and type(numero)!= str:
    num_digitos = contar_digitos(numero)
    print("Número de dígitos:", num_digitos)
else:
    print("Erro")