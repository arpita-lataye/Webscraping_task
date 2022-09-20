import requests
from bs4 import BeautifulSoup
import json
from Task1_IMDB import scrapped

def scrape_movie_cast(api):
    list1=[]
    response=requests.get(api)
    # print(response.content)
    soup=BeautifulSoup(response.text,"html.parser")
    # print(soup)
    table=soup.find("div",class_="castSection")
    # print(table)
    tr=table.find_all("div",class_="cast-item media inlineBlock")

    for i in tr[1:]:
        url=i.find("a",class_="unstyled articleLink")
        link1=url.get_text()
        link=url["href"]
        name=i.find("span")
        Name=name.get_text().strip()
        dict1={}
        dict1["url"]=link
        dict1["name_of_actor"]=Name

        list1.append(dict1)

    with open("Task12_movie_cast.json","w") as file:
        json.dump(list1,file,indent=4)

    return list1

api=scrapped[0]["movie_url"]
scrape_movie_cast(api)