'''
Palíndromos com múltiplas palavras. O conceito de palíndromo também pode ser aplicado  
a frases, por exemplo: “A base do teto desaba”. Faça um novo programa Python que 
modifique o programa do exercício anterior para verificar se frases são palíndromos. Seu 
programa vai precisar ignorar os espaços em brando das frases. Como desafio adicional, 
amplie sua solução para que também ignore sinais de pontuação e trate letras maiúsculas e 
minúsculas como equivalentes
'''
frase = input("Digite uma frase: ")
frase_processada = ''.join(c.lower() for c in frase if c.isalnum())
palavra_reversa = ""

for i in range(len(frase_processada) - 1, -1, -1):
    palavra_reversa += frase_processada[i]


if palavra_reversa == frase_processada:
    print(f"A frase '{palavra_reversa}' é um palíndromo.")
else:
    print(f"A frase '{palavra_reversa}' não é um palíndromo.")