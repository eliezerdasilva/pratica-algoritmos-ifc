#Escreva um programa Python que peça para o usuário os comprimentos 
#da largura e profundidade de uma sala. Após a leitura dos valores, seu programa deve exibir a 
#área da sala. A largura e a profundidade devem ser números reais. Inclua as unidades nas 
#mensagens de entrada e saída (metros e metros quadrados).
profundidadeSala= int(input("Informe a profundidade da Sala(Metros)"))
larguraSala = int(input("Informe a largura da Sala(Metros)"))

areaSala = profundidadeSala*larguraSala
print("A área da sala é :",areaSala, "metros")