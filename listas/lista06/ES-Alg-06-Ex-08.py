'''
Somente palavras. Neste exercício você deve criar uma função em Python que recebe um 
texto em uma string e retorna uma lista somente com as palavras, sem espaços ou símbolos 
de pontuação. Por exemplo, se a string for: “Beleza! Este é um ótimo exemplo, você 
não acha?”, sua função deveria retornar a seguinte lista: [ “Beleza", “Este", “é", 
“um", “ótimo", "exemplo", “você", “não", “acha”]. Escreva uma função main 
que demonstre o funcionamento da sua solução

'''
import re

def extrair_palavras(texto):
    palavras = re.findall(r'\b\w+\b', texto)
    return palavras

def main():
    texto = "Beleza! Este é um ótimo exemplo, você não acha?"
    palavras = extrair_palavras(texto)
    print(palavras)

if __name__ == "__main__":
    main()
