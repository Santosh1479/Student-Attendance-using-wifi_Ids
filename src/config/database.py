from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def connect_to_mongo(uri, db_name):
    try:
        client = MongoClient(uri)
        db = client[db_name]
        print("MongoDB connection successful")
        return db
    except ConnectionFailure as e:
        print(f"Could not connect to MongoDB: {e}")
        return None