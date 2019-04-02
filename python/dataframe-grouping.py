import pandas as pd
import numpy as np

'''Using generators to create Dictionary as String, List with different lengths'''
df = pd.DataFrame({ 'A' : 1,
                'B1' : pd.Timestamp('20130102'), 
                'B2' : pd.date_range('20130101', periods=4), 
                'C' : pd.Series(1, index=list(range(4)), dtype='float32'), 
                'D' : np.array([3] * 4,dtype='int32'), 
                'E' : pd.Categorical(["test","train","test","train"]) })
print(df, df.info(), df.index)

'''Create group'''
by_E = df.groupby(['E'])
print(by_E.groups)

'''Apply aggregates to group'''
sum_D_by_E = by_E.D.sum()
print(sum_D_by_E)

'''Restore back to dataframe'''

df1 = pd.DataFrame(sum_D_by_E).reset_index()
print(df1)
