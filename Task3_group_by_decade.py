from Task1_IMDB import scrapped
from Task2_group_by_year import dec
import json

def group_by_decade(movies):
    moviedec={}
    list1=[]
    for i in movies:
        mod=i%10
        decade=i-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()

    for i in list1:
        moviedec[i]=[]
    
    for i in moviedec:
        dec10=i+9
        for j in movies:
            if j>=i and j<= dec10:
                for k in movies[j]:
                    moviedec[i].append(k)
        # return moviedec
    with open("Task3_group_by_decade.json","w") as g:
        json.dump(moviedec,g, indent=4)

print(group_by_decade(dec))