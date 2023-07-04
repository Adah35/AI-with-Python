# from ast import If
# from codecs import ignore_errors
# import random 
# import json
# import pickle
# import numpy as np

import nltk
nltk.download('punkt')
from nltk.stem import WordNetLemmatizer

# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense,Activation,Dropout
# from tensorflow.keras.optimizers import SGD

# lemmatizer =  WordNetLemmatizer()

# intents = json.loads(open('intent.json').read())

# words = []
# classes = []
# document = []
# ignore_letters = ['.',',','?','!']



# for intent in intents['intents']:
#     for pattern in intent['pattern']:
#         word_list = nltk.word_tokenize(pattern)
#         words.extend(word_list)
#         document.append((word_list,intent['tag']))
#         if intent['tag'] not in classes:
#             classes.append(intent['tag'])
# print(document)