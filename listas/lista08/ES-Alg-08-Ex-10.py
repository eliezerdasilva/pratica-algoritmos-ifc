'''
'''
def decodificar_run_length(lista_compactada):
  if len(lista_compactada) == 2:
    return lista_compactada[0] * lista_compactada[1]
  else:
    
    valor, repeticoes = lista_compactada[0:2]
    resto_lista = lista_compactada[2:]

    resto_descompactado = decodificar_run_length(resto_lista)

    descompactado = valor * repeticoes + resto_descompactado

    return descompactado

lista_compactada = ["A", 12, "B", 4, "A", 6, "B", 1]
print("Lista compactada:", lista_compactada)

lista_descompactada = decodificar_run_length(lista_compactada)
print("Lista descompactada:", lista_descompactada)


