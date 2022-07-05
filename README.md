# TFT
The app enables TeamFight Tactics' (TFT) players to get a list of champions with specific traits in Polish and English.
To achieve that it creates an API that returns data in **JSON** format using a combination of:
- Datascraping (w/ **Beautiful Soup**)
- Image altering (w/ **Pillow**)
- **FastApi** (Backend).

Then, the API is called using **JavaScript**, the fetched *JSON* is processed and the desired champions are shown as images in **HTML**. The traits that create a combination no champion has are faded out.

Finally, the app is wrapped in **Docker-Compose**.

![obraz](https://user-images.githubusercontent.com/102622810/177196769-ecc1694e-df40-4447-bf98-460c39331b91.png)


## Scrap.py
The code is responsible for scraping data from *https://app.mobalytics.gg/pl_pl/tft/champions* and saving it as a list of dicts in a *JSON* file.
```JSON
[{"name": "aatrox", 
  "traits": ["shimmerscale", "warrior"],
  "price": 1},
  ...
]
```
It also saves champion images in *Icons/* directory.


## imgEdit.py
The code is responsible for editing images downloaded in *Scrap.py* and saving them in *Icons/Edited* directory. It adds champion name in the bottom left of a picture.
![obraz](https://user-images.githubusercontent.com/102622810/177202845-69ac835b-8bec-42e5-9138-81c56a5a4e2d.png)


# API.py
The code utilises data prepared in *Scrap.py* and *imgEdt.py* in 2 endpoints.


### *localhost:8000/*
Returns *JSON* containing data about champions with traits specified in traits parameter (all champions if called without the parameter).

E.g. *localhost:8000/?traits=warrior,shimmerscale,*  ->
```JSON
{"champions": [
  { 
  "name": "aatrox",
  "traits": ["Shimmerscale", "Warrior"], 
  "price": 1, 
  "iconurl": "https://raw.githubusercontent.com/a-wieczorek/TFT/main/IconsEdited/aatrox.jpg"
  }, 
  {
  "name": "olaf", 
  "traits": ["Scalescorn", "Bruiser", "Warrior"], 
  "price": 3, 
  "iconurl": "https://raw.githubusercontent.com/a-wieczorek/TFT/main/IconsEdited/olaf.jpg"
  },
  ...
]}
```


### *localhost:8000/traitlists*
Returns *JSON* containing data about existing traits in English and in Polish language sorted alphabetically. Polish list is sorted by Polish names but also contains English ones - this allows keeping the *ID* (in *HTML*) of individual traits the same and keeping the traits chosen easily when the language is switched.
```JSON
{
"traitListEN": ["Assassin", "Astral", "Bard", ...], 
"traitListPL": [["Bard", "Bard"], ["Festynowy", "Revel"], ["Gwiezdny", "Astral"], ...]
}
```

## Index.html
Accessing the *HTML* file while running the project with *docker-compose* is possible under *localhost:3000/Index.html*.

