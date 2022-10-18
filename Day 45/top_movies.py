from dataclasses import dataclass
from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.imdb.com/list/ls068718974/")

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
titles = soup.find_all(class_="lister-item-header")

for title in titles:
    name_list = title.get_text().splitlines()
    space = " "
    names = space.join(name_list)
    
    with open("Day 45/Movies.txt", mode="a") as file:
        file.write(f"{names}\n")