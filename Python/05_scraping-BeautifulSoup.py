import requests
import pandas as pd
import time
from bs4 import BeautifulSoup
url = "http://www.allocine.fr/"
r = requests.get(url)
print(url, r.status_code)
soup = BeautifulSoup(r.content, "lxml")

# for p in soup.find_all("a"):
#     print(p.text)
title = []
synopsis = []
links = []
target_syp = None

for elem in soup.find_all("a", class_="meta-title meta-title-link"):
    links.append(elem.get("href"))

movie_links = ["http://www.allocine.fr" + elem for elem in links if "film" in elem]

for links in movie_links:

    r = requests.get(links)
    soup = BeautifulSoup(r.content, "lxml")

    for elem in soup.find_all("div", class_="titlebar-title titlebar-title-xl"):
        title.append(elem.text)

    for elem in soup.find_all("div", class_="content-txt"):  # ------------------→ J'ai galéré comme pas permis
        if elem.find("p", class_="bo-p"):
            target_syp = elem

    if target_syp:
        synopsis.append(target_syp.text)

print("Total titles:", len(title))
print("Total synopsis:", len(synopsis))
print("Total movie links:", len(movie_links))

df = pd.DataFrame({"Title": title})
df["Synopsis"] = synopsis
df["Links"] = movie_links

df.to_csv("./data/scraping/allo_cine.csv", index=False)