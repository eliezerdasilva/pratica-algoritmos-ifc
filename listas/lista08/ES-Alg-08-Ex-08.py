'''
'''
def dec_bin_recursivo(numero):
 
  if numero == 0:
    return "0"
  elif numero == 1:
    return "1"
  else:
    resto = numero % 2
    parte_binaria = dec_bin_recursivo(numero // 2)
    return parte_binaria + str(resto)

try:
  numero_decimal = int(input("Digite um número decimal não negativo: "))

  if numero_decimal < 0:
    raise ValueError("Erro: valor negativo não é permitido.")

  binario = dec_bin_recursivo(numero_decimal)
  print(f"O número {numero_decimal} em binário é: {binario}")
except ValueError as erro:
  print(erro)
