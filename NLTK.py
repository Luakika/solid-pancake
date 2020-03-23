# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 14:05:10 2020

@author: alex.a.murray
"""
# Returns instances and surround words
text3.concordance('lights')
#Returns words used in similar contexts
text3.similar('men')

# Plots instances of words by their place in the order of whole document
text3.dispersion_plot(['God', 'Monster', 'Eve'])

# Imput document
def lexical_diversity(text):
    return len(text)/ len(set(text))

def percentage(count, total):
    return 100 * count / total

percentage(text3.count('God'), len(text3))


Genesis = text3[0:11]
lexical_diversity(test)

# Frequency Distribution
freq = FreqDist(text3)

# Bigrams function
bi = bigrams(Genesis)

freq.plot(50, cumulative = TRUE)

# Cheat Sheet
fdist = FreqDist(samples) #Create a frequency distribution containing the given samples
fdist.inc(sample) #Increment the count for this sample
fdist['monstrous'] #Count of the number of times a given sample occurred
fdist.freq('monstrous') #Frequency of a given sample
fdist.N() #Total number of samples
fdist.keys() #The samples sorted in order of decreasing frequency
for sample in fdist: #Iterate over the samples, in order of decreasing frequency
fdist.max() #Sample with the greatest count
fdist.tabulate() #Tabulate the frequency distribution
fdist.plot() #Graphical plot of the frequency distribution
fdist.plot(cumulative=True) #Cumulative plot of the frequency distribution
fdist1 < fdist2 #Test if samples in fdist1 occur less frequently than in fdist2






