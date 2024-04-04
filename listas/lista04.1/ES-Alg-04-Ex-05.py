'''
Faça um programa Python que calcule o valor de A, dado pela expressão abaixo, onde N é um 
número inteiro positivo fornecido pelo usuário.
'''
N = int(input("Digite o valor de N: "))  

soma = 0  


for i in range(N, 0, -1):
     soma += i / (N - i + 1)
     print("A soma da série é:", soma, i)
