'''
Faça uma função chamada eh_bissexto(ano) que recebe como parâmetro um inteiro positivo 
ano e devolve True se ano for bissexto, False em caso contrário.  
Obs.: Um ano é bissexto se (ano % 4 == 0 E (ano % 100 != 0 OU ano % 400 == 0)).)
'''


def eh_bissexto(ano):
    if (ano % 4) == 0 and (ano % 100 != 0 or ano % 400 == 0):
        return "O ano é bissexto"
    else:
        return "O ano não é bissexto"

ano = int(input("Informe o ano: "))
resultado = eh_bissexto(ano)
print(resultado)
