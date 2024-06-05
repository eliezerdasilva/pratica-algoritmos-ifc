'''

'''
def raiz_quadrada(n, estimativa=1.0):
 
  if abs(estimativa**2 - n) <= 1e-12:
    return estimativa
  else:
    nova_estimativa = (estimativa + (n / estimativa)) / 2
    return raiz_quadrada(n, nova_estimativa)


valores = [2.0, 4.0, 9.0, 16.0, 25.0]

for valor in valores:
  raiz = raiz_quadrada(valor)
  print(f"A raiz quadrada de {valor} é: {raiz:.4f}")
