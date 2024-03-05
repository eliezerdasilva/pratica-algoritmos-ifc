'''
Aritmética. Escreva um programa Python que leia do usuário dois inteiros a e b. Seu 
programa deve computar e exibir o seguinte:

•A soma de a e b 
•A diferença quando b é subtraído de a 
•O produto de a por b 
•O quociente quando a é dividido por b 
•O resto quando a é dividido por b

'''
import math

valorInteiroUm = float(input("Informe o valor A (inteiros) :"))
valorInteiroDois = float(input("Informe o valor B (inteiros) :"))


soma = valorInteiroUm + valorInteiroDois
diferenca = valorInteiroUm - valorInteiroDois
produto = valorInteiroUm * valorInteiroDois
quociente =  valorInteiroUm / valorInteiroDois
resto = valorInteiroUm % valorInteiroDois


print("Soma de a e b:", soma)
print("Diferença entre a e b:", diferenca)
print("Produto de a e b:", produto)
print("O quociente de a dividido por b é : ",quociente)
print("O resto da divisão é : ",resto)
print("Resultado de Log10(a):", math.log10(valorInteiroUm))
print("Resultado de a elevado b:",valorInteiroUm**valorInteiroDois)