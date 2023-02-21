from botometer import Botometer
import pandas as pd
from tqdm import tqdm



if __name__=='__main__':

    
    rapidapi_key=''

    twitter_app_auth = {
    "consumer_key" : "",
    "consumer_secret" : "",
    "access_token": "",
    "access_token_secret": ""
    }
    
    bom = Botometer(wait_on_ratelimit=True,
                            rapidapi_key=rapidapi_key,
                            **twitter_app_auth)



    coretweet_60s=pd.read_csv('../Project7/analysis/text.csv')#text.csv is from gephi

    users=coretweet_60s[coretweet_60s.sort_values(['indegree'],ascending=False)['indegree']>100]['d0'].tolist()


    i=1
    for user,result in tqdm(bom.check_accounts_in(users)):
        print(result)
        if "error" not in result:
            df=pd.json_normalize(result)
            if i==1:
                df.to_csv('../Project7/Botscore.csv',index=None,mode='a')
            else:
                df.to_csv('../Project7/Botscore.csv',index=None,mode='a',header=None)
            i+=1