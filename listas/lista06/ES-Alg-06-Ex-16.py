'''
'''
def infix_to_postfix(tokens):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    operator_stack = []

    postfix_expression = []

    def get_precedence(operator):
        return precedence.get(operator, 0)

    for token in tokens:
        if token.isdigit():
            postfix_expression.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                postfix_expression.append(operator_stack.pop())
            operator_stack.pop() 
        else:
            while operator_stack and get_precedence(operator_stack[-1]) >= get_precedence(token):
                postfix_expression.append(operator_stack.pop())
            operator_stack.append(token)

    while operator_stack:
        postfix_expression.append(operator_stack.pop())

    return postfix_expression

def main():
    infix_expression = input("Digite uma expressão infixa: ")
    tokens = infix_expression.split()
    postfix_expression = infix_to_postfix(tokens)
    print("Expressão pós-fixa:", ' '.join(postfix_expression))

if __name__ == "__main__":
    main()
