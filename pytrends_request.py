import os
import gcsfs
import pandas as pd
import random
import pytrends
from pytrends.request import TrendReq

import time as timer 
import datetime
from datetime import datetime, date, time, timedelta


#--------------------------------------
# date example for periodical request
#--------------------------------------
yesterday=(datetime.now()-timedelta(days=1)).date()
week_ago=(datetime.now()-timedelta(days=8)).date()
dates=str(week_ago) + " " + str(yesterday) 

#--------------------------------------
# keywords (no more than 5 in the same sublist, and read perfectly the documentation of pytrends!)
#--------------------------------------
keywords1=[
    ["keyword"],category_code,
    ["keyword"],category_code,
    ["and so on"],category_code,
]
keywords2=[
    '''more keywords'''
]
#--------------------------------------
# the function
#--------------------------------------
def tracking_in_time_keywords(kw_list):
    pytrends = TrendReq(hl='country', tz=<timezone you want>)
    future_dataframe={}
    c=1
    for i in range(len(kw_list)):
        if i%2==0:
        
            try:
                print("Requesting ",str(kw_list[i]))
                pytrends.build_payload(kw_list[i], cat=kw_list[i+1],timeframe=dates, geo='country', gprop='')
                
                future_dataframe[c]=pytrends.interest_over_time() 
                future_dataframe[c].drop(['isPartial'], axis=1,inplace=True)
                c+=1
                result = pd.concat(future_dataframe, axis=1)

                # this is for intense use of the script, remove it to avoid Cloud Function timeout (and save money)
                secs=int(random.randrange(10, 50))
                print("Sleeping {} seconds before requesting ".format(secs),str(kw_list[i]))
                timer.sleep(secs)
                print("Done")

            except:
                print("***","\n","Error with ",kw_list[i],"or not enough trending percentaje","\n","***")
    
    result.columns = result.columns.droplevel(0)
    df1=result.unstack(level=-1)
    df2=pd.DataFrame(df1)
    df2.reset_index(inplace=True)
    df2.columns = ["keyword","date","trend_index"]
    return df2


#--------------------------------------
# applying the function to create all csvs you want
#--------------------------------------
new_df_keywords = tracking_in_time_keywords(keywords)
new_df_keywords.to_csv(os.getenv("PROJECT_TMP"))    # you can use also os.environ() 
'''new_df_keywords_2 = tracking_in_time_keyword( ..)'''