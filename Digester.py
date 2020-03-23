# -*- coding: utf-8  -*-
"""
Created on Tue Mar 10 15:00:48 2020

@author: alex.a.murray
"""

# Load Text
import nltk
import pandas

file = "C:/Rasa/Python Files/rasa_training/training_data_generation/master_data/raw_master_training_data_intent.csv"

df = pandas.read_csv(file)

# Just Get Words
def tokenizer(data):
    phrase_tokens= []
    for i in data.index:
        phrase_tokens += nltk.word_tokenize(df.loc[i, "UTTERANCE"])
    return phrase_tokens


def Token_Intent(data):
    phrase_temp = []
    phrase_final= []
    phrase_intent= []
    
    for i in data.index:
        phrase_temp = []
        phrase_temp += nltk.word_tokenize(df.loc[i, "UTTERANCE"])
        
        for tok in phrase_temp:
            phrase_intent.append(df.loc[i, "INTENT"])
            phrase_final = pandas.DataFrame(phrase_intent, phrase_temp)
   
    return phrase_final



#tokens = nltk.word_tokenize(text)