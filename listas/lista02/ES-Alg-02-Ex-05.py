'''
Considere o software que controla uma máquina automática de compras. 
Uma tarefa que ele precisa realizar é determinar quanto troco fornecer ao comprador quando 
este faz o pagamento em dinheiro. Escreva um programa Python que inicia lendo do usuario 
uma quantidade de centavos como um número inteiro (portanto vamos considerar números de 
0 a 99). Então o seu programa deve calcular e exibir quantidade e o valor de cada moeda para 
compor este troco em centavos informado. O troco deve ser montado com a menor quantidade 
possível de moedas. Assuma que a máquina possui moedas de 50, 25, 10, 5 e 1 centavos.
'''
centavos = int(input("Informe a Quantidade de centavos"))
moedasCinquenta = centavos // 50
moedasVinteCinco = (centavos % 50) // 25
moedasDez = ((centavos % 50) % 25) // 10
moedasCinco = (((centavos % 50) % 25) % 10) // 5
moedasUm = (((centavos % 50) % 25) % 10) % 5
print("Moedas de 50 centavos:", moedasCinquenta)
print("Moedas de 25 centavos:", moedasVinteCinco)
print("Moedas de 10 centavos:", moedasDez)
print("Moedas de 5 centavos:", moedasCinco)
print("Moedas de 1 centavo:", moedasUm)