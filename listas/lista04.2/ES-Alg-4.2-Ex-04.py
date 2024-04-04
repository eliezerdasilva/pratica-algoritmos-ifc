'''
 Crie um programa Python para calcular o perímetro de um 
polígono sendo fornecidas as coordenadas x e y de cada um de seus vértices. Inicie lendo x e 
y do primeiro vértice. Depois disso continue lendo x e y dos próximos vértices até que o 
usuário entre com uma linha em branco para o valor da coordenada x (ou seja, quando ele 
digitar “Enter" ou “Return" sem fornecer um valor). Cada vez que você ler as coordenadas de 
um novo vértice, você deve calcular a distância em relação ao vértice anterior e acrescentá-la 
ao valor do perímetro. A figura abaixo ilustra como se calcula a distância entre dois pontos 
sendo dadas suas coordenadas x e y.
'''
import math

perimetro = 0
x_primeiro = float(input("Digite a coordenada x do primeiro vértice: "))
y_primeiro = float(input("Digite a coordenada y do primeiro vértice: "))
x_anterior, y_anterior = x_primeiro, y_primeiro
while True:
    entrada_x = input("Digite a coordenada x de um ponto (enter para sair): ").strip()
    if entrada_x == "":
        distancia_final = math.sqrt((x_anterior - x_primeiro) ** 2 + (y_anterior - y_primeiro) ** 2)
        perimetro += distancia_final
        break
    x = float(entrada_x)
    y = float(input("Digite a coordenada y de um ponto: "))
    distancia = math.sqrt((x - x_anterior) ** 2 + (y - y_anterior) ** 2)
    perimetro += distancia
    x_anterior, y_anterior = x, y
print("O perímetro deste polígono é igual a", perimetro)
