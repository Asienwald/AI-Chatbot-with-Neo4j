import nltk
import numpy as np
import random
import string # to process standard python strings

f = open('chatbot.txt', 'r', errors = 'ignore')
raw = f.read()
raw = raw.lower() # Converts to lowercase

# first time use only
# nltk.download('punkt')
# nltk.download('wordnet')

# converts to list of sentences
sent_tokens = nltk.sent_tokenize(raw)
# converts to list of words
word_tokens = nltk.word_tokenize(raw)

print("SENT", sent_tokens[:2])
print("\nWORD", word_tokens[:2])