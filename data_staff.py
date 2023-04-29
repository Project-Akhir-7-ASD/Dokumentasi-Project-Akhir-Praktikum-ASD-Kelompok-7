from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://kayla11virrly:yHe6dfatbJleGTfZ@cluster0.4a1rn0i.mongodb.net/test")
database = cluster["DBMHS7"]
collection = database["Data"]
