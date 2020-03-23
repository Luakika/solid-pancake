# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 16:41:06 2019

@author: candice.l.penelton
"""

import sys
import csv
from os import path,listdir,getcwd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# example command line arguments
new_data_dir = "C:/Rasa/converse-3.0.0-rasa_training/models/new_utterances.csv"
training_data_dir = "C:/Rasa/converse-3.0.0-rasa_training/training_data_generation/master_data/raw_master_training_data_intent.csv"
out_file = "cosine_scores.csv"

min_score = 0

def get_all_scores(training_df, new_data, min_score):
    #Create the Document Term Matrix
    vectorizer = CountVectorizer()
    # vectorizer = TfidfVectorizer()
    
    score_data = []
    
    # this is to avoid having duplicate pairs like "A,B", "B,A" if comparing 
    # the training data set to it self
    pair_dict = {}
    
    for new_utterance in new_data:
        # Create tf-idf scores for data set including the new example
        training_utterances = list(training_df["UTTERANCE"])
        temp_data = [new_utterance] + training_utterances
        doc_matrix = vectorizer.fit_transform(temp_data)
        index = 0
        
        pair_dict[new_utterance] = set()
        
        # Get the cosine score and match the score to the utterance and intent 
        for score in cosine_similarity(doc_matrix[0],doc_matrix[1:])[0]:
            utterance = training_df.loc[index,'UTTERANCE']
            reverse_pair = False
            
            # avoid adding data B A pair if A B in data already
            if utterance in pair_dict.keys():
                if new_utterance in pair_dict[utterance]:
                    reverse_pair = True
                        
            if score > min_score and utterance != new_utterance and not reverse_pair:
                    intent = training_df.loc[index,'INTENT']
                    data_item = [new_utterance,utterance,intent,float(score)]
                    score_data.append(data_item)
                    pair_dict[new_utterance].add(utterance)
            
            index += 1
    
    return score_data
            
def get_top_scores(training_df, new_data):
    #Create the Document Term Matrix
    vectorizer = CountVectorizer()
    # vectorizer = TfidfVectorizer()
    
    score_data = []
    
    # this is to avoid having duplicate pairs like "A,B", "B,A" if comparing 
    # the training data set to it self
    pair_dict = {}
    
    for new_utterance in new_data:
        # Create tf-idf scores for data set including the new example
        training_utterances = list(training_df["UTTERANCE"])
        temp_data = [new_utterance] + training_utterances
        doc_matrix = vectorizer.fit_transform(temp_data)
        index = 0
        
        pair_dict[new_utterance] = set()
        min_score = 0.0
        
        # Get the cosine score and match the score to the utterance and intent 
        for score in cosine_similarity(doc_matrix[0],doc_matrix[1:])[0]:
            utterance = training_df.loc[index,'UTTERANCE']
            reverse_pair = False
            
            # avoid adding data B A pair if A B in data already
            if utterance in pair_dict.keys():
                if new_utterance in pair_dict[utterance]:
                    reverse_pair = True
                        
            if score > min_score and utterance != new_utterance and not reverse_pair:
                    intent = training_df.loc[index,'INTENT']
                    data_item = [new_utterance,utterance,intent,float(score)]
                    pair_dict[new_utterance].add(utterance)
                    min_score = score
            
            index += 1
        
        
        score_data.append(data_item)
    
    return score_data

def write_score_data(score_data, out_file):
    # Save file
    result_header = ["NEW_UTTERANCE","TRAINING_UTTERANCE","INTENT","COSINE_SCORE"]
    cosine_df = pd.DataFrame(score_data,columns=result_header)
    cosine_df = cosine_df.sort_values(by=["COSINE_SCORE"],ascending=False)
    cosine_df.to_csv(out_file)

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

#new_data_dir = sys.argv[1]
#training_data_dir = sys.argv[2]
#out_file = sys.argv[3]    
    
# example command line arguments
# new_data_dir = "full_training_data\\masterbot\\raw_master_training_data_intent.csv"
# training_data_dir = "full_training_data\\masterbot\\raw_master_training_data_intent.csv"
# out_file = "cosine_scores.csv"

# Get data
new_data_dir = path.join(getcwd(),new_data_dir)
new_df = pd.read_csv(new_data_dir)
new_data = list(new_df["UTTERANCE"])

training_data_dir = path.join(getcwd(),training_data_dir)
training_df = pd.read_csv(training_data_dir)
training_df = training_df[["INTENT","UTTERANCE"]]
training_df = training_df.reset_index()

score_data = []

if is_float(sys.argv[4]):
    min_score = float(sys.argv[4])
    score_data = get_all_scores(training_df, new_data, min_score)
    write_score_data(score_data, out_file)
elif sys.argv[4] == 'top':
    score_data = get_top_scores(training_df, new_data)
    write_score_data(score_data, out_file)
else:
    print("Missing or invalid parameter")
   


