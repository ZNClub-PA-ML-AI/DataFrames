'''creating Dataframes'''

import pandas as pd
import numpy as np
from io import StringIO
from pandas.io.json import json_normalize
import json

'''DataFrame is an object. It contains Series object as columns'''
s = pd.Series([1,3,5,np.nan,6,8])

'''Using datetime index for creating Dataframe using random values'''
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

'''Using generators to create Dictionary as String, List with different lengths'''

df = pd.DataFrame({ 'A' : 1.,
                 'B' : pd.Timestamp('20130102'), 
                'C' : pd.Series(1,index=list(range(4)),dtype='float32'), 
                'D' : np.array([3] * 4,dtype='int32'), 
                'E' : pd.Categorical(["test","train","test","train"]) })

'''
Format     Data                 Reader - Writer
text    CSV                    read_csv    to_csv
text    JSON                read_json    to_json
text    HTML                read_html    to_html
text    Local clipboard        read_clipboard    to_clipboard
binary    MS Excel            read_excel    to_excel
binary    HDF5 Format            read_hdf    to_hdf
binary    Feather Format        read_feather    to_feather
binary    Parquet Format        read_parquet    to_parquet
binary    Msgpack                read_msgpack    to_msgpack
binary    Stata                read_stata    to_stata
binary    SAS                    read_sas     
binary    Python Pickle Format read_pickle    to_pickle
SQL    SQL                        read_sql    to_sql
SQL    Google Big Query        read_gbq    to_gbq
'''

'''From CSV'''
data = 'col1,col2,col3\na,b,1\na,b,2\nc,d,3'
df = pd.read_csv(StringIO(data))

data = 'col1;col2;col3\na;b;1\na;b;2\nc;d;3'
df = pd.read_csv(StringIO(data), sep=";")

example = {'first_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'], 
        'last_name': ['Miller', 'Jacobson', ".", 'Milner', 'Cooze'], 
        'age': [42, 52, 36, 24, 73], 
        'preTestScore': [4, 24, 31, ".", "."],
        'postTestScore': ["25,000", "94,000", 57, 62, 70]}
df = pd.DataFrame(example, columns = ['first_name', 'last_name', 'age', 'preTestScore', 'postTestScore'])
df.to_csv('example.csv')

'''without index'''
df = pd.read_csv('example.csv')

'''without headers'''
df = pd.read_csv('../data/example.csv', header=None)

'''with new column names'''
df = pd.read_csv('../data/example.csv', names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])

'''??drop headers and new column names'''

df = pd.read_csv('../data/example.csv', 
                 index_col=['First Name', 'Last Name'], 
                 names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'])
#fails
df = pd.read_csv('../data/example.csv', 
                 names=['UID', 'First Name', 'Last Name', 'Age', 'Pre-Test Score', 'Post-Test Score'],
                 index_col=['First Name', 'Last Name'], 
                 na_values=['.'])
#pd.isnull(df)


'''replace NA with defaul'''
sentinels = {'Last Name': ['.', 'NA'], 'Pre-Test Score': ['.']}
df = pd.read_csv('../data/example.csv', na_values=sentinels)

'''skip first n rows'''
df = pd.read_csv('../data/example.csv', skiprows=3)

'''include only first n rows'''
df = pd.read_csv('../data/example.csv', nrows=3)

'''replace , in string and convert to numeric'''
df = pd.read_csv('../data/example.csv', thousands=',')


'''From JSON'''
'''
split    dict  like {index -> [index], columns -> [columns], data -> [values]}
records    list like [{column -> value}, … , {column -> value}]
index    dict  like {index -> {column -> value}}
columnsdict like {column -> {index -> value}}
values    just the values array
table          adhering to the JSON Table Schema
'''

split_data = """
{"columns":["col 1","col 2"],
  "index":["row 1","row 2"],
  "data":[["a","b"],["c","d"]]}
"""
df = pd.read_json(split_data, orient='split')

index_data = """
{"row 1":{"col 1":"a","col 2":"b"},"row 2":{"col 1":"c","col 2":"d"}}
""" 
df = pd.read_json(index_data, orient='index')
'''default'''
df = pd.read_json(index_data)

columns_data = """
{"col 1":{"row 1":"a","row 2":"b"},"col 2":{"row 1":"c","row 2":"d"}}
""" 
df = pd.read_json(columns_data, orient='columns')

records_data = """
[{"col 1":"a","col 2":"b"},{"col 1":"c","col 2":"d"}]
"""
df = pd.read_json(records_data, orient='records')

values_data = """
[["a","b"],["c","d"]]
"""
df = pd.read_json(values_data, orient='values')

table_data = """
{"schema": {"fields": [{"name": "index", "type": "string"},
                        {"name": "col 1", "type": "string"},
                        {"name": "col 2", "type": "string"}],
                "primaryKey": "index",
                "pandas_version": "0.20.0"},
    "data": [{"index": "row 1", "col 1": "a", "col 2": "b"},
            {"index": "row 2", "col 1": "c", "col 2": "d"}]}
"""
''' not available in version '0.18.1' '''
#df = pd.read_json(table_data, orient='table')

unnormalized_json = """
[{'id': 1, 'name': {'first': 'Coleen', 'last': 'Volk'}},
{'name': {'given': 'Mose', 'family': 'Regner'}},
{'id': 2, 'name': 'Faye Raker'}]
"""
#df = json_normalize(json.load(unnormalized_json))


## ADD ON
obj = {"name":"is unique"}
to_json = json.dumps(obj)
from_json = json.loads(to_json)


'''From XLSX/ XLS'''

df = pd.read_csv('../data/example.csv', names=[0,1,2,3,4])
df.to_excel('../data/example.xlsx')
df.to_excel('../data/example.xls')

df = pd.read_excel('../data/example.xlsx', sheet=0)

# Import the excel file and call it xls_file
xls_file = pd.ExcelFile('../data/example.xls')
xls_file.sheet_names
df = xls_file.parse('Sheet1')