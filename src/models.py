import file
import language

class SimpleClassifier:
  def __init__(self, base):
    self.words_of_corpus = self.learn(base)

  def learn(self, data):
    words_of_corpus = {}
    intents = data['intents']

    for intent in intents:
      category = intent['category']
      patterns = intent['patterns']

      for pattern in patterns:
        phrase = language.normalize(pattern)

        if category not in list(words_of_corpus.keys()):
          words_of_corpus[category] = {}
        
        for word in phrase:
          if word not in list(words_of_corpus[category].keys()):
            words_of_corpus[category][word] = 1
          else:
            words_of_corpus[category][word] += 1
        
    return words_of_corpus

  def category_classify(self, phrase, category):
    score = 0

    for word in phrase:
      if word in self.words_of_corpus[category]:
        score += self.words_of_corpus[category][word]

    return score

  def classify_phrase(self, phrase):
    highest_score = 0
    category_name = 'unknown'

    for category in self.words_of_corpus.keys():
      score = self.category_classify(phrase, category)

      if score > highest_score:
        highest_score = score
        category_name = category

    return category_name, highest_score