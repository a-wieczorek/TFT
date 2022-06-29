import json
import pickle
from dataclasses import dataclass
import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse


@dataclass
class Data:
    name: str
    classes: list
    price: int


app = FastAPI()

x = open("data_pickle.txt", "rb")
data = pickle.load(x)
x.close()


@app.get("/", response_class=HTMLResponse)
async def root(request: Request, traits=None):
    myDict = {}
    if traits is None:
        traits = []
    else:
        traits = traits.split(',')
    for k in traits:
        for i in data:
            if k in i.classes:
                miniDict = {'classes': i.classes, 'price': i.price, 'imgurl': f'https://raw.githubusercontent.com/a-wieczorek/TFT/main/IconsEdited/{i.name}.jpg'}
                myDict[i.name] = miniDict

    return json.dumps(myDict)





uvicorn.run(app, host='localhost', port=8000)
