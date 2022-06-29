import json
import pickle
from dataclasses import dataclass
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from typing import List

@dataclass
class Champion:
    name: str
    traits: list
    price: int


app = FastAPI()
x = open("data_pickle.txt", "rb")
champions = pickle.load(x)
x.close()


def get_with_all_traits(traits: List[str]) -> List[str]:
    result: List[str] = []
    for c in champions:
        if all(x in c.traits for x in traits):
            result.append(c.name)
    return result


@app.get("/", response_class=HTMLResponse)
async def root(request: Request, traits=None):
    myDict = {}
    if traits is None:
        traits = []
    else:
        traits = traits.split(',')
    names = get_with_all_traits(traits)
    for i in names:
        for k in champions:
            miniDict = {}
            if i == k.name:
                miniDict['traits'] = k.traits
                miniDict['price'] = k.price
                miniDict['iconurl'] = f'https://raw.githubusercontent.com/a-wieczorek/TFT/main/IconsEdited/{i}.jpg'
                myDict[i] = miniDict

    return json.dumps(myDict)





uvicorn.run(app, host='localhost', port=8000)
