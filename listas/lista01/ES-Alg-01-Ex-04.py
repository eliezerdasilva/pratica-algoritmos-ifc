#Crie um programa Python que leia as dimensões de um terreno em 
#metros (largura e profundidade), e exiba o resultado em hectares
larguraTerreno = int(input("informe a Largura do terreno em metros : "))
profundidadeTerreno = int(input("informe a Profundidade do terreno em metros : "))

areaHectares = (larguraTerreno *profundidadeTerreno)/100
print("O total de hectares é de ",areaHectares);
