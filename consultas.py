from pymongo import MongoClient
MONGO_URL = 'mongodb://localhost'
location = MongoClient(MONGO_URL)
database = location['COVID']
collection = database['CASOS']
