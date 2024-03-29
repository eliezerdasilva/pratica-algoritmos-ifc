'''
Uma função quadrática pode ser descrita da seguinte forma: 
onde a, b e c são constantes, e a é diferente de zero. As raízes da 
função quadrática podem ser encontradas determinando-se os valores de x que satisfaçam a 
equação quadrática . Uma função quadrática pode ter 0, 1 ou 2 raízes 
reais. Essas raízes podem ser calculadas pela fórmula da Bháskara, mostrada abaixo

A parte da expressão dentro da raiz quadrada é chamada de discriminante. Se o discriminante 
for negativo, a equação não possui raízes reais. Se o discriminante for igual a zero, então a 
equação tem apenas uma raiz real. Caso contrário, a equação tem duas raízes reais e a 
expressão deve ser computada duas vezes, uma com o sinal de + e a outra com o sinal de - 
ao se calcular o numerador da fração.  
 
Escreva um programa Python que calcula as raízes reais de uma função quadrática. Seu 
programa deve iniciar solicitando ao usuário os valores de a, b e c. Então o programa deve 
exibir uma mensagem informando a quantidade de raízes reais e o(s) valor(es) da(s) raiz(es).
'''
import math


a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

delta = b**2 - 4*a*c

if delta < 0:
    print("A equação não possui raízes reais.")
elif delta == 0:
    raiz = -b / (2*a)
    print("A equação possui uma raiz real:", raiz)
else:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print("A equação possui duas raízes reais:", raiz1, "e", raiz2)
