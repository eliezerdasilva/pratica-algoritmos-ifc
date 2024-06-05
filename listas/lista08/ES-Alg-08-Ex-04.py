'''

'''
def fibonacci_memo(n, memo={}):
 

  if n in memo:
    return memo[n]

  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

n = int(input("informe um numero"))
resultado = fibonacci_memo(n)
print(f"O {n}º número de Fibonacci é {resultado}")
