'''
A tabela abaixo mostra os feriados nacionais brasileiros que caem sempre no 
mesmo dia (em oposição aos feriados variáveis como carnaval e corpus christi).

Escreva um programa Python que leia do usuário o mês e o dia de uma determinada data. Se 
o mês e o dia corresponderem a uma das datas da tabela acima, seu programa deve exibir o 
nome do feriado. Caso contrário o programa deve informar que o dia e o mês informados não 
correspondem a um feriado nacional.
'''

mes = input("Informe o mês (formato MM): ")
dia = input("Informe o dia (formato DD): ")
data = mes + "-" + dia
if data == "01-01":
    print("O dia", dia, "de", mes, "corresponde ao feriado de Ano Novo.")
elif data == "21-04":
    print("O dia", dia, "de", mes, "corresponde ao feriado de Tiradentes.")
elif data == "01-05":
    print("O dia", dia, "de", mes, "corresponde ao feriado do Dia do Trabalho.")
elif data == "07-09":
    print("O dia", dia, "de", mes, "corresponde ao feriado da Independência do Brasil.")
elif data == "12-10":
    print("O dia", dia, "de", mes, "corresponde ao feriado de Nossa Senhora Aparecida.")
elif data == "02-11":
    print("O dia", dia, "de", mes, "corresponde ao feriado de Finados.")
elif data == "15-11":
    print("O dia", dia, "de", mes, "corresponde ao feriado da Proclamação da República.")
elif data == "25-12":
    print("O dia", dia, "de", mes, "corresponde ao feriado de Natal.")
else:
    print("O dia", dia, "de", mes, "não corresponde a um feriado nacional.")
