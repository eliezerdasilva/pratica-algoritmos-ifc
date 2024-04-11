'''
Escreva uma função Python chamada quadrado(x), que vai receber receber um número real 
x, e vai retornar o valor de x ao quadrado
'''
def quadrado(x):
    return x**2

x = int(input("Informe um numero real"))
resultado = quadrado(x)
print(resultado)