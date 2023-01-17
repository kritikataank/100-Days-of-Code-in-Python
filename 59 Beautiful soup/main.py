from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="span", class_="titleline")
points = soup.find_all(name="span", class_="score")

for article in articles:
    print(article.getText())

point = [score.getText() for score in points]
print(point)

pt = [int(point[point.index(i)].split()[0]) for i in point]
print(pt)

largest_vote = max(pt)
largest_index= pt.index(largest_vote)
print(articles[largest_index])
print(largest_vote)

# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
#
# all_anchor_tags = soup.find_all(name= "a")
#
# for tags in all_anchor_tags:
#     print(tags.getText())
#     print(tags.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading.getText())
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
# print(section_heading.name)
# print(section_heading.get("class"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector='#name')
# print(name)
#
# headings = soup.select_one(selector=".heading")
# print(headings)
