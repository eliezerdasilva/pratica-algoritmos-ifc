'''
Distância entre dois pontos na terra. A terra é curva (a não ser para os terraplanistas! 😱) e 
a distância entre graus de longitude (leste-oeste) varia conforme a latitude (norte-sul). Com 
isso, encontrar a distância entre dois pontos na superfície da terra é mais complicado do 
simplesmente usar o Teorema de Pitágoras no plano. Seja  e  as latitudes e 
longitudes de dois pontos na superfície da terra. A distância em quilômetros entre estes dois 
pontos ao longo da superfície da terra é dada por: 

dista n ci a = 6371.01 ×ar ccos(sen(t1) ×sen(t2) + cos(t1) ×cos(t2) ×cos(g1 −g2)) 

Crie um programa Python que receba a latitude e a longitude de dois pontos na Terra em 
graus, calcule e exiba a distância entre eles em quilômetros ao longo da superfície

Observação: as funções trigonométricas do Python operam em radianos (e não em graus). 
Com isso, você vai precisar converter os dados de graus para radianos antes de calcular a 
distância. O módulo matemático do Python contém uma função chamada radians, que faz 
esta conversão.
Observação: você pode usar a função log10 do módulo math para calcular o penúltimo 



'''
import math

lat1 = float(input("Digite a latitude do primeiro ponto em graus: "))
lon1 = float(input("Digite a longitude do primeiro ponto em graus: "))
lat2 = float(input("Digite a latitude do segundo ponto em graus: "))
lon2 = float(input("Digite a longitude do segundo ponto em graus: "))

''''
? 
'''
lat1 = lat1 * math.pi / 180
lon1 = lon1 * math.pi / 180
lat2 = lat2 * math.pi / 180
lon2 = lon2 * math.pi / 180

raio_terra = 6371.01


delta_lat = lat2 - lat1
delta_lon = lon2 - lon1

a = (math.sin(delta_lat / 2) ** 2) + math.cos(lat1) * math.cos(lat2) * (math.sin(delta_lon / 2) ** 2)
c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
distancia = raio_terra * c


print("A distância entre os pontos é de", round(distancia, 2), "quilômetros.")
