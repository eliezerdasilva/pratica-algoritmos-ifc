'''
Dado um número de três algarismos N = CDU 
(onde C é o algarismo das centenas, D é o algarismo das dezenas e U o algarismo das 
unidades), considere o número M constituído pelos algarismos de N em ordem inversa, isto é, 
M=UDC. Faça um programa Python para gerar e imprimir M a partir de N (p.ex.:N=123 
->M=321).
'''

numero = int(input("Informe um número inteiro N com três algarismo"))
centena = numero//100
dezena = (numero%100)//10
unidade= ((numero%100)%10) 

m = unidade*100 + dezena*10 + centena
print("N :",numero," M: ",m)