import certifi
ca=certifi.where()
from pymongo import MongoClient
client = MongoClient("mongodb+srv://codnjs:test@cluster0.0frgcjv.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)
db = client.wakhoo