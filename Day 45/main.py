from bs4 import BeautifulSoup
from requests import head

with open("Day 45/website.html", encoding='utf-8') as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.get("href"))


section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.get_text())

company_url = soup.select_one(selector="p a")
# print(company_url)

headings = soup.select(".heading")
print(headings)