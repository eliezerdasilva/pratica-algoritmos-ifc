'''
Calculadora de envio e-commerce. Uma loja online fornece envio de seus itens pelo preço 
de R$ 10,95 para o primeiro item e R$ 2,95 para cada um dos demais itens. Escreva uma 
função que receba a quantidade de ítens de um pedido e retorne o valor total do envio de 
acordo com essas regras. Inclua um programa principal que leia do usuário o número de itens 
adquiridos e mostre o custo do envio
'''
def envio(quantidadeEnvio):
    result = 0
    result = 10.95 
    if quantidadeEnvio >= 2 :
        quantidadeEnvio = quantidadeEnvio -1 
        result += quantidadeEnvio*2.95
    
    return result
quantidadeEnvio = int(input("Informe a quantidade de produtos"))
result = envio(quantidadeEnvio)
print(" O valor para entrega é de : {:.2f}".format(result))