''' 
Área e volume. Escreva um programa Python que começa lendo o valor de um raio r, 
fornecido pelo usuário. O programa deve continuar calculando e exibindo a área de um círculo 
de raio r, e o volume de uma esfera de raio r. Utilize a constante pi do módulo math nos seus 
cálculos. 

'''
import math
raio = float(input("Informe o tamanho do Raio"))
area  = math.pi * raio ** 2
volume = (math.pi * raio ** 3 * 4)/3
print("A área da esfera é de {:.2f}. O volume é de {:.2f}".format(area, volume))
