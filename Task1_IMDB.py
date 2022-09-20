from bs4 import BeautifulSoup
import requests
import json

def scrap_top_list():
    url= 'https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/'
    page=requests.get(url)

    # print(page.content)

    soup = BeautifulSoup(page.text,"html.parser")
    # print(soup
    main_div = soup.find("table",class_="table")
    # print(main_div)

    trs = main_div.find_all('tr')
    # print(trs)
    top_movie=[]
    
    for tr in trs[1:]:
        position=tr.find('td',class_="bold").get_text()
        # movie_name.append(position)
        rank=position
        movie_ratings=tr.find("span",class_="tMeterScore")
        rating=movie_ratings.get_text().strip()
        movie_name=tr.find("a",class_="unstyled articleLink")
        title=movie_name.get_text().strip()
        list=title.split()
        year=list[-1][1:5]
        year1=int(year)
        name_length=len(list)-1
        name=""
        for l in range(name_length):
            name=name+" "
            name=name+list[l]
        movieName=name
        movie_Reviews= tr.find("td",class_="right hidden-xs")
        reviews=movie_Reviews.get_text()
        url=tr.find("a",class_="unstyled articleLink")
        link=url.get_text()
        link=url["href"]
        movie_link="https://www.rottentomatoes.com"+link
        details={}
        details["movie_rank"]=rank
        details["movie_rating"]=rating
        details["movie_name"]=movieName
        details["movie_reviews"]=reviews
        details["movie_url"]=movie_link
        details["year"]=year1
        top_movie.append(details)
    with open("IMDB_top_movie1.json","w") as file:
        json.dump(top_movie,file,indent=4)
    return top_movie


scrapped=scrap_top_list()




# def IMDB_scrap_top_list():
#     url= 'https://www.rottentomatoes.com/top/bestofrt/top_100_action__adventure_movies/'
#     page=requests.get(url)

#     # print(page.content)

#     soup = BeautifulSoup(page.text,"html.parser")
#     # print(soup
#     main_div = soup.find("table",class_="table")
#     # print(main_div)

#     trs = main_div.find_all('tr')
#     # print(trs)
#     movie_ranks=[]
#     movie_name=[]
#     year_of_realese=[]
#     movie_urls=[]
#     movie_ratings=[] 

#     for tr in trs[1:]:
#         position=tr.find('td',class_="bold").get_text().strip()
#         # position=tr.find('td',class_="bold").get_text()
#         # movie_name.append(position)
#         rank=""
#         for i in position:
#             if '.' not in i:
#                 rank+=i
#             else:
#                 break
#         movie_ranks.append(rank)
#         # print(movie_ranks)

#         title = tr.find("a", class_="unstyled articleLink").get_text().strip()
#         movie_name.append(title)
#         # return movie_name
       
#         year=tr.find("a",class_="unstyled articleLink").get_text()
#         year_of_realese.append(year)
#         # return year_of_realese
#         imdb_rating=tr.find("span",class_="tMeterScore").get_text().strip()
#         movie_ratings.append(imdb_rating)
#         # return movie_ratings
        
#         link= tr.find("a", class_="unstyled articleLink").get_text()
#         link1=link["href"]
#         movie_link="https://www.imdb.com"+link1
#         movie_urls.append(movie_link)

#     top_movies=[]
#     details={"position":'',"name":'',"year":'',"rating":'',"url":''}
#     for i in range(0,len(movie_ranks)):
#         details['position']= int(movie_ranks[i])
#         details['name']=str(movie_name[i])
#         year_of_realese[i]=year_of_realese[i][1:5]
#         details['year']=int(year_of_realese[i])
#         details['rating']=float(movie_ratings[i])
#         details['url']=movie_urls[i]
#         top_movies.append(details.copy())
#     return top_movies

# print(IMDB_scrap_top_list())