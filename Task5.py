from Task1_IMDB import scrapped
from Task4 import scrapped_movie_details
import json

def get_movie_list_details(movies_list):
    list1=[]
    for j in movies_list:
        list1.append(j)
        if j["movie_rank"]=="10":
            break

    link_url={}
    for k in list1:
        link_url.update({k['movie_url']:k['movie_name']})

    list2=[]
    for a,b in link_url.items():
        u=scrapped_movie_details(a,b)
        list2.append(u)
    with open("Task5_movie_information.json","w") as myfile:
        json.dump(list2,myfile,indent=4)

    return list2  

all_movies=get_movie_list_details(scrapped)