import json
import pickle
from dataclasses import dataclass


@dataclass
class Data:
    name: str
    classes: list
    price: int


x = open("data_pickle.txt", "rb")
data = pickle.load(x)
x.close()

Dict = {}
for i in data:
    miniDict = {'classes': i.classes, 'price': i.price, 'imgpath': f'IconsEdited/{i.name}.jpg'}
    Dict[i.name] = miniDict
with open("DataJson", "w") as fp:
    json.dump(Dict, fp)

