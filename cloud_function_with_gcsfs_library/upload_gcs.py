import os
import gcsfs
import pandas as pd

# of course is not necessary to write in csv, you can upload straight to GCS

# you can use this very code. In Google Cloud, advanced, change the environment variables
# TOKEN NAME, TOKEN PATH... By the location of your token and paths. Write them without 
# declaring they're string (without " ")

# CREDENTIALS
fs = gcsfs.GCSFileSystem(token=os.getenv("TOKEN_NAME"), project=os.getenv("PROJECT_NAME"))


# Write in GCS.
with fs.open(os.getenv("PROJECT_PATH")) as uploading_keywords:
    df = pd.read_csv(uploading_keywords)
fs.upload("PROJECT_TMP",os.getenv("PROJECT_PATH"))
