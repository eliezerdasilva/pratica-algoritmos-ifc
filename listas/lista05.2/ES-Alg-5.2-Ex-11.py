'''
Senha aleatória. Escreva uma função que gere uma senha aleatória. A senha deve ter um 
comprimento aleatório de 7 a 10 caracteres. Cada caractere deve ser selecionado 
aleatoriamente das posições 33 a 126 na tabela ASCII. Sua função não receberá nenhum 
parâmetro. Ele retornará a senha gerada aleatoriamente como seu único resultado. Exiba a 
senha gerada aleatoriamente no programa principal do seu arquivo fonte
'''
import random

def generate_random_password():
    length = random.randint(7, 10)
    password = ''
    for _ in range(length):
        char = chr(random.randint(33, 126))
        password += char
    return password

random_password = generate_random_password()
print("Senha aleatória gerada:", random_password)
