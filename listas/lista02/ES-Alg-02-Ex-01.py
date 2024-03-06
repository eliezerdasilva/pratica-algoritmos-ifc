'''
Unidades de tempo. Crie um programa Python que leia do usuário um valor de intervalo de 
tempo expresso em número de dias, horas, minutos e segundos. O programa deve computar e 
exibir a quantidade total de segundos deste intervalo de tempo informado.

'''
dias =int(input("Informe a quantidade de dias"))
horas = int(input("Informe a quantidade de horas"))
minutos = int(input("Informe a quantidade de minutos"))
segundos = int(input("Informe a quantidade de segundos"))

totalSegundos = (dias*86400)+(horas*3600)+(minutos*60)+segundos
print("O intervalode tempo em segundos é de :",totalSegundos)
