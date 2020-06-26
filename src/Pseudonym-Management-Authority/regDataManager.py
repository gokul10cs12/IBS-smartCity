from src.CommonVariables import Generals
from DBManager.dbConnectionManager import DB


class RegDataManager:
    def __init__(self):
        self.db = DB()

    def saveData(self, formData):
        if self.db.connectUserRegisterDB(Generals.REG_DB):
            self.db.checkData(formData["regToken"])
            self.db.insertData(formData)


if __name__ == '__main__':
    regDataManager = RegDataManager()
    regDataManager.saveData("save")