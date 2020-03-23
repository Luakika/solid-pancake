# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 14:07:41 2020

@author: alex.a.murray
"""

import numpy as np
import pandas as pd

s = pd.Series([1,3,5, np.nan, 6, 8])



#Index as rows
#Columns as columns 

dates = pd.date_range('20130101', periods = 7)

df = pd.DataFrame(np.random.randn(7,5), index=dates, columns = list ('ABCDE'))

print(df)

# Organizing dataframe with multiple data types
df2= pd.DataFrame({'A':1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'), 
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

##### Viewing Data
# See the top index rows
df.head()

# See the last index rows
df.tail(3)

#Display index / column levels
df.index
df.columns

# See array of floats
df.to_numpy

# NumPy arrays have one dtype for the entire array, while pandas DataFrames have one dtype per column
# dataframe with multiple datatypes
df2.to_numpy()


#Transpose
df.T

# Five number summary
df.describe()


# Sort by axis
df.sort_index(axis=1, ascending=False)
# Sort by values
df.sort_values(by='B')

# Getting
df['A']


#Setting 
s1 = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20130102', periods=6))
s1

df['F'] = s1

#Setting values by label
df.at[dates[0], 'A'] = 0

#setting values by position
df.iat[0,1] = 0

# Setting by assigning with a NumPy array
df.loc[:, 'D'] = np.array([5] * len(df))

df

df2 = df.copy()

df2[df2 > 0] = -df2

df2

df1 = df.reindex(index)


# Plural maker
def plural(word):
    if word.endswith('y'):
        return word[:-1] + 'ies'
    elif word[-1] in 'sx' or word[-2:] in ['sh', 'ch']:
        return word + 'es'
    elif word.endswith('an'):
        return word[:-2] + 'en'
    else:
        return word + 's'
