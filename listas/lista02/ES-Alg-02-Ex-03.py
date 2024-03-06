'''
A linguagem Python possui uma biblioteca de funções para lidar com tempo, 
incluindo a função asctime no módulo time. Ela lê o tempo atual do Clock interno do 
computador e o retorna em um formato legível. Escreva um programa que exiba a data e a 
hora atuais. Seu programa não precisa obter qualquer entrada do usuário.

'''

from datetime import datetime

hora_atual = datetime.now().time()

print("Hora atual:", hora_atual)
