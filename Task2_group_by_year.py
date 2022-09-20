from Task1_IMDB import scrapped
import json

def group_by_year(movies):
    years=[]
    for i in movies:
        year=i['year']
        if year not in years:
            years.append(year)
    movie_dict={}
    for j in years:
        movie_dict.update({j:[]})
    for i in movies:
        year=i['year']
        movie_dict[year].append(i)
    with open("movie_by_year.json","w") as d:
        json.dump(movie_dict,d,indent=4)

    return movie_dict

dec=group_by_year(scrapped)