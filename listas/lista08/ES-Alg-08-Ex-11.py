'''
'''
def codificar_run_length(lista_original):
  if len(lista_original) == 1:
    return [lista_original[0], 1]
  else:
    elemento_atual = lista_original[0]
    repeticoes = 1
    resto_lista = lista_original[1:]

    for elemento in resto_lista:
      if elemento == elemento_atual:
        repeticoes += 1
      else:
        break

    resto_compactado = codificar_run_length(resto_lista)
    lista_compactada = [elemento_atual, repeticoes] + resto_compactado

    return lista_compactada

texto_original = input("Digite um texto para comprimir: ")
lista_original = list(texto_original)

lista_compactada = codificar_run_length(lista_original)
print("Texto compactado:", lista_compactada)
