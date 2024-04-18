'''
Mediana de três valores. Escreva uma função que recebe três números como parâmetros e 
retorna o valor da mediana desses parâmetros como seu resultado. Inclua um programa 
principal que lê três valores do usuário e exibe a mediana destes valores
'''
def mediana(n1,n2,n3):
    maior  = max(n1,n2,n3)
    menor = min(n1,n2,n3)
    result = (n1+n2+n3)- maior  - menor 
    return  result

n1 = float(input("informe os valores para mediana"))
n2 = float(input("informe os valores para mediana"))
n3 = float(input("informe os valores para mediana"))
result = mediana(n1,n2,n3)
print("A mediana é ", result)