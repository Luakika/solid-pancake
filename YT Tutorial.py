# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 12:49:39 2020

@author: alex.a.murray
"""
import nltk 
from nltk.corpus import state_union
from nltk import PunktSentenceTokenizer


train_text = state_union.raw("2005-GWBush.text")
sample_text = state_union.raw("2006-GWBush.txt")

custom_sent_tokenizer = PunktSentenceTokenizer(train_text)
tokenized = custom_sent_tokenizer.tokenize(sample_text)


def process_content():
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            print(tagged)
            
    except Exception as e:
            print(str(e))
            
process_content