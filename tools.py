#!/usr/bin/env python

'''
You have a pandas data Series of strings and you want to convert it to a list of json objects.
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
update column in dataframe with another dataframe
'''

def updatecol(_df1,_df2):
    
    _df1.set_index('author_id',inplace=True)
    _df2.set_index('retweeted_user_id',inplace=True)
    _df2.update(_df1)
    
    _df1.reset_index(inplace=True)
    _df2.reset_index(inplace=True)
    return _df2