from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
titles = soup.find(class_="titleline")
points = soup.find_all(class_="score")
 
for point in points:
    print(point.get_text())