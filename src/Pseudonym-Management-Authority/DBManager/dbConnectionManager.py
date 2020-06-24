from pymongo import MongoClient


class DB:
    connector = 'mongodb://localhost:27017'

    def __init__(self):
        self.client = MongoClient(DB.connector)

    def connectUserRegisterDB(self, dbName):
        print(self.client.list_database_names())
        if dbName in self.client.list_database_names():
            print("db {} exist".format(dbName))
            return True
        else:
            print("db {} not available".format(dbName))
            return False


if __name__ == '__main__':
    db = DB("PmaMapper")
    print(db.connectUserRegisterDB())
