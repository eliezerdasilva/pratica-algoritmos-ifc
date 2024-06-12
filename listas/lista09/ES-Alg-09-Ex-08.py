import re

def encontrar_palavras_mais_frequentes(nome_arquivo):

  try:
    with open(nome_arquivo, 'r') as arquivo:
      contagem_palavras = {}
      for linha in arquivo: 
        palavras_linha = re.findall(r'\w+', linha.lower())
        for palavra in palavras_linha:
          if palavra in contagem_palavras:
            contagem_palavras[palavra] += 1
          else:
            contagem_palavras[palavra] = 1
      frequencia_maxima = max(contagem_palavras.values())


      print(f"Palavras mais frequentes ({frequencia_maxima} aparições):")
      for palavra, contagem in contagem_palavras.items():
        if contagem == frequencia_maxima:
          print(f"- {palavra}")
  except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")

if __name__ == "__main__":
  nome_arquivo = input("Digite o nome do arquivo: ")


  encontrar_palavras_mais_frequentes(nome_arquivo)
