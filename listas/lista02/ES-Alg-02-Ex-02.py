'''
Neste exercício você deve fazer o processo inverso do 
exercício anterior. Desenvolva um programa Python que recebe do usuário uma quantidade de 
tempo em segundos. Então o programa deve exibir a quantidade de tempo equivalente na 
forma D:HH:MM:SS, onde D, HH, MM e SS representam dias, horas, minutos e segundos 
respectivamente. Os valores de horas, minutos e segundos devem ser formatados todos com 
dois dígitos, sendo obrigatória a inclusão do dígito 0 para valores menores que 10
'''
segundoDados = int(input("informe o tempo em segundos"))

dias = segundoDados // 86400
segundoDados %= 86400

horas = segundoDados // 3600
segundoDados %= 3600

minutos = segundoDados // 60
segundos = segundoDados % 60

print("Tempo equivalente: {:02d}:{:02d}:{:02d}:{:02d}".format(dias, horas, minutos, segundos))
