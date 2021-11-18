import json
from pymongo import MongoClient

client = MongoClient("localhost", 27017)

db = client.pymongo_json

collection = db.users

with open("data.json") as json_file:
    file_data = json.load(json_file)

collection.insert_many(file_data)
