'''
Escreva uma função Python chamada quociente(x, y), que vai receber receber 2 números 
reais x e y, e vai retornar o valor da divisão de x por y
'''
def quociente(x,y):
    return x / y
x = int(input("Informe um número real X"))
y = int(input("Informe um número real Y"))
resultado = quociente(x,y)
print(resultado)