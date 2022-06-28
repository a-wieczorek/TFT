import json
import pickle
from dataclasses import dataclass

@dataclass
class Data:
    name: str
    classes: list
    price: int


x = open("data_pickle.txt", "rb")
y = pickle.load(x)
x.close()
print(y)
