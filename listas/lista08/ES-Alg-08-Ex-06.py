'''
'''
def mdc(a, b):
  """
  Função recursiva para calcular o Máximo Divisor Comum (MDC) de dois números inteiros.

  Argumentos:
    a (int): O primeiro número inteiro.
    b (int): O segundo número inteiro.

  Retorno:
    int: O Máximo Divisor Comum de a e b.
  """
  if b == 0:
    return a
  else:
    resto = a % b
    return mdc(b, resto)

# Solicita os números do usuário
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Calcula o MDC usando a função mdc
mdc_resultado = mdc(num1, num2)

# Mostra o resultado
print(f"O Máximo Divisor Comum de {num1} e {num2} é: {mdc_resultado}")
