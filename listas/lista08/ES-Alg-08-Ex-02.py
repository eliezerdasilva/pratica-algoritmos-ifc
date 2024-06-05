'''

'''
def fibonacci(n, memo={0: 0, 1: 1}):
    if n < 0:
        raise ValueError("O índice de Fibonacci não pode ser negativo.")
    if n not in memo:
        memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

while True:
    try:
        n = int(input("Digite um número inteiro não negativo: "))
        if n < 0:
            raise ValueError("O número deve ser não negativo.")
        break
    except ValueError as e:
        print(f"Entrada inválida: {e}. Por favor, tente novamente.")
    
resultado = fibonacci(n)
print(f"O {n}º termo da sequência de Fibonacci é: {resultado}")

