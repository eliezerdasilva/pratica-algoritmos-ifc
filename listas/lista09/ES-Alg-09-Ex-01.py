'''

'''
import sys

# Imprime o número de argumentos (incluindo o nome do script)
print(f"Número de argumentos: {len(sys.argv)}")

# Imprime cada argumento individualmente
for i, argumento in enumerate(sys.argv):
    print(f"Argumento {i+1}: {argumento}")
