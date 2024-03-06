'''
Dado um número de três algarismos N = CDU (onde C é o 
algarismo das centenas, D é o algarismo das dezenas e U o algarismo das unidades) Faça um 
programa Python que receba do usuário o número inteiro N, e imprima separadamente a 
centena, a dezena e a unidade.

'''
numero = int(input("Informe um número inteiro com três algarismo"))
centena = numero//100
dezena = (numero%100)//10
unidade= ((numero%100)%10)


print("Centena ",centena," Dezena ",dezena," Unidade ",unidade)
