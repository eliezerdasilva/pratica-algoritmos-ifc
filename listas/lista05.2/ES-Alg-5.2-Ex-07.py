'''
Triângulo válido? Se você possui 3 canudos, possivelmente de tamanhos diferentes, pode ou 
não ser possível montar um triângulo juntando as pontas dos canudos. Por exemplo, se todos 
tiverem 15 cm de comprimento, facilmente você pode formar um triângulo equilátero. Porém, 
se um canudo tem 15 cm e os outros dois tem 5 cm cada, você não consegue formar o 
triângulo. Generalizando: se o comprimento de um canudo é maior ou igual que a soma dos 
comprimentos dos outros dois outros canudos, eles não podem formar um triângulo. Caso 
contrário, podem formar um triângulo. Escreva uma função que determina se 3 comprimentos 
podem ou não formar um triângulo. A função deve receber 3 parâmetros e retornar um valor 
lógico. Além disso, escreva um programa que leia 3 valores do usuário e demonstre o 
comportamento desta função.

'''
def eh_triangulo(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True

a = float(input("Informe o comprimento do primeiro canudo: "))
b = float(input("Informe o comprimento do segundo canudo: "))
c = float(input("Informe o comprimento do terceiro canudo: "))

if eh_triangulo(a, b, c):
    print("É possível formar um triângulo com os comprimentos fornecidos.")
else:
    print("Não é possível formar um triângulo com os comprimentos fornecidos.")
