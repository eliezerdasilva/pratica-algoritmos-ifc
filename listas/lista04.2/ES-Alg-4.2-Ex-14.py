'''
Escreva um programa Python que converte um número binário (base 2) para 
decimal (base 10). Seu programa deve iniciar lendo um número binário como uma string. Então, ele 
deve computar o número decimal equivalente processando cada dígito do número binário. Finalmente 
seu programa deve exibir uma mensagem informando o número decimal calculado
'''

numero_binario = input("Digite um número binário: ")
numero_decimal = 0
for digito in numero_binario:
    numero_decimal = numero_decimal * 2 + int(digito)
print("O número decimal equivalente é:", numero_decimal)
