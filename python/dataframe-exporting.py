'''Export Dataframe'''

import pandas as pd
import numpy as np

kwargs = {
  'index': False,
}

df = pd.DataFrame(np.random.randn(5, 2), columns=list('AB'))

'''To CLIPBOARD'''
dfclip = df.copy()
dfclip.to_clipboard()

'''to CSV'''
from csv import QUOTE_NONE, QUOTE_ALL, QUOTE_NONNUMERIC, QUOTE_MINIMAL # QUOTE_MINIMAL is default
csv_kwargs = dict(quoting=QUOTE_ALL,)
csv_kwargs.update(kwargs)

dfcsv = df.copy()
csv_in_string = dfcsv.to_csv(None, csv_kwargs)


'''To JSON'''
dfj = df.copy()

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

#date handling


'''to EXCEL'''

