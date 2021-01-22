# Activate this first line and the last one when it works as you want.

#from google.cloud import storage
#---------------------------------

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
# 
#--------------------------------------
keywords=["keyword1", "keyword2", "keyword3", "...", "keyword 42"]

#--------------------------------------
# 
#--------------------------------------
pytrends = TrendReq(hl='ES', tz=0)
future_dataframe={}
c=1
for k in keywords:   

    try:
        pytrends.build_payload([k], timeframe=dates, geo='ES', gprop='')
        future_dataframe[c]=pytrends.interest_over_time() 
        future_dataframe[c].drop(['isPartial'], axis=1,inplace=True)
        c+=1
        result = pd.concat(future_dataframe, axis=1)
    except:
        print("***","\n","Error with ",k,"or not enough trending percentaje","\n","***")

result.columns = result.columns.droplevel(0)
df1=result.unstack(level=-1)
df2=pd.DataFrame(df1)
df2.reset_index(inplace=True)
df2.columns = ["keyword","date","trend_index"]


# this final line too
#df2.to_csv('gs://your bucket in GCS/the_csv_name_there.csv')
#-----------------
