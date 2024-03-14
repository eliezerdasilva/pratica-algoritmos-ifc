'''
A quantidade de dias de um mes pode variar de 28 a 31 
dias. Neste exercício você deve criar um programa Python que recebe do usuário o nome de 
um mês (como uma string). Então seu programa deve exibir uma mensagem informando a 
quantidade de dias daquele mês. Caso o mês seja fevereiro, sua mensagem pode informar 
“28 ou 29 dias"
'''

mes = input("informe o mês")
mes = mes.lower()
if mes == "janeiro":
    print("Janeiro 31 dias")
elif mes == "fevereiro":
    print("Fevereiro 28 ou 29 dias")
elif mes == "março":
    print("Março 31 dias")
elif mes == "abril":
    print("Abril 30 dias")
elif mes == "maio":
    print("Maio 31 dias")
elif mes == "junho":
    print("Junho 30 dias")
elif mes == "julho":
    print("Julho 31 dias")
elif mes == "agosto":
    print("Agosto 31 dias")
elif mes == "setembro":
    print("Setembro 30 dias")
elif mes == "outubro":
    print("Outubro 31 dias")
elif mes == "novembro":
    print("Novembro 30 dias")
elif mes == "dezembro":
    print("Dezembro 30 dias")
else:
    print("Valor invalido")