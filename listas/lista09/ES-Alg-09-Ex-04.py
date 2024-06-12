'''


'''
import sys

def concatenar_arquivos(nome_arquivos):
  for nome_arquivo in nome_arquivos:
    try:
      with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()
        print(f"\n-- Conteúdo do arquivo: {nome_arquivo} --")
        print(conteudo)
    except FileNotFoundError:
      print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print("Erro: Nenhum nome de arquivo foi fornecido.")
    sys.exit(1)

  nome_arquivos = sys.argv[1:]

  concatenar_arquivos(nome_arquivos)
