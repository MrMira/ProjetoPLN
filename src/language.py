import nltk

# Realiza o processo de token.
def tokenizer(data):
  return nltk.word_tokenize(data)

# Remove pontuação.
def remove_punctuation(list_of_words):
  return [word for word in list_of_words if word.isalnum()]

# Deixa tudo em minúsculo.
def to_lower_case(list_of_words):
   return [word.lower() for word in list_of_words]

# Remove stopwords da frase.
def remove_stopwords(list_of_words):
  stopwords = nltk.corpus.stopwords.words('portuguese')
  return [word for word in list_of_words if word not in stopwords]

# Realização o processo de stemmer.
def settemer(list_of_words):
  stemmer = nltk.stem.RSLPStemmer()

  list_of_stems = []
  for word in list_of_words:
    stem = stemmer.stem(word)
    list_of_stems.append(stem)

  return list_of_stems

# Realiza a normalização de um texto.
def normalize(phrase):
  phrase = tokenizer(phrase)
  phrase = remove_punctuation(phrase)
  phrase = to_lower_case(phrase)
  phrase = remove_stopwords(phrase)
  phrase = settemer(phrase)
  return phrase