'''
Raiz quadrada. Escreva um programa Python que implemente o método de Newton para 
calcular e exibir o valor da raiz quadrada de um número. O método de Newton é descrito pelo 
pseudo-código abaixo: 
 
Leia o valor de x do usuário 
Inicialize raiz = x/2 
Enquanto raiz não é boa o suficiente, faça 
       Atualize raiz para receber a média entre raiz e x/raiz 
 
Quando o algoritmo chega ao fim, raiz contém um valor aproximado da raiz quadrada de x. A 
qualidade desta aproximação depende de como você define “boa o suficiente”. Podemos, por 
exemplo, considerar a solução boa o suficiente quando o valor absoluto da diferença entre  
raiz * raiz e x é menor que
'''
x = float(input("Digite um número para calcular a raiz quadrada: "))
raiz = x / 2
    
while abs(raiz * raiz - x) > 1e-12:
    raiz = (raiz + x / raiz) / 2
print("A raiz quadrada de", x, "é aproximadamente", raiz)