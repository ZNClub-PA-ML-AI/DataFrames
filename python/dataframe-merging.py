'''dataframe merge operations in Python'''

import pandas as pd
import numpy as np


## without index

df1 = pd.read_csv('../data/source1.csv')
df2 = pd.read_csv('../data/source2.csv')
print(df1.shape, df2.shape)

pandas_merged = pd.merge(left=df1, right=df2, on='id')

dataframe_merged = df1.merge(right=df2, on='id')


## with specifying index

'''break major df into n minor dfs and join using index '''
total_values = 3
a = ['A'+str(i) for i in range(total_values)]
b = ['B'+str(i) for i in range(total_values)]
c = ['C'+str(i) for i in range(total_values)]
dataset = list(zip(a,b))
df1 = pd.DataFrame(data = dataset,
	columns = ['A','B'], index = a
	)
dataset = list(zip(a,c))
df2 = pd.DataFrame(data = dataset,
	columns = ['A','C'], index = a
	)
print(df1)
print('-'*20)
print(df2)
print('-'*20)

not_so_good = pd.concat([df1, df2], axis=0)
'''not_so_good dataframe created'''
print(not_so_good)
print('-'*20)


'''
     A   B
A0  A0  B0
A1  A1  B1
A2  A2  B2
--------------------
     A   C
A0  A0  C0
A1  A1  C1
A2  A2  C2
--------------------
     A    B    C
A0  A0   B0  NaN
A1  A1   B1  NaN
A2  A2   B2  NaN
A0  A0  NaN   C0
A1  A1  NaN   C1
A2  A2  NaN   C2
--------------------

'''

'''divide not_so_good into n minors and concat them column wise'''
df3 = not_so_good[['A','B']].dropna()
df3.set_index('A')
df4 = not_so_good[['A','C']].dropna()
df4.set_index('A')
print(df3)
print('-'*20)
print(df4)
print('-'*20)

# much_better = pd.concat([df3, df4], axis = 1)
# much_better = pd.concat([df3, df4], axis = 1, join = 'inner')
much_better = pd.concat([df3, df4], axis =1 , join_axes = [df3.index])
print(much_better)
print('-'*20)
'''
     A   B
A0  A0  B0
A1  A1  B1
A2  A2  B2
--------------------
     A   C
A0  A0  C0
A1  A1  C1
A2  A2  C2
--------------------
     A   B   A   C
A0  A0  B0  A0  C0
A1  A1  B1  A1  C1
A2  A2  B2  A2  C2
--------------------
'''
''' 
# IMPROVEMENTS
1. In much_better, column 'A' is getting repeated. Why?
--> Because much_better is a dataframe of concatenation of two other dataframes
    along the columns.Concatenation of two dataframes won't drop-off the common
    column.If you want to drop the common column,try merging them instead of
    concatenation.
'''
much_better=pd.merge(df3,df4,how='inner')  #Performs the inner join of two dataframes
print('-'*20)
print(much_better)
print('-'*20)
'''
--------------------
    A   B   C
0  A0  B0  C0
1  A1  B1  C1
2  A2  B2  C2
--------------------
'''

'''
2. Can this entire logic be written in R?
--> Refer the R code attached.  
'''
