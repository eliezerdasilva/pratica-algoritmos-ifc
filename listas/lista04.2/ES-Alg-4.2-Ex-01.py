'''
Escreva um programa Python que calcula a média aritmética de um 
conjunto de valores fornecidos pelo usuário. O usuário deve entrar com o valor 0 indicando 
que não serão mais fornecidos novos valores. Seu programa deve exibir uma mensagem de 
erro se o primeiro valor fornecido pelo usuário for 0.

'''

x =0
y =0 
while True:
     numero = input("Informe Um numero")
     if numero == "0":
         break
     x += float(numero)
     y += 1

print("média aritmética é de {:.2f}".format(x / y))