from random import randrange

# Gera um número aleatório natural entre um
# número inicial (inclusivo) e final (exclusivo).
def random_natural(start = 0, end = 2):
  return randrange(start, end)