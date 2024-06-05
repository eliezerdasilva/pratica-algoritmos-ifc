'''
'''
def eh_palindromo(texto):
  texto = texto.lower().replace(" ", "")
  if len(texto) < 2:
    return True
  primeiro = texto[0]
  ultimo = texto[-1]
  return primeiro == ultimo and eh_palindromo(texto[1:-1])

texto = input("Informe o texto")
if eh_palindromo(texto):
  print(f"{texto} é um palíndromo!")
else:
  print(f"{texto} não é um palíndromo.")
