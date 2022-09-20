from Task5 import all_movies
import json

def analyse_language_and_directors(movies_list):
    director={}
    for i in  all_movies:
        count=0
        for j in all_movies:
            if i["Director:"]==j["Director:"]:
                if i['Original Language:']==j["Original Language:"]:
                    count+=1
            
            director.update({i["Director:"]:{i["Original Language:"]:count}})

    with open("Task10_language.json","w") as d:
        json.dump(director,d,indent=4)

    return director

analyse_language_and_directors(all_movies)