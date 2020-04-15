
import gcsfs
import pandas as pd

# of course is not necessary to write in csv, you can upload straight to GCS

# CREDENTIALS
fs = gcsfs.GCSFileSystem(token='your creds name.json' ,project='your project in gcs')

# upload the new final keywords
with fs.open('bucket in gcs/name of the csv.csv') as mergekey:
    df = pd.read_csv(mergekey)
fs.upload("../tmp/keywords_new.csv",'bucket in gcs/name of the csv.csv') # it looks redundant but it's how it works