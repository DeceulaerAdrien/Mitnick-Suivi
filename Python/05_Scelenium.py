# import os
# import re
# import selenium
# import collections
# import bs4
import requests
# import json
# import lxml.html
# import time
# import random
# import logging
# import numpy as np
import pandas as pd

# from bs4 import BeautifulSoup
# from selenium import webdriver
# from random import randint
# from time import gmtime, strftime
# from tabulate import tabulate
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By

# key = "73bbb95f8ecb49b499113a46481b4af1"
# url = "https://newsapi.org/v2/top-headlines?sources=lequipe&apiKey=" + key
# response = requests.get(url)

# # Here the response format is a json file, it is used as a dictionary
# print(response.json())
# dictionnary = response.json()
# print(dictionnary.keys())
# for element in list(dictionnary.keys()):
#     print("##############################################")
#     print("Key: ", element, "// Values: ", dictionnary[element])
# # And now we have lists in dictionaries(it's a JSON file actually but it's very similar)
# # We will discover the information of the article key.
#
# for element in enumerate(dictionnary["articles"]):
#     print("###############################################")
#     print(element)
# # So if we keep going, it gives us another dictionary!
# for element in dictionnary["articles"][0].keys():
#     print(" Key : ", element, "Values : ", dictionnary["articles"][0][element])


key = "73bbb95f8ecb49b499113a46481b4af1"
url = "https://newsapi.org/v2/top-headlines?sources=lequipe&apiKey=" + key

response = requests.get(url)

data = response.json()

if data["status"] == "ok":
    # Extract the articles
    articles = data["articles"][:10]  # Get the last ten articles

    titles = []
    authors = []
    descriptions = []
    urls = []

    for article in articles:
        titles.append(article.get("title", ""))
        authors.append(article.get("author", ""))
        descriptions.append(article.get("description", ""))
        urls.append(article.get("url", ""))

    df = pd.DataFrame({
        "Title": titles,
        "Author": authors,
        "Description": descriptions,
        "URL": urls
    })

    df.to_csv("./data/scraping/news_articles.csv", index=False)

    print("Data saved successfully to news_articles.csv.")
else:
    print("Failed to retrieve news articles. Status:", data["status"])