'''
"Tokenização" de strings. A tokenização é o processo de conversão de uma string em uma
lista de substrings, conhecidas como tokens. Em muitas circunstâncias, uma lista de tokens é
muito mais fácil de trabalhar do que a string original porque a string original pode ter
espaçamento irregular. Em alguns casos, um trabalho substancial também é necessário para
determinar onde termina um token e onde começo o próximo.
Em uma expressão matemática, os tokens são itens como operadores, números e parênteses.
Alguns tokens, como *, /, ^, ( e ) são fáceis de identificar porque o token é um único caractere
e nunca faz parte de outro token. Os símbolos + e - são um pouco mais desafiadores de tratar
porque podem representar o operador de adição ou subtração ou podem ser parte de um
token de número.
Dica: Um sinal de + ou de - é um operador se o caractere (diferente de espaço em branco)
imediatamente anterior fizer parte de um número ou se o caractere (diferente de espaço em
branco) imediatamente antes for um parêntese fechado. Caso contrário, faz parte de um
número.

'''
import re

def tokenize(expression):
    expression = re.sub(r'([+\-*/^()])', r' \1 ', expression)
    expression = ' '.join(expression.split())
    tokens = []
    number_pattern = r'-?\d+'
    for token in re.findall(r'[-+*/^()]|' + number_pattern, expression):
        tokens.append(token)

    return tokens

def main():
    expression = input("Digite uma expressão matemática: ")
    tokens = tokenize(expression)
    print("Tokens:", tokens)

if __name__ == "__main__":
    main()
