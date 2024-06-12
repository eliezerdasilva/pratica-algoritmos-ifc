'''

'''
def numerar_linhas(arquivo_entrada, arquivo_saida):

  try:
    with open(arquivo_entrada, 'r') as entrada, open(arquivo_saida, 'w') as saida:
      for numero_linha, linha in enumerate(entrada, start=1):
        saida.write(f"{numero_linha}: {linha}")
  except FileNotFoundError as e:
    print(f"Erro: Arquivo '{e.filename}' não encontrado.")
  except Exception as e:
    print(f"Erro inesperado: {e}")

if __name__ == "__main__":
  nome_arquivo_entrada = input("Digite o nome do arquivo de entrada: ")
  nome_arquivo_saida = input("Digite o nome do arquivo de saída: ")
  numerar_linhas(nome_arquivo_entrada, nome_arquivo_saida)
