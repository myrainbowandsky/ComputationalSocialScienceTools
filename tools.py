#!/usr/bin/env python

'''
1. You have a pandas data Series of strings and you want to convert it to a list of json objects.
input: pandas Series of strings
output: pandas Series of json objects
'''
import json
def ser2json(_str):
    if type(_str) == float:
        pass
    else:    
        return (json.loads(_str))

'''
2. update column in dataframe with another dataframe
'''
def updatecol(_df1,_df2):
    
    _df1.set_index('author_id',inplace=True)
    _df2.set_index('retweeted_user_id',inplace=True)
    _df2.update(_df1)
    
    _df1.reset_index(inplace=True)
    _df2.reset_index(inplace=True)
    return _df2


def float2int(_str):
    if type(_str) == None:
        pass
    else:    
        return (int(_str))

'''
reading when converting data
'''
import pandas as pd
in_reply_user = pd.read_csv('../Project6/data/in_reply_to_screen_name.csv',converters={'Unnamed: 0': str})

'''
domains extractor
'''
import tldextract
    
def domain4(_url):
    
    if type(_url) == str:
  
        _ext = tldextract.extract(_url)

        return  _ext.registered_domain
    else: 
        return None

 
def concatdf(path,files):
    DF=pd.DataFrame()
    for i in range(len(files)):
        each = files[i]
        df=pd.read_csv(path+each)
        print(df.shape)
        DF=pd.concat([DF,df])
        
    return DF

## concat 'text by username
df.groupby(by='name').agg(text=("text", lambda x: ",".join(set(x))))