import os

def analisar_frequencia_letras(nome_arquivo):

  try:
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
      texto = arquivo.read().lower()  # Converte todo o texto para minúsculas
      texto = texto.replace('e', '')  # Remove a letra "e" do texto

      frequencia_letras = {}
      for letra in 'abcdefghijklmnopqrstuvwxyz':
        frequencia_letras[letra] = 0

      for caractere in texto:
        if caractere in frequencia_letras:
          frequencia_letras[caractere] += 1

      for letra, contagem in frequencia_letras.items():
        total_caracteres = len(texto)
        proporcao = contagem / total_caracteres * 100
        frequencia_letras[letra] = f"{proporcao:.2f}%"

      letra_menos_frequente = min(frequencia_letras, key=frequencia_letras.get)
      frequencia_menos_frequente = frequencia_letras[letra_menos_frequente]

      print("---------- Análise da Frequência de Letras ----------")
      for letra, frequencia in frequencia_letras.items():
        print(f"{letra}: {frequencia}")
      print(f"Letra com menor frequência: {letra_menos_frequente}")

  except FileNotFoundError as e:
    print(f"Erro: Arquivo não encontrado: {e}")
  except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    nome_arquivo = input("Digite o nome do arquivo de texto: ")
    analisar_frequencia_letras(nome_arquivo)