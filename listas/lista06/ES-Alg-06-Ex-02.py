'''

'''
numeros = []

while True:
    num = int(input("Digite um número (0 para parar): "))
    if num == 0:
        break
    numeros.append(num)

numeros.sort(reverse=True)

print("Números em ordem decrescente:")
for num in numeros:
    print(num)
