'''
Tabela de conversão de temperaturas. Escreva um programa Python que mostre uma tabela 
de conversão de temperaturas em graus Celsius e graus Fahrenheit. A tabela deve incluir em 
suas linhas todas as temperaturas entre 0 e 100 graus Celsius que sejam múltiplas de 10 
graus Celsius. Inclua os cabeçalhos apropriados e tabulações para suas colunas. Pesquise na 
internet sobre a fórmula de conversão de temperaturas Celsius para Fahrenheit.

 TC/5 = (TF – 32)/9
'''
tempC = 0
tempF = 0
while tempC <= 100:
    tempF = (tempC/5) * 9 +32 
    print("Temperatura em Celsius = ", tempC," Temperatura em Fahrenheit", tempF)
    tempC += 10
    
