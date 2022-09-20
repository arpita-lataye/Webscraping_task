from Task13 import cast
import json

def analyse_co_actors(cast):
    list=[]
    for i in cast:
        list1=[]
        for j in i["cast"]:
            list1.append(j["name_of_actor"])
        list.append(list1)
        dic={}
        for i in list:
            for j in i:
                count=0
                for s in i:
                    if s==j:
                        d=j
                        i.remove(d)
                        dic.update({j:i})
                        count+=1
        print(dic)
        
        with open ("Task14_co_actors.json","w") as file:
            json.dump(dic,file,indent=4)

analyse_co_actors(cast)