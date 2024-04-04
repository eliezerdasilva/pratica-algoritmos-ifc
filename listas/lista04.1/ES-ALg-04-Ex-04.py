'''
Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um 
número inteiro positivo fornecido pelo usuário. 

'''

N = int(input("Digite o valor de N: ")) 

soma = 0 

# Itera de 1 até N
for i in range(1, N + 1):
    soma += 1 / i 

print("A soma da série é:", soma)
