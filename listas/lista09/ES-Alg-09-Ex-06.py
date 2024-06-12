'''


''' 
def encontrar_palavras_mais_longas(nome_arquivo):
  try:
    with open(nome_arquivo, 'r') as arquivo:
      palavras_unicas = set()
      palavras_tamanhos = {}

      for linha in arquivo:
        linha_sem_espacos = linha.strip()
        palavras_linha = linha_sem_espacos.split()

        for palavra in palavras_linha:
          if palavra not in palavras_unicas:
            palavras_unicas.add(palavra)
            palavras_tamanhos[palavra] = len(palavra)
          else:
            if len(palavra) > palavras_tamanhos[palavra]:
              palavras_tamanhos[palavra] = len(palavra)

      tamanho_maximo = max(palavras_tamanhos.values())


      print(f"Palavras mais longas com {tamanho_maximo} caracteres:")
      for palavra, tamanho in palavras_tamanhos.items():
        if tamanho == tamanho_maximo:
          print(f"- {palavra}")
  except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")

if __name__ == "__main__":
  nome_arquivo = input("Digite o nome do arquivo: ")

  encontrar_palavras_mais_longas(nome_arquivo)
