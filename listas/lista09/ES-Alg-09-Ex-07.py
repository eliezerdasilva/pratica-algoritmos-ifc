import sys

def analisar_frequencia_letras(nome_arquivo):
  """
  Analisa a frequência de letras em um arquivo de texto.

  Argumentos:
    nome_arquivo (str): Caminho para o arquivo a ser analisado.

  Retorna:
    None

  Exceções:
    FileNotFoundError: Se o arquivo não for encontrado.
    IndexError: Se nenhum argumento for passado para o programa.
  """
  try:
    with open(nome_arquivo, 'r') as arquivo:
      # Dicionário para armazenar contagem de letras
      contagem_letras = {}
      
      # Processa cada letra do arquivo
      for letra in arquivo.read().lower():
        if letra.isalpha(): # Verifica se é letra (ignora outros caracteres)
          if letra in contagem_letras:
            contagem_letras[letra] += 1
          else:
            contagem_letras[letra] = 1

      # Calcula o total de letras
      total_letras = sum(contagem_letras.values())

      # Converte contagem em porcentagem
      for letra, contagem in contagem_letras.items():
        porcentagem = (contagem / total_letras) * 100
        contagem_letras[letra] = porcentagem

      # Exibe a frequência de cada letra
      print("Frequência de letras:")
      for letra, porcentagem in sorted(contagem_letras.items()):
        print(f"{letra}: {porcentagem:.2f}%")
  except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
  except IndexError:
    print("Erro: Nenhum arquivo passado como argumento.")

if __name__ == "__main__":
  # Verifica se o nome do arquivo foi passado como argumento
  if len(sys.argv) > 1:
    nome_arquivo = sys.argv[1]
    analisar_frequencia_letras(nome_arquivo)
  else:
    print("Erro: Nenhum arquivo passado como argumento.")
