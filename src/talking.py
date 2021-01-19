import file
import support
import language

import models

# Classe contendo a estrutura do chatbot.
class Chatbot:
  def __init__(self):
    self.sex = support.random_natural()

    if self.sex == 1:
      self.name = "Miguel"
    else:
      self.name = "Priscila"
    
    self.base = file.load_json('src/intents.json')
    self.model = models.SimpleClassifier(self.base)

    self.request = ""
    self.response = ""
  
  def greeting(self):
    print(f"Olá eu sou {self.name}. Como posso ajudar?")
  
  def process(self, text):
    self.request = text

    parsed = self.parse(text)
    analysed = self.analyse(parsed)
    response = self.execute(analysed)

    self.response = response
  
  def parse(self, data):
    list_of_words = language.normalize(data)
    return list_of_words

  def analyse(self, data):
    class_score = self.model.classify_phrase(data)
    return class_score

  def execute(self, data):
    text = ""
    response = []
    
    class_category = data[0]
    class_score = data[1]

    if class_category == 'unknown':
      default = self.base['default']

      for state in default:
        category = state['category']
        if category == class_category:
          response = state['response']
          break
      
      initial = response['initial']
      initial_chosen = support.random_natural(0, len(initial))
      
      text = (
        f"{initial[initial_chosen]}"
      )

    if class_category != 'unknown':
      intents = self.base['intents']

      for intent in intents:
        category = intent['category']
        if category == class_category:
          response = intent['response']
          break
      
      initial = response['initial']
      options = response['options']

      initial_chosen = support.random_natural(0, len(initial))
      options_chosen = support.random_natural(0, len(options))
      
      text = (
        f"{initial[initial_chosen]}\n"
        f"{options[options_chosen]}"
      )

    return text
  
  def reply(self):
    print(f"\n{self.response}")