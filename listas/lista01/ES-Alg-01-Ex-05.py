'''
Alguns estabelecimentos retornam créditos em troca de reciclagem 
de recipientes. Em um estabelecimento em particular, vasilhames de um litro ou menos geram 
crédito de 10 centavos e vasilhames de mais de um litro geram créditos de 25 centavos. 
Escreva um programa que leia do teclado a quantidade destes dois tipos de vasilhames a 
serem reciclados. A seguir o programa deve calcular e exibir o valor total dos créditos 
referentes ao retorno dos vasilhames. Pesquise sobre como formatar a saída para que a 
resposta seja exibida com sinal de reais R$ e exatamente duas casas decimais.  

'''
import locale
vasilhameIgualInferiorUmLitro = float(input("Informe quantos vasilhames igual ou inferior a 1 litro possui :"))
vasilhameSuperiorUmLitro = float(input("Informe quantos vasilhames superior a 1 litro possui :"))

totalCredito =round( (vasilhameIgualInferiorUmLitro*0.10)+(vasilhameSuperiorUmLitro*0.25),2)

print(" O total de créditos é de : R$ {:.2f}".format(totalCredito))