'''
Conta do almoço. Imagine que você foi almoçar num restaurante, e pediu uma refeição com 
um suco, um prato principal e uma sobremesa. Cada um desses itens tem um preço unitário. 
Algoritmos Bacharelado em Ciência da Computação 
Ao final, o valor da conta deve ser a soma do valor dos itens consumidos, acrescida de 10% 
de taxa de serviço. Faça um programa Python para receber estes dados do usuário e calcular 
o valor total da conta deste tipo de refeição. Exiba a resposta com os mesmos critérios de 
formatação da questão anterior (R$ e 2 casas decimais). 
'''

valorSuco = float(input("Informe o valor do suco :"))
valorPrato = float(input("Informe o valor do prato :"))
valorSobremesa = float(input("Informe o valor do sobremesa :"))

valorTotalPagar = (valorPrato+valorSuco+valorSobremesa)*1.10
print("O valor total é de R$ {:.2f}".format(valorTotalPagar))