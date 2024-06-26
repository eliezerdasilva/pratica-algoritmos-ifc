'''
Escreva uma função que determina quantos dias há em um determinado 
mês. Sua função deve receber dois parâmetros: o mês como um número inteiro entre 1 e 12 e 
o ano como um número inteiro de quatro dígitos. Certifique-se de que sua função retorne o 
número correto de dias em fevereiro para os anos bissextos. Inclua um programa principal que 
lê um mês e ano do usuário e exibe o número de dias naquele mês. O exercício 12 da lista 3 
pode ajudá-lo a resolver esse problema

'''
def mesAno(month, year):

    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return 29
        else:
            return 28
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        return 31


month = int(input("Digite o número do mês (1 a 12): "))
year = int(input("Digite o ano (4 dígitos): "))

    
num_days = mesAno(month, year)

print(f"O mês {month} do ano {year} tem {num_days} dias.")

