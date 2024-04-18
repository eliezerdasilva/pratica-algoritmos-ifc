'''
Em uma determinada cidade, as tarifas de táxi consistem em um valor inicial de 
R$ 4,00 mais R$ 0,25 a cada 140 metros percorridos. Escreva uma função que recebe como 
seu único  parâmetro a distância percorrida em quilômetros, e retorna como seu único 
resultado o valor total da corrida. Escreva um programa principal que demonstre o 
funcionamento de sua função. 
'''
def calcular_tarifa(distancia_km):
    valor_inicial = 4.00  
    tarifa_por_metro = 0.25 / 140  
    distancia_metros = distancia_km * 1000 
    valor_corrida = valor_inicial + (tarifa_por_metro * distancia_metros)
    return valor_corrida

km = float(input("Informe a distância percorrida em quilômetros: "))
valor_total = calcular_tarifa(km)
print("O valor total da corrida é R$", valor_total)