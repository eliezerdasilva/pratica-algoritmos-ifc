'''
Aproximação do valor de . O valor aproximado de  pode ser calculado pela série infinita 
apresentada abaixo: 
 
 π≈3 + 4
2 ×3 ×4 −4
4 ×5 ×6 + 4
6 ×7 ×8 −4
8 ×9 ×10 + 4
10 ×11 ×12 
 
Escreva um programa Python que exiba 15 aproximações de . A primeira aproximação deve 
ter apenas o primeiro termo da série (ou seja, o valor resultante vai ser somente 3). Cada nova 
aproximação de  mostrada pelo seu programa deve incluir mais um termo da série, sendo 
cada vez uma aproximação mais precisa do que a anterior.

'''
termo = 3
soma = termo

for i in range(2, 16):
    termo = (i * 2 - 1) * (i * 2) * (i * 2 + 1)
    if i % 2 == 0:
        termo = 4 / termo
        soma += termo
    else:
        termo = 4 / termo
        soma -= termo

print("Valor de π aproximado após 15 termos:", soma)

