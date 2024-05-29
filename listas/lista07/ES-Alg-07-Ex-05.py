'''
Anagramas. Duas palavras são anagramas se contiverem as mesmas letras, mas em ordens 
diferentes. Por exemplo: “amor" e “roma" são anagramas porque cada uma delas contém um 
"a", um "o", um "m" e um “r”. Crie uma função Python que recebe duas strings e retorna True 
se elas forem anagramas, ou False caso contrário
'''

def sao_anagramas(palavra1, palavra2):
    palavra1 = palavra1.replace(" ", "").lower()
    palavra2 = palavra2.replace(" ", "").lower()
    
    
    if len(palavra1) != len(palavra2):
        return False
    
    contador1 = {}
    contador2 = {}
    
    for letra in palavra1:
        contador1[letra] = contador1.get(letra, 0) + 1
    
    for letra in palavra2:
        contador2[letra] = contador2.get(letra, 0) + 1
    
    return contador1 == contador2

palavra1 = "amor"
palavra2 = "roma"
print(sao_anagramas(palavra1, palavra2))  # Saída: True
