
import config
import interface

from talking import Chatbot

# Declaração da função principal.
def main():
  # Mostra o título.
  interface.show_title()
  
  # Inicializa o chatbot.
  bot = Chatbot()
  bot.greeting()

  # Laço principal.
  keep = True
  while keep:
    # Obtém o texto de entrada do usuário.
    print(": ", end='')
    request = input()
    
    # Enquanto não receber mensagem para fechar
    # deixa o robô conversando com a pessoa.
    if request != 'quit':
      bot.process(request)
      bot.reply()
    else:
      keep = False


# Executa a função principal.
if __name__ == '__main__':
    main()