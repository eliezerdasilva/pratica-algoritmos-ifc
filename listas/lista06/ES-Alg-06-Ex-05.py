'''

'''


negativos = []
zeros = []
positivos = []

print("Digite os números inteiros (pressione Enter para finalizar):")

while True:
    entrada = input()
    if entrada == "":
        break

    numero = int(entrada)
    if numero < 0:
        negativos.append(numero)
    elif numero == 0:
        zeros.append(numero)
    else:
        positivos.append(numero)

print("Números negativos:")
for num in negativos:
    print(num)

print("Zeros:")
for num in zeros:
    print(num)

print("Números positivos:")
for num in positivos:
    print(num)


