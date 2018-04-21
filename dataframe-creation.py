'''creating Dataframes'''

import pandas as pd
import numpy as np
from io import StringIO
'''DataFrame is an object. It contains Series object as columns'''
s = pd.Series([1,3,5,np.nan,6,8])

'''Using datetime index for creating Dataframe using random values'''
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))

'''Using generators to create Dictionary as String, List with different lengths'''

df = pd.DataFrame({ 'A' : 1., 'B' : pd.Timestamp('20130102'), 'C' : pd.Series(1,index=list(range(4)),dtype='float32'), 'D' : np.array([3] * 4,dtype='int32'), 'E' : pd.Categorical(["test","train","test","train"]) })

'''
Format 	Data 				Reader - Writer
text	CSV					read_csv	to_csv
text	JSON				read_json	to_json
text	HTML				read_html	to_html
text	Local clipboard		read_clipboard	to_clipboard
binary	MS Excel			read_excel	to_excel
binary	HDF5 Format			read_hdf	to_hdf
binary	Feather Format		read_feather	to_feather
binary	Parquet Format		read_parquet	to_parquet
binary	Msgpack				read_msgpack	to_msgpack
binary	Stata				read_stata	to_stata
binary	SAS					read_sas	 
binary	Python Pickle Format read_pickle	to_pickle
SQL	SQL						read_sql	to_sql
SQL	Google Big Query		read_gbq	to_gbq
'''

'''From a CSV'''
data = 'col1,col2,col3\na,b,1\na,b,2\nc,d,3'
df = pd.read_csv(StringIO(data))

