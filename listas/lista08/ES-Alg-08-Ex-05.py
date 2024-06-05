'''
'''
def somar_valores(valor_anterior):
 

  valor_str = input("Digite um valor numérico (ou deixe em branco para finalizar): ")

  try:
    valor = float(valor_str)
  except ValueError:
    return valor_anterior

  if valor_str == "":
    return valor_anterior
  else:
    return somar_valores(valor_anterior + valor)

soma_total = somar_valores(0.0)
print(f"Soma total: {soma_total}")
