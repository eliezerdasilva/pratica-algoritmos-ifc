'''
Admitindo que uma data é lida pelo algoritmo em uma variável inteira, e não
em uma variável do tipo data, crie um programa Python que leia uma data no formato
DDMMAA e imprima essa data no formato AAMMDD, onde:
• a letra D corresponde a dois algarismos representando o dia;
• a letra M corresponde a dois algarismos representando o mês;
• a letra A corresponde aos dois últimos algarismos representando o ano.
Por exemplo: a data 110618 (11 de junho de 2018), deve ser impressa como 180611
'''
data = int(input("Digite a data no formato DDMMAA: "))
dia = data // 10000
mes = (data % 10000) // 100
ano = data % 100
nova_data = ano * 10000 + mes * 100 + dia
print("A data no formato AAMMDD é:", nova_data)
