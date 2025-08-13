import requests
from bs4 import BeautifulSoup

response=requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')
website=response.text

soup=BeautifulSoup(website,'html.parser')

movies=[title.getText() for title in soup.find_all(name='h3',class_='title')]

ordered_movies=movies[::-1]
with open('movies_list.txt','w',encoding="utf-8") as file:
    for movies in ordered_movies:
        file.write(f"{movies}\n")
