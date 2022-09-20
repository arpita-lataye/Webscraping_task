import json
from Task5 import all_movies

def analyse_movies_language(movies_list1):
    language1={}
    for i in movies_list1:
        count=0
        for j in movies_list1:
            if i["Original Language:"]==j["Original Language:"]:
                count+=1
            language1.update({i["Original Language:"]:count})

    with open ("Task6_count_of_language.json","w") as d:
        json.dump(language1,d,indent=4)
    return language1

analyse_movies_language(all_movies)