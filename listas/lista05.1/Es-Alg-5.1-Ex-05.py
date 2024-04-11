'''
Escreva uma função Python chamada potencia(x, y), que vai receber receber 2 números 
reais x e y, e vai retornar o valor de x elevado a y. Obs.: faça a operação de potenciação 
usando laço de repetição com comandos for ou while. 
'''
def potencia(x, y):
    resultado = 1
    for _ in range(y):
        resultado *= x
    return resultado

x = int(input("Informe um número real X: "))
y = int(input("Informe um número real Y: "))
resultado = potencia(x, y)
print(resultado)
