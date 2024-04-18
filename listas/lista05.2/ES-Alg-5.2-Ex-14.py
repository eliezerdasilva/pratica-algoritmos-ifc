'''
Datas mágicas. Uma “data mágica” é uma data na qual a multiplicação do dia pelo mês é 
igual aos dois últimos dígitos do ano. Por exemplo, 10 de junho de 1960 é uma data mágica 
porque 10 vezes 6 é igual a 60, que são os dois últimos dígitos do ano. Escreva uma função 
que determina se uma data é ou não mágica. A função deve receber 3 parâmetros inteiros 
(dia, mês e ano), e retornar um valor lógico. Escreva um programa main que utilize sua função 
para determinar e imprimir todas as datas mágicas do século XX. O exercício anterior pode ser 
útil para resolver este problema
'''

dia = int(input("Digite o dia (1-31): "))
mes = int(input("Digite o mês (1-12): "))
ano = int(input("Digite o ano (1900-1999): "))
   
def main():
    resto = ano % 100
   
    if dia * mes == resto:
        print(f"{dia}/{mes}/{ano} é uma data mágica")
    else:
        print(f"{dia}/{mes}/{ano} não é uma data mágica") 
main()
