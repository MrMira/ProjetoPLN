import json

# Faz a leitura de um arquivo JSON.
def load_json(name):
  with open(name, encoding='utf-8') as file:
    data = json.load(file)
    return data