'''
Letras maiúsculas. Muitas pessoas não usam letras maiúsculas corretamente, especialmente 
ao digitar em smartphones. Neste exercício, você escreverá uma função que coloca em 
maiúscula os caracteres apropriados em uma string. O primeiro caractere da string deve ser 
convertido em letra maiúscula, assim como o primeiro caractere (que não seja espaço) após 
um “.”, “!” ou "?". Por exemplo, se a função for fornecida com a string “que horas eu tenho que 
estar lá? qual é o endereço?" então ele deve retornar a string “Que horas eu tenho que estar 
lá? Qual é o endereço?". Inclua um programa principal que leia uma string do usuário, corrige 
as letras maiúsculas usando sua função e exibe o resultado
'''
def corrige_maiusculas(frase):
    frase_corrigida = ''
    maiuscula = True
    
    for char in frase:
        if maiuscula and char.isalpha():
            frase_corrigida += char.upper()
            maiuscula = False
        else:
            frase_corrigida += char
        
        if char in ['.', '!', '?']:
            maiuscula = True
    
    return frase_corrigida


frase = input("Digite uma frase: ")
frase_corrigida = corrige_maiusculas(frase)
print("Frase corrigida:", frase_corrigida)
