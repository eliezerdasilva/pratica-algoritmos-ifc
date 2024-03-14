'''
Escreva um programa Python que recebe do usuário um número inteiro. Seu 
programa deve então exibir uma mensagem indicando se o número fornecido é par ou ímpar.
'''
numero = int(input("informe um número inteiro "))
if(numero%2==0):
    resposta = 'par'
else: 
    resposta = 'impar'

print(resposta)