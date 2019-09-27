#! python3

# Keras deep learning library to build classification model
# Lancaster stemming library used to collapse distinct word forms
import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

# things we need for Tensorflow
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import pandas as pd
import pickle
import random

import json

with open('chat_intents.json') as intent_file:
    intents = json.load(intent_file)

words = []
classes = []
documents = []
ignore_words = ['?']

#loop through each sentence in our intents patterns
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each word in sentence
        w = nltk.word_tokenize(pattern)
        
        # add to words list
        words.extend(w)
        
        # add documents in corpus
        documents.append((w, intent['tag']))
        
        # add to our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# stem & lower ea word & remove dupes
words = [stemmer.stem(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))

# sort classes
classes = sorted(list(set(classes)))

# documents = combination between patterns & intents
#print(len(documents), 'documents', documents)
# classes = intents
#print(len(classes), "classes", classes)
# words = all words, vocab
#print(len(words), "unique stemmed words", words)


# create our training data
training = []
# create an empty array for our output
output_empty = [0] * len(classes)

# training set, bag of words for ea sentence
for doc in documents:
    # initialise our bag of words
    bag = []
    #list tokenized words for the pattern
    pattern_words = doc[0]
    # stem ea word - create base word to represent related words
    # Please read stemming VS lemmatization
    pattern_words = [stemmer.stem(word.lower()) for word in pattern_words]
    
    # create our bag of words arr with 1, if word match found in
    # current pattern
    length = 0
    for w in words:
        # bag.append(1) if w in pattern_words else bag.append(0)
        if w in pattern_words:
          bag.append(1)
          length += 1
        else:
          bag.append(0)
        
    # output is '0' for ea tag & '1' for current tag (for ea pattern)
    # output_row is basically the class/intents it falls in
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    
    # append length of sentence into training data
    # bag.append(length)
    
    training.append([bag, output_row])
    
    # print(training)


    # shuffle our features & turn into np.array
random.shuffle(training)
training = np.array(training)

# create train & test lists. X - patterns, Y - intents
# training_x = [training[:,0], training[:,2]]
train_x = list(training[:,0])
train_y = list(training[:,1])
#print(train_x)
#print(len(train_x[0]))

# Create model - 3 layers
# 1st layer 128 neurons, 2nd layer 64 neurons & 3rd contains num of neurons
# equal to num of intents to predict output intent with softmax

model = Sequential()
model.add(Dense(128, input_shape = (len(train_x[0]), ), activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation = 'softmax'))

# Compile model. Stochastic gradient descent with Nesterov accelerated
# gradient gives good results for this model

sgd = SGD(lr = 0.01, decay = 1e-6, momentum = 0.9, nesterov = True)
# print(dir(sgd))
# print(sgd.lr)
model.compile(loss = 'categorical_crossentropy', optimizer = sgd,
              metrics = ['accuracy'])



# Fit the model
# Epochs means iterations
model.fit(np.array(train_x), np.array(train_y), epochs = 200,
          batch_size = 5, verbose = 1)

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into arr
    sentence_words = nltk.word_tokenize(sentence)
    # stem ea word - create short form for word
    sentence_words = [stemmer.stem(word.lower()) for word in sentence_words]
    return sentence_words

# Translate user sentence into bag of words with arr 0/1
# 0 or 1 for ea word in bag that exists in the sentence
def bow(sentence, words, show_details = False):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # Initialise bag of words - matrix of N words, vocab matrix
    bag = [0] * len(words)
    
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                # assign 1 if current word in vocab position
                bag[i] = 1
                if show_details:
                    print(f"Found in bag: {w}")
                    
    # bag.append(len(sentence_words))
    return np.array(bag)

def classify_local(sentence):
    ERROR_THRESHOLD = 0.5
    
    # generate probabilities from model
    input_data = pd.DataFrame([bow(sentence, words)], dtype = float,
                              index = ['input'])
    # print([input_data])
    
    results = model.predict([input_data])[0]
    # print(results)
    # filter predictions below a threshold & provide intent index
    
#     for i, r in enumerate(results):
#       print(i)
#       print(r)
#       print(r > ERROR_THRESHOLD)
#       print()
    
    results = [[i, r] for i, r in enumerate(results) if r > ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key = lambda x: x[1], reverse = True)
    
    return_list = []
    for r in results:
        # print(r)
        return_list.append((classes[r[0]], str(r[1])))
    # return tuple of intent & probability
    return return_list


intent_list = classify_local("how old is sp")
# print(intent_list)

from data.general import general
from data.course import course
from data.cca import cca
from data.misc import misc

def find_data(intent_list: list):
    if len(intent_list) < 1:
        return "Sorry I don't know what you are trying to ask :("
    else:
        user_intent = intent_list[0][0]
    
    if user_intent == 'unknown' or user_intent == '':
        return "Sorry I don't understand that."
    for intent in intents['intents']:
        if intent['tag'] == user_intent:
            file_name = intent['context']
    
    data_dicts = dict(
        general = general,
        course = course,
        cca = cca,
        misc = misc
    )
    data_dict = data_dicts[file_name]
    
    output = data_dict[user_intent]
    return output


def ask_chatbot(user_input: str):
    intent_list = classify_local(user_input)
    # user_intent = intent_list[0][0]
    out = find_data(intent_list)
    return out

print(ask_chatbot("are clubs compulsory"))