# TFT
The app enables TeamFight Tactics' (TFT) players to get a list of champions with specific traits in Polish and English.
To achieve that it creates an API that returns data in **JSON** format using a combination of:
- Datascraping (w/ **Beautiful Soup**)
- Image altering (w/ **Pillow**)
- **FastApi** (Backend).

Then, the API is called using **JavaScript**, the fetched *JSON* is processed and the desired champions are shown as images. The traits that create a combination no champion has are faded out.

Finally, the app is wrapped in **Docker-Compose**

![obraz](https://user-images.githubusercontent.com/102622810/177196769-ecc1694e-df40-4447-bf98-460c39331b91.png)

#Scrap.py
The code is responsible for scraping data from *https://app.mobalytics.gg/pl_pl/tft/champions* and saving it as a list of dicts in a *JSON* file
```JSON
[{"name": "aatrox", 
  "traits": ["shimmerscale", "warrior"],
  "price": 1},
  ...
]
```
It also saves champion images in *Icons/* directory

#imgEdit.py
The code is responsible for editing images downloaded in *Scrap.py*. It adds champion name in the bottom left of a picture.

