from pymongo import MongoClient
from src.CommonVariables import Generals
import json

class DB:
    connector = 'mongodb://localhost:27017'

    def __init__(self):
        self.client = MongoClient(DB.connector)

    def connectUserRegisterDB(self, dbName):
        if dbName in self.client.list_database_names():
            # print("db {} exist".format(dbName))
            return True
        else:
            # print("db {} not available".format(dbName))
            return False

    def insertData(self, formData):
        myDb = self.client[Generals.REG_DB]
        if Generals.REG_COLLECTION in myDb.collection_names():
            myCollection = myDb[Generals.REG_COLLECTION]
            queryResult = myCollection.insert_one(formData)
            print('Insert result:', queryResult)

    def updateData(self, formData):
        pass

    def checkData(self, regToken):
        myDb = self.client[Generals.REG_DB]
        if Generals.REG_COLLECTION in myDb.collection_names():
            myCollection = myDb[Generals.REG_COLLECTION]
            myQuery = {"regToken": regToken}
            queryResult = myCollection.find(myQuery)
            for i in queryResult:
                print(i['commonname'])
                if i:
                    print("True")
                else:
                    print("false")
                return True
        else:
            print("couldn't connect to collectionsq")


if __name__ == '__main__':
    db = DB("PmaMapper")
    print(db.connectUserRegisterDB())
