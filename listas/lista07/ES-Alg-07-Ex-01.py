'''
Caracteres únicos. Escreva uma função Python para verificar se uma string possui 
caracteres únicos. Por exemplo, a string “azul" não repete letras, mas a string 
“ferramenta"possui letras repetidas. A função deve receber uma string e retornar True no 
primeiro caso (letras únicas) ou False caso contrário (letras repetidas). Você deve usar 
conjuntos para implementar a função
'''
def caracteres_unicos(string):
    return len(set(string)) == len(string)

def main():
    string = input("Digite uma string: ")
    resultado = caracteres_unicos(string)
    print("A string possui caracteres únicos:", resultado)

if __name__ == "__main__":
    main()
