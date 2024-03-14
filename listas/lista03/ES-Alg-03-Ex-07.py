'''
 A tabela abaixo mostra uma lista de volume sonoro em decibéis para 
diferentes tipos comuns de barulhos

Escreva um programa Python que receba do usuário um nível de volume em decibéis. Se o 
usuário entrar com um valor igual a um daqueles listados na tabela, então seu programa deve 
exibir uma mensagem informando o tipo de barulho da tabela equivalente ao valor informado. 
Se o usuário entrar um valor intermediário entre dois valores da tabela, então seu programa 
deve exibir uma mensagem informando que o nível está entre os dois barulhos (deve informar 
quais são eles). Certifique-se também que seu programa exiba mensagens apropriadas caso o 
usuário entre com valor menor que o menor valor da tabela ou maior que o maior valor
'''
volume = int(input("Informe o valor em decibéis"))
if volume == 40 or volume <= 40:
    print("Sala sileciosa ") 
elif volume == 70 :
    print("Despertador")
elif volume <70 and volume >40:
     print("Sala sileciosa e Despertador ") 
elif volume == 106 :
    print("Cortador de grama")
elif volume <106 and volume >70:
    print("Despertador e Cortador de grama")
elif volume >= 130 :
    print("Britadeira")
else :
    print("Cortador de grama e Britadeira")