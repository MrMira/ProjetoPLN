import nltk

# Baixar os arquivos do pacote.
def models():
  nltk.download('punkt')
  nltk.download('stopwords')
  nltk.download('rslp')

# Configurar os modelos.
def main():
  models()

# Executa a função principal.
if __name__ == '__main__':
  main()