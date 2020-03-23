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
df2= pd.DataFrame({'A':1.,
                    'B': pd.Timestamp('20130102'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'), 
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})

df.head()
df.tail(3)

df.to_numpy()
df2.to_numpy()

df.T