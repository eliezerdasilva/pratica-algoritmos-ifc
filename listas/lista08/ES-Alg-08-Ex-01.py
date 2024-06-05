'''

'''
def fatorial(n):
    # Verificação para garantir que n é um número inteiro positivo
    if n < 0:
        raise ValueError("O fatorial não é definido para números negativos.")
    # Caso base: 1! = 1
    if n == 0 or n == 1:
        return 1
    # Passo recursivo: n! = n * (n-1)!
    return n * fatorial(n - 1)

# Testes
print(fatorial(1))  # Saída: 1
print(fatorial(5))  # Saída: 120
print(fatorial(7))  # Saída: 5040
print(fatorial(10))  # Saída: 3628800
