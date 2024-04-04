'''
. Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um 
número inteiro positivo fornecido pelo usuário.  
'''
N = int(input("Digite o valor de N: "))

A = 0
for i in range(1, 2*N, 2):
    A += 1 / i

print("O valor de A é: {:.2f}".format(A))
