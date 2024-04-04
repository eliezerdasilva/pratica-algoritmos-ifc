'''
Cifra de César. Um dos primeiros exemplos conhecidos de criptografia foi utilizado pelo 
imperador romano Julio César. César precisava fornecer instruções por escrito para seus 
generais, mas não queria que seus inimigos descobrissem suas estratégias caso as 
mensagens com as instruções fossem extraviadas. Com isso, ele acabou desenvolvendo o 
que mais tarde ficou conhecido como a “cifra de César”.  
 
A idéia por trás desta cifra é simples (e portanto não oferece proteção contra as técnicas 
modernas de quebra de códigos). Cada letra da mensagem original é deslocada em 3 
posições. Com isso, a letra A se torna letra D, B se torna E, C se torna F, e assim por diante. A 
ultimas 3 letras do alfabeto são transformadas nas primeiras. X se torna A, Y se torna B e Z se 
torna C. Caracteres que não são letras não são convertidos. 
 
Escreva um program Python que implemente a cifra de César. Permita que o usuário forneça a 
mensagem e a distância de deslocamento de letras (portanto não será o valor fixo de 
deslocamento de 3 letras no alfabeto). Certifique-se que seu programa codifique corretamente 
tanto letras maiúsculas quanto minúsculas. Seu programa também deve suportar valores 
negativos de deslocamento de letras, assim ele pode ser usado tanto para codificar quanto 
para decodificar mensagens.
'''
mensagem = input("Digite a mensagem: ")
deslocamento = int(input("Digite o deslocamento de letras: "))

resultado = ""
for char in mensagem:
    if char.isalpha():  
        base = ord('A') if char.isupper() else ord('a')
        cod = (ord(char) - base + deslocamento) % 26 + base  
        resultado += chr(cod) 
    else:
        resultado += char 
        
print(resultado)