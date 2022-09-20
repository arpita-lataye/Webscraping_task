import json
from Task5 import all_movies

def analyse_movies_directors(movie_details_list):
    dict1={}
    for i in movie_details_list:
        count=0
        for j in movie_details_list:
            if i["Director:"]==j["Director:"]:
                count=count+1
        dict1.update({i["Director:"]:count})

    with open ("Task7_directors_analyse.json","w") as file:
        json.dump(dict1,file, indent=4)

    return dict1

analyse_movies_directors(all_movies)