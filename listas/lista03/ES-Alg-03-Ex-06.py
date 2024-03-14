'''
Baseado nos comprimentos dos seus lados, um triângulo pode ser 
classificado como equilátero (quando os três lados tem o mesmo tamanho), isósceles (quando 
apenas dois lados são iguais) ou escaleno (quando os três lados são diferentes). Escreva um 
programa Python que recebe do usuário os comprimentos dos 3 lados de um triângulo e exiba 
uma mensagem informando qual é o tipo do triângulo
'''
lado1 = float(input("Informe o comprimento do primeiro lado: "))
lado2 = float(input("Informe o comprimento do segundo lado: "))
lado3 = float(input("Informe o comprimento do terceiro lado: "))

if lado1 == lado2 == lado3 :
    print("Equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Isósceles")
else:   
    print("Escaleno")