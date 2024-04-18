'''

Escreva uma função que recebe como parâmetros os comprimentos dos dois 
lados menores de um triângulo retângulo. A função deve retornar como resultado o 
comprimento da hipotenusa, calculado com o Teorema de Pitágoras. Inclua um programa 
principal (função main) que solicite ao usuário os comprimentos dos lados, utilize sua função 
para calcular a hipotenusa e imprima o resultado
'''

import math
def hipotenusa(l1, l2):
    hp = 0
    hp = l1**2 + l2**2
    return math.sqrt(hp)
result = 0
l1 = int(input("Informe um dos lados menores que a hipotenusa"))    
l2 = int(input("Informe um dos lados menores que a hipotenusa"))    
result= hipotenusa(l1,l2)
print("A hipotenusa é : ",result)