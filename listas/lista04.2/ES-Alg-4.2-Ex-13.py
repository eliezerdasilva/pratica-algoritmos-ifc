'''

'''

n = int(input("Digite um número inteiro maior ou igual a 2: "))

if n < 2:
    print("Erro: O número deve ser maior ou igual a 2")
else:
    print("Fatores primos de", n, ":")
    fator = 2
    while fator <= n:
        if n % fator == 0:
            print(fator)
            
            n //= fator
        else:
            fator += 1
