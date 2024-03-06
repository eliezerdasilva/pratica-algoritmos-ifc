'''
Desenvolva um programa que obtenha do usuário um 
número inteiro de 4 dígitos e exiba a soma dos dígitos do número. Por exemplo, se o usuário 
fornecer o número 3141, então seu programa deve exibir o número 9 (3 + 1 + 4 + 1).
'''
numero = int(input("Informe um número inteiro com 4 digitos"))
primeiroDigito = numero//1000
segundoDigito = (numero%1000)//100
terceiroDigito= ((numero%1000)%100)//10
quartoDigito= ((numero%1000)%100)%10

print("A soma dos numeros é ",primeiroDigito+segundoDigito+terceiroDigito+quartoDigito)
