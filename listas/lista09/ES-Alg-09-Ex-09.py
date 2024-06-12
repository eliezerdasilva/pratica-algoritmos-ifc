
def remocaoComentarios(arquivo_entrada,arquivo_saida): 
    try:
        with open(arquivo_entrada, "r") as arquivo:
            conteudo = arquivo.readlines()
           

        with open(arquivo_saida, "w") as novo_arquivo:
            for i in conteudo:
                if i[0] == "#":
                    continue
                else:
                    novo_arquivo.write(i)

        with open(arquivo_saida, "r") as arquivo:
            conteudo = arquivo.readlines()
    except Exception :
        print(f"Ocorreu algo inesperado! Erro")
        
if __name__ == "__main__":
    arquivo_entrada = input("Insira o arquivo de entrada: ")
    arquivo_saida = input("Insira o arquivo de saída:")
    remocaoComentarios(arquivo_entrada,arquivo_saida)