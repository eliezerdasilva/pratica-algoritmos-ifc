'''
Uma loja online oferece aos seus clientes dois tipos de 
produto: bugigangas e quinquilharias. Cada bugiganga pesa 75 gramas e cada quinquilharia 
pesa 112 gramas. Faça um programa Python que leia a quantidade de bugigangas e a 
quantidade de quinquilharias de um pedido do usuário. A seguir, seu programa deve calcular e 
exibir o peso total do pedido.

'''
quantidadeBugigangas = int(input("Informe a quantidade de bugigangas :"))
quantidadesQuinquilharia = int(input("Informe a quantidade de quinquilharia"))

gramasTotalGramas = quantidadeBugigangas*75 + quantidadesQuinquilharia*112
print("A quantidade de gramas do pedido é :",gramasTotalGramas, "Gramas")
