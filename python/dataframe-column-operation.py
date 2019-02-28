# -*- coding: utf-8 -*-
"""
Created on Fri Sep  7 10:06:42 2018

@author: ZNevzz
"""
import pandas as pd
import numpy as np

'''Using datetime index for creating Dataframe using random values'''
dates = pd.date_range('20130101', periods=6)
df1 = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

df2 = pd.DataFrame({ 'A' : 1.,
                 'B' : pd.Timestamp('20130102'), 
                'C' : pd.Series(1,index=list(range(4)),dtype='float32'), 
                'D' : np.array([3] * 4,dtype='int32'), 
                'E' : pd.Categorical(["test","train","test","train"]) })
df = df1

'''all columns list'''

'''
checkout list vs np.array 
https://stackoverflow.com/questions/993984/what-are-the-advantages-of-numpy-over-regular-python-lists
'''
columns = list(df)
np_columns = df.columns.values


''' link: https://stackoverflow.com/questions/19482970/get-list-from-pandas-dataframe-column-headers '''
fastest_converted_to_list = df.columns.values.tolist()

'''select subset of columns'''
df = df2
columns = list(df)
df3 = df[columns[-2:]]

'''select columns using indexing'''
df_by_col_indices = df.loc[:-2])
df_by_col_names = df.loc['B':'D']
'''select columns using indexing, Pandas Object vs Copy of Pandas Object https://realpython.com/copying-python-objects/ https://pandas.pydata.org/pandas-docs/version/0.22/generated/pandas.DataFrame.copy.html'''
df4 = df.iloc[:, -2:]

'''apply operation on all columns '''
X_num = df.copy()
# Scaling the numeric features using standardization
X_num = (X_num - X_num.mean()) / X_num.std()
X_num = X_num.fillna(X_num.mean())
X_num.head()
