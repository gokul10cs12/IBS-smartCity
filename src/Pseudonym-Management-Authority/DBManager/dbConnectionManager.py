import pymongo
from pymongo import MongoClient


class DB(object):
    connector = 'mongodb://localhost:27017'

    def __init__(self, dbName):
        self.client = MongoClient(DB.connector)
        self.dbName = dbName

    def connectUserRegister(self):
        print(self.client.list_database_names())
        if self.dbName in self.client.list_database_names():
            print("db {} exist".format(self.dbName))
        else:
            print("db {} not available".format(self.dbName))



if __name__ == '__main__':
    db = DB("PmaMapper")
    db.connectUserRegister()
