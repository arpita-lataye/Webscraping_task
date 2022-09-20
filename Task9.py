import json
import random
import os
import  time
from Task4 import scrapped_movie_details
from Task1_IMDB import scrapped


def movie_list():
    for i in range(10):
        ab=scrapped[i]['movie_url']
        Url=scrapped[i]["movie_url"][33:]
        NAME=scrapped[i]["movie_name"]

        uRL="/home/oem/Desktop/WEB_SCRAPING/"+Url+".json"
        file=os.path.exists(uRL)
        if file==True:
            with open(file,"r") as f:
                a=json.load(f)
                # print(a)

        else:
            print('file doesnt exists')
            data=scrapped_movie_details(ab, NAME)

            r=random.randint(1,3)
            time.sleep(r)
            with open (uRL,"a") as x:
                json.dump(data,x,indent=4)

movie_list()