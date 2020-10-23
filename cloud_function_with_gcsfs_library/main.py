import runpy
import os

def main (data,context):


    #--------------------------------------
    processes= ("pytrends_request.py","upload_gcs.py","remove_files.py")

    for p in processes:
        exec(open(p).read())
        print(p," done.")

if __name__ == "__main__":
  
    main('data','context')
 