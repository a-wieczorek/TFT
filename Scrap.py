import urllib
from dataclasses import dataclass
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pickle


@dataclass
class Data:
    name: str
    classes: list
    price: int


data = []
champs = []
iconsUrl = []

url = 'https://app.mobalytics.gg/pl_pl/tft/champions'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, "html.parser")
for a in soup.find_all('a', href=True):
    if a['href'].startswith('/pl_pl/tft/champions/'):
        classes = []
        price = int(a.select('div.m-s5xdrg')[0].contents[1])
        name = a['href'][len('/pl_pl/tft/champions/'):]
        for i in a.select('div.m-8s0dym'):
            classes.append(str(i.nextSibling))
        data.append(Data(
            name=str(name),
            classes=classes,
            price=int(price),
        ))
        x = a.select('div.m-1lk7whh')[0]['style']
        link = x[x.find('(') + 1:x.find(')')]
        urllib.request.urlretrieve(link, "Icons/" + link.split("/")[-1])

data_pickled = open('data_pickle.txt', 'wb')
pickle.dump(data, data_pickled)
data_pickled.close()

