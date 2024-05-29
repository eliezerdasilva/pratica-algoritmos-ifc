'''
Anagramas novamente. A noção de anagramas pode ser estendida para múltiplas palavras. 
Por exemplo: "William Shakespeare” e “I am a weakish speller” são anagramas se ignorarmos 
se as letras são maiúsculas e também os espaços. Crie uma nova versão da sua função do 
exercício anterior para verificar se duas frases são anagramas. Sua função deve 
desconsiderar se as letras são maiúsculas ou minúsculas, ignorar espaços e sinais de 
pontuação
'''
import string

def sao_anagramas(frase1, frase2):
    frase1 = frase1.translate(str.maketrans('', '', string.punctuation)).replace(' ', '').lower()
    frase2 = frase2.translate(str.maketrans('', '', string.punctuation)).replace(' ', '').lower()
    
    return sorted(frase1) == sorted(frase2)

frase1 = "William Shakespeare"
frase2 = "I am a weakish speller"
if sao_anagramas(frase1, frase2):
    print("As frases são anagramas.")
else:
    print("As frases não são anagramas.")
