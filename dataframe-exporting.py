'''Export Dataframe'''

import pandas as pd
import numpy as np

'''To JSON'''
dfj = pd.DataFrame(np.random.randn(5, 2), columns=list('AB'))

'''
orient: format of JSON string

split	dict like {index -> [index], columns -> [columns], data -> [values]}
records	list like [{column -> value}, ... , {column -> value}]
index	dict like {index -> {column -> value}}
columns	dict like {column -> {index -> value}}
values	just the values array
'''
#default
json = dfj.to_json()
print(json, end='\n'+'-'*10+'\n')
json = dfj.to_json(orient='split')
print(json, end='\n'+'-'*10+'\n')
json = dfj.to_json(orient='records')
print(json, end='\n'+'-'*10+'\n')
json = dfj.to_json(orient='index')
print(json, end='\n'+'-'*10+'\n')
json = dfj.to_json(orient='columns')
print(json, end='\n'+'-'*10+'\n')
json = dfj.to_json(orient='values')
print(json, end='\n'+'-'*10+'\n')