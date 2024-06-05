'''

'''
def dec_bin_iterativo(q):
  
  resultado = ""
  while q > 0:
    resto = q % 2
    resultado = str(resto) + resultado
    q //= 2
  return resultado[::-1]  
numero_decimal = int(input("Digite um número decimal: "))
binario = dec_bin_iterativo(numero_decimal)
print(f"O número {numero_decimal} em binário é: {binario}")
