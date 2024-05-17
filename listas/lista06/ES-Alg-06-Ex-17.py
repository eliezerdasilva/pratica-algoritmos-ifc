'''

'''
def tokenize_expression(expression):
    tokens = []
    current_token = ''

    for char in expression:
        if char.isdigit() or char in '+-*/^()':
            if current_token and current_token.isdigit() and char.isdigit():
                current_token += char
            else:
                if current_token:
                    tokens.append(current_token)
                current_token = char
        elif char != ' ':
            raise ValueError("Caractere inválido na expressão: {}".format(char))

    if current_token:
        tokens.append(current_token)

    return tokens


def infix_to_postfix(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    operators = []
    postfix = []

    for token in tokens:
        if token.isdigit():
            postfix.append(token)
        elif token in '+-*/^':
            while operators and operators[-1] != '(' and precedence.get(token, 0) <= precedence.get(operators[-1], 0):
                postfix.append(operators.pop())
            operators.append(token)
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators[-1] != '(':
                postfix.append(operators.pop())
            operators.pop()

    while operators:
        postfix.append(operators.pop())

    return postfix


def main():
    expression = input("Digite uma expressão infixa: ")
    try:
        tokens = tokenize_expression(expression)
        postfix = infix_to_postfix(tokens)
        print("Expressão pós-fixa:", ' '.join(postfix))
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
