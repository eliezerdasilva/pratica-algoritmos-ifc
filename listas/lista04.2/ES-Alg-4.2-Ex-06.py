'''
Bits de paridade. Um bit de paridade é um mecanismo para detecção de erros em dados 
transmitidos por uma conexão não confiável, como linha telefônica por exemplo. A idéia básica 
é que, a cada grupo de 8 bits, seja acrescentado um bit adicional de forma que erros em bits 
individuais possam ser detectados.  
 
Os bit de paridade podem ser computados para paridade par ou paridade ímpar. Se for usada 
paridade par, então o bit de paridade a ser transmitido deve ser tal que o número total de bits 
“1”  transmitidos (8 bits de dados + 1 bit de paridade) é par. Se for utilizada paridade ímpar, o 
número total de bits “1” transmitidos deve ser ímpar. 
 
Escreva um programa Python que compute o bit de paridade para grupos de 8 bits fornecidos 
pelo usuário utilizando paridade par. Seu programa deve ler strings contendo 8 bits (portanto 
as strings vai ser sequencias de 8 caracteres 0 ou 1) até que o usuário entre com uma linha 
em branco. Logo após o usuário fornecer cada string, seu programa deve exibir uma 
mensagem informando se o bit de paridade deve ser 0 ou 1. O programa também deve exibir 
'''
while True:
    entrada = input("Digite uma sequência de 8 bits (ou deixe em branco para sair): ").strip()
    
    if entrada == "":
        break
    
    if len(entrada) != 8 or not all(bit in '01' for bit in entrada):
        print("A entrada deve conter exatamente 8 bits (0 ou 1).")
        continue
    
    num_uns = entrada.count('1')
    
    if num_uns % 2 == 0:
        bit_de_paridade = '0'
    else:
        bit_de_paridade = '1'
    
    print("O bit de paridade para a sequência {} deve ser: {}".format(entrada, bit_de_paridade))
