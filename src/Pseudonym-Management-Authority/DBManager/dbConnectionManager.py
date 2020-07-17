from pymongo import MongoClient
from src.CommonVariables import Generals


class DB:
    connector = 'mongodb://localhost:27017'

    def __init__(self):
        self.client = MongoClient(DB.connector)

    def connectUserRegisterDB(self, dbName):
        if dbName in self.client.list_database_names():
            return True
        else:
            return False

    def insertData(self, formData):
        myDb = self.client[Generals.REG_DB]
        if Generals.REG_COLLECTION in myDb.collection_names():
            myCollection = myDb[Generals.REG_COLLECTION]
            queryResult = myCollection.insert_one(formData)
            print('Insert result:', queryResult)

    def updateData(self, formData):
        pass

    def checkData(self, query):
        myDb = self.client[Generals.REG_DB]
        if Generals.REG_COLLECTION in myDb.collection_names():
            myCollection = myDb[Generals.REG_COLLECTION]
            queryResult = myCollection.find(query).limit(1).count()
            print("queryResult:", queryResult)

            if queryResult == 0:
                return False
            else:
                return True

        else:
            print("couldn't connect to collections")


if __name__ == '__main__':
    db = DB("PmaMapper")
    print(db.connectUserRegisterDB())
