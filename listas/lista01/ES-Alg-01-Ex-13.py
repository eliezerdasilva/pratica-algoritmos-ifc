'''
 Área de um triângulo. A área de um triângulo pode ser calculada pela fórmula abaixo, onde b 
é o comprimento de sua base e h é o comprimento de sua altura.

'''
h = float(input("Informe a altura do triângulo"))
b = float(input("Informe a base do triângulo"))

area = (b * h )/2
print("A área do triângulo é de {:.2f}".format(area))