import pymongo

class Database(object):
    URI = "127.0.0.1:27017"
    DB = None

    @staticmethod
    def initialize():
        conn = pymongo.MongoClient(Database.URI)
        Database.DB = conn['blog']

    @staticmethod
    def find(collection, query):
        return Database.DB[collection].find(query)

    @staticmethod
    def insert(collection, data):
        Database.DB[collection].insert(data)