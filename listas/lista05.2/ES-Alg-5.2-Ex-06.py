'''
Centralizando uma string. Escreva uma função que recebe uma string como seu primeiro
parâmetro e a largura de uma linha do terminal em caracteres como seu segundo parâmetro.
Sua função deve retornar uma nova string que consiste na string original e no número correto
de espaços iniciais para que a string original apareça centralizada dentro da largura fornecida
quando for impressa. Não adicione nenhum caractere ao final da string. Inclui um programa
principal que demonstre sua função. 

'''
def centralizar_string(string, largura):
    espacos_iniciais = (largura - len(string)) // 2
    return ' ' * espacos_iniciais + string

largura_da_linha = 80
string_original = "Texto centralizado"
string_centralizada = centralizar_string(string_original, largura_da_linha)

print("String original:")
print(string_original)
print("\nString centralizada:")
print(string_centralizada)
