'''
Valor das entradas. Um determinado zoológico estipula o valor da entrada baseado na idade 
do visitante. Visitantes com até dois anos de idade não precisam pagar. Crianças entre 3 e 12 
anos de idade pagam R$ 14.00. Idosos com 65 anos ou mais pagam R$ 18.00. Todos os 
demais pagam R$ 23.00. Crie um programa que inicia lendo as idades, uma por uma, de um 
grupo de pessoas. O usuário deve entrar uma linha em branco para indicar que não há mais 
pessoas no grupo. Depois disso, seu programa deve exibir uma mensagem informando o 
preço total de todas as entradas para o grupo. O valor deve ser exibido com duas casas 
decimais
'''
valor_total = 0
while True:
    entrada = input("Digite a idade da pessoa (ou deixe em branco para sair): ").strip()
    if entrada == "":
        break
    idade = int(entrada)
    if idade <= 2:
        valor = 0
    elif 3 <= idade <= 12:
        valor = 14
    elif idade >= 65:
        valor = 18
    else:
        valor = 23
    
    valor_total += valor
print("O valor total das entradas é R$ {:.2f}".format(valor_total))
