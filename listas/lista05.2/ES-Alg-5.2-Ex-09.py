'''
A string representa um inteiro? Neste exercício, você deve escrever uma função chamada 
isInteger que determina se os caracteres em uma string representam ou não um inteiro válido, 
retornando um valor lógico como resultado. Ao determinar se uma string representa um inteiro, 
você deve ignorar qualquer espaço em branco à esquerda ou à direita. Uma vez que este 
espaço em branco é ignorado, uma string representa um inteiro se seu comprimento for pelo 
menos 1 e contiver apenas dígitos, ou se seu primeiro caractere for + ou - e o primeiro 
caractere é seguido por um ou mais caracteres, todos os quais são dígitos. Escreva um 
programa principal que leia uma string do usuário e informe se ela representa ou não um 
número inteiro.

'''

def isInteger(s):
    s = s.strip()  
    if len(s) == 0:
        return False 
    if s[0] in ['+', '-']:
        s = s[1:]  
    return s.isdigit()  

string = input("Digite uma string: ")
if isInteger(string):
    print("A string representa um número inteiro.")
else:
    print("A string não representa um número inteiro.")
