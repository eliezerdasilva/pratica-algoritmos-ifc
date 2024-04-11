
'''
Escreva uma função Python chamada imprime_n_vezes(nome, n), que vai receber uma 
string e um numero inteiro n, e vai imprimir essa string n vezes.
'''
def imprime_n_vezes(nome,n):
    for i in range(n):
        print(nome)
n = int(input("Informe quantas vezes o nome ira repetir"))
imprime_n_vezes("Eli",n)