""" 

from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.fundsexplorer.com.br/ranking")
res = BeautifulSoup(html.read()."html5lib");
print(res.title)

https://imasters.com.br/back-end/como-fazer-web-scraping-com-python
"""
from requests import get
url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'
response = get(url)
print(response.text[:500])