'''
Verificação de senha válida. Neste exercício, você deve escrever uma função que determina 
se uma senha é válida ou não. Definiremos uma boa senha como aquela que tem pelo menos 
8 caracteres e contém pelo menos uma letra maiúscula, pelo menos uma letra minúscula e 
pelo menos um número. Sua função deve retornar True se a senha passada a ela como seu 
único parâmetro for válida. Caso contrário, ele deve retornar False. Inclua um programa 
principal que lê a senha do usuário e informa se ela é ou não válida.

'''
def is_valid_password(password):
    if len(password) < 8:
        return False
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    return has_upper and has_lower and has_digit


password = input("Digite a senha: ")
if is_valid_password(password):
    print("Senha válida.")
else:
    print("Senha inválida. Certifique-se de que ela tenha pelo menos 8 caracteres, uma letra maiúscula, uma letra minúscula e um número.")
