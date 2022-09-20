import json 
from bs4 import BeautifulSoup 
import requests
import os
from Task1_IMDB import scrapped
from Task4 import scrapped_movie_details

def scrapped_new_movie_details(URL):
    for i in scrapped:
        if i["movie_url"]==URL:
            Url=i["movie_url"][33:]
            NAME=i["movie_name"]

            file= os.path.exists("/home/oem/Desktop/WEB_SCRAPING/"+Url+".json")
            if file ==True:
                with open (file,"r") as f:
                    a=json.load(f)

            else:
                print("file doesnt Exist")
                data=scrapped_movie_details(i["movie_url"], NAME)

                with open ("Task8_movie_details.json","w") as m:
                    json.dump(data,m,indent=4)

                return data

URL1=scrapped[1]["movie_url"]
scrapped_new_movie_details(URL1)