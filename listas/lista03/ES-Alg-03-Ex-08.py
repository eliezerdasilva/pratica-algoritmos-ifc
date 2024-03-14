'''
Existem algumas diferenças entre as escolas latina e anglo-saxônica 
de música. A mais conhecida é a diferença no nome das notas musicais. Na escola latina 
temos Dó, Ré, Mi, Fá, Sol, Lá e Si. Os nomes correspondentes na escola anglo-saxônica são 
C, D, E, F, G, A e B (do dó ao si, respectivamente. Além disso, a tecnologia MIDI incorporou 
um número ao nome de cada nota indicando em qual oitava ela pertence. Por exemplo, o dó 
central do piano é chamado de C4, o dó mais agudo, uma oitava acima é chamado de C5, e o 
dó uma oitava abaixo (mais grave) é chamado de C3
'''
notas = {
    "C": 261.63,
    "C#": 277.18,
    "D": 293.66,
    "D#": 311.13,
    "E": 329.63,
    "F": 349.23,
    "F#": 369.99,
    "G": 392.00,
    "G#": 415.30,
    "A": 440.00,
    "A#": 466.16,
    "B": 493.88
}
# Solicita o nome da nota ao usuário
nome_nota = input("Informe o nome da nota: ")

# Extrai o nome da nota e sua oitava
nota = nome_nota[:-1]
oitava = int(nome_nota[-1])
frequencia = notas[nota] * (2 ** (oitava - 4)) 
print(frequencia)

