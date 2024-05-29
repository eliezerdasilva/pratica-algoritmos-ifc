'''
Código morse. O código morse é um esquema de codificação de letras e números utilizando 
pontos e traços. Neste exercício você deve escrever um programa que usa um dicionário para 
armazenar o mapeamento de letras e números para código Morse. Voce deve representar os 
pontos com símbolo de ponto “.” e traços com sinal de subtração “-“. A tabela abaixo mostra o 
mapeamento de letras e números para código Morse. Seu programa deve ler uma mensagem 
do usuário e então deve traduzir cada letra e número para código Morse, deixando um espaço 
em branco entra cada caractere traduzido. O programa deve ignorar qualquer caracter que 
não seja letra ou número. Por exemplo, a mensagem Hello, World! Deve ser exibida da 
seguinte forma: .... . .-.. .-.. --- .-- --- .-. .-.. -..
'''
def morse_code(message):
    morse_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    morse_message = []
    for char in message.upper():
        if char in morse_dict:
            morse_message.append(morse_dict[char])
        elif char != ' ':
            morse_message.append(char)

    return ' '.join(morse_message)


def main():
    message = input("Digite a mensagem para ser convertida para código Morse: ")
    morse = morse_code(message)
    print("Código Morse:", morse)


if __name__ == "__main__":
    main()
