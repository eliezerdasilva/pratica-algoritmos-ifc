if __name__ == "__main__":
    arquivo_entrada = input("Insira o nome do arquivo de entrada: ")
    try:
        with open(arquivo_entrada, "r") as arquivo:
            conteudo = arquivo.readlines()
            texto = ""
            for i in conteudo:
                texto += i.replace("\n", " ")
                
            traducao = str.maketrans("", "", ".,:?!#/()0123456789")
            texto_sem_pontuacao = texto.translate(traducao)
            lista_de_palavras = texto_sem_pontuacao.split()
            
            erros_ortograficos = []
            for i in lista_de_palavras:
                if i in open('dicionario.txt').read():
                    continue
                else:
                    erros_ortograficos.append(i)
            if not erros_ortograficos:
                print(f"O arquivo {arquivo_entrada} não possui erros ortográficos!")
            else:
                print(f"Palavras com erro ortográfico no arquivo {arquivo_entrada}:")
                for i in erros_ortograficos:
                    print(i)
    except Exception as e:
        print(f"Ocorreu algo inesperado! Erro: {e}")