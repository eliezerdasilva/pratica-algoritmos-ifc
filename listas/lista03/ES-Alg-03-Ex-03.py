'''
Escreva um programa Python que peça para o usuário uma letra do 
alfabeto. Se o usuário entrar com as letras a, e, i, o ou u, o programa deve exibir uma 
mensagem dizendo que a letra é uma vogal. Caso contrário, o programa deve exibir a 
mensagem informando que a letra é uma consoante
'''
letra = input("Informe uma letra")
if "a"==letra or "e"==letra or "i"==letra or "o"==letra or "u"==letra:
    print("Vogal")
else:
    print("Consoante")
