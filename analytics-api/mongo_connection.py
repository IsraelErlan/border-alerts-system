from pymongo import MongoClient 
import os

class Mongo:
    client = None
    collection = None 
    host = os.getenv('MONGO_HOST', 'localhost')
    port = int(os.getenv('MONGO_PORT', 27017))

    @classmethod
    def get_client(cls):
        if cls.client is None:
            cls.client = MongoClient(host=cls.host, port=cls.port)
        return cls.client
    
    @classmethod
    def get_collection(cls, db_name="week-18-test", collection_name="week-18-collection"):
        if cls.collection is None:
            client = cls.get_client()
            db = client[db_name]
            cls.collection = db[collection_name]
        return cls.collection

