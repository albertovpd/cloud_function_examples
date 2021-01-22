import os
from os import listdir
from os.path import isfile, join

def main (data,context):
    
    processes= ["pytrends_request.py","remove_files.py"] #,"upload_gcs_real.py",

    for p in processes:
        print(p)
        exec(open(p).read())

if __name__ == "__main__":
  
    main('data','context')