'''
 Crie um programa Python que determina e exibe o nome de um polígono 
regular sendo fornecida pelo usuário a quantidade de lados. Seu programa deve suportar 
polígonos de 3 a 10 lados (inclusive). Caso o usuário forneça valores fora desta faixa, o 
programa deve exibir uma mensagem de erro.
'''
lados = int(input("informe a quantidade de lados"))
if lados<3 or lados >10:
    print("Erro : valor invalido")
elif lados == "3":
    print("triângulo")
elif lados == "4" :
    print("Quadrilátero")
elif lados == 5:
    print("Pentágono")
elif lados == 6 :
    print("Hexágono")
elif lados == 7:
    print("Heptágono")
elif lados == 8:
    print("Octógono")
elif lados == 9:
    print("Eneágono")
else :
    print("Decágono")