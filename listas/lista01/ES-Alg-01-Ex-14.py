'''
No exercício anterior você criou um programa para 
calcular a área de um triângulo dados sua base e sua altura. Entretanto, também é possível 
calcular a área de um triângulo se forem conhecidos os comprimentos de seus 3 lados. Seja 
, , e  os comprimentos dos três lados
'''
import math

'''
?
'''
a = float(input("Digite o comprimento do lado a: "))
b = float(input("Digite o comprimento do lado b: "))
c = float(input("Digite o comprimento do lado c: "))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

print("A área do triângulo é {:.2f}".format(area))
