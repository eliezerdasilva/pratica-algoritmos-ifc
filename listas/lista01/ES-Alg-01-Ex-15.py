''' Um polígono é regular se seus lados são todos do mesmo 
tamanho e os ângulos entre lados adjacentes são todos iguais. A área de um polígono regular 
pode ser calculada pela fórmula abaixo onde l é o comprimento de um lado e n é o número de 
lados
'''
import math
comprimento = float(input("Informe o comprimento do polígono "))
nLados = float(input("Informe a quantidade de lados do polígono"))

area = (nLados * comprimento**2)/(4* math.tan(math.pi/nLados))
print("A área do polígono é de {:.2f}".format(area))
