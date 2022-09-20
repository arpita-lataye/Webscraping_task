import requests
from bs4 import BeautifulSoup
import json
from Task1_IMDB import scrapped

def scrapped_movie_details(url1,name):
    advanture_url=url1
    advanture_api=requests.get(advanture_url)
    # print(advanture_api.content)
    soup=BeautifulSoup(advanture_api.text,"html.parser")
    # print(soup)
    table_tag=soup.find("ul",class_="content-meta info")
    # print(table_tag)
    li=table_tag.find_all("li",class_="meta-row clearfix")
    movie_dict={}

    for i in li:
        dict1=i.find("div",class_="meta-label subtle").text.strip()
        dict2=i.find("div",class_="meta-value").text.replace(" ","").replace("\n","").strip()
        movie_dict[dict1]=dict2
        movie_dict["name"]=name

    with open ("Task4_movie_details.json","w") as g:
        json.dump(movie_dict,g,indent=4)
    return movie_dict


for j in scrapped:
    url1=scrapped[0]['movie_url']
    name=scrapped[0]['movie_name']

scrapped_movie_details(url1,name)