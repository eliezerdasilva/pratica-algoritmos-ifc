'''

'''
import sys

def exibir_cabecalho(nome_arquivo, numero_linhas=10):
  try:
    with open(nome_arquivo, 'r') as arquivo:
      linhas = arquivo.readlines()[:numero_linhas]
  except FileNotFoundError:
    print(f"Erro: Arquivo '{nome_arquivo}' não encontrado.")
    return None
  except ValueError:
    print(f"Erro: 'numero_linhas' deve ser um número não negativo.")
    return None

  
  for linha in linhas:
    print(linha.rstrip())

if __name__ == "__main__":
 
  if len(sys.argv) < 2:
    print("Erro: Nenhum nome de arquivo foi fornecido.")
    sys.exit(1)

  
  nome_arquivo = sys.argv[1]
  if len(sys.argv) > 2:
    try:
      numero_linhas = int(sys.argv[2])
      if numero_linhas <= 0:
        raise ValueError
    except ValueError:
      print(f"Erro: 'numero_linhas' deve ser um número inteiro positivo.")
      sys.exit(1)
  else:
    numero_linhas = 10



exibir_cabecalho(nome_arquivo, numero_linhas)
