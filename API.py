import json
from dataclasses import dataclass

import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from pydantic import parse_obj_as


@dataclass
class Champion:
    name: str
    traits: list
    price: int


app = FastAPI()

with open('data.json', 'r') as f:
    champions_json = json.load(f)
champions = parse_obj_as(List[Champion], champions_json)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

translator = {
    "Shimmerscale": "Migocząca Łuska",
    "Warrior": "Wojownik",
    "Jade": "Nefrytowy",
    "Evoker": "Przywołujący",
    "Legend": "Legenda",
    "Tempest": "Nawałnica",
    "Dragon": "Smok",
    "Swiftshot": "Szybkostrzelny",
    "Astral" : "Gwiezdny",
    "Dragonmancer": "Wysłannik Smoków",
    "Mage": "Mag",
    "Mirage": "Miraż",
    "Revel": "Festynowy",
    "Bruiser": "Osiłek",
    "Guild": "Z Gildii",
    "Mystic": "Mistyk",
    "Bard": "Bard",
    "Scalescorn": "Łuskobójcy",
    "Guardian": "Strażnik",
    "Cannoneer": "Kanonier",
    "Assassin": "Zabójca",
    "Whispers": "Szepty",
    "Shapeshifter": "Zmiennokształtny",
    "Ragewing": "Skrzydło Gniewu",
    "Cavalier": "Kawalerzysta",
    "Trainer": "Trener",
    "Starcaller": "Zaklinacz Gwiazd",
    "Spellthief": "Złodziej Czarów",
}


def get_with_all_traits(traits: List[str]) -> List[str]:
    result: List[str] = []
    for c in champions:
        if all(x.lower() in c.traits for x in traits):
            result.append(c.name)
    return result


@app.get("/", response_class=HTMLResponse)
async def root(request: Request, traits=None):
    allTraits = []
    myDict = {}
    miniDicts = []
    if traits is None:
        traits = []
    else:
        traits = traits[:-1].split(',')
    names = get_with_all_traits(traits)
    for i in names:
        for k in champions:
            allTraits = allTraits + [trait.capitalize() for trait in k.traits]
            miniDict = {}
            if i == k.name:
                capTraits = [x.capitalize() for x in k.traits]
                miniDict['name'] = k.name
                miniDict['traits'] = capTraits
                miniDict['price'] = k.price
                miniDict['iconurl'] = f'https://raw.githubusercontent.com/a-wieczorek/TFT/main/IconsEdited/{i}.jpg'
                miniDicts.append(miniDict)
    myDict['champions'] = miniDicts
    myDict['traitListEN'] = sorted(set(allTraits))
    myDict['traitListPL'] = sorted([[translator[trait], trait] for trait in allTraits])
    return json.dumps(myDict)


@app.get("/traitlists", response_class=HTMLResponse)
async def returnLists(request: Request):
    allTraits = []
    result = {}
    for k in champions:
        allTraits = allTraits + [trait.capitalize() for trait in k.traits]
    allTraits = set(allTraits)
    result['traitListEN'] = sorted(allTraits)
    result['traitListPL'] = sorted([[translator[trait], trait] for trait in allTraits])
    return json.dumps(result)

if __name__ == '__main__':
    uvicorn.run(app, host='localhost', port=8000)
