import pymongo
from pymongo import MongoClient
import dns

cluster = pymongo.MongoClient("mongodb+srv://SimFil:Sommar2021@cluster0.k6mlfru.mongodb.net/?retryWrites=true&w=majority")
db = cluster["invoiceReader"]
collection = db["invoiceReader"]

post = {"_id":0, "name": "simon", "score": 5}

collection.insert_one(post)