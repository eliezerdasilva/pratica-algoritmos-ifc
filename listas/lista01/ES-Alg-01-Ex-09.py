'''
Juros compostos. Faça de conta que você acabou de abrir uma conta de investimento que 
rende 12% de juros ao ano. Os juros que você ganha são pagos ao final do ano. Escreva um 
programa que começa lendo do usuário o valor inicial depositado na conta. Em seguida, o 
programa deve computar e exibir o saldo da conta de investimento após 1, 2 e 3 anos. Exiba 
cada valor com exatamente 2 casas decimais. 

'''
valorInvestido = float(input("Informe o valor investido :"))
jurosAno1 = valorInvestido * 1.12
jurosAno2 = jurosAno1 * 1.12
jurosAno3 = jurosAno2 * 1.12
print("O investimento em 1 ano é de",jurosAno1)
print("O investimento em 2 anos é de",jurosAno2 )
print("O investimento em 3 anos é de ",jurosAno3)