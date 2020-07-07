from src.CommonVariables import Generals
from DBManager.dbConnectionManager import DB


class RegDataManager:
    def __init__(self):
        self.db = DB()

    def saveData(self, formData):
        if self.db.connectUserRegisterDB(Generals.REG_DB):
            queryData = {"commonname": formData["commonname"]}
            booleanCheck = self.db.checkData(queryData)
            if booleanCheck:
                return Generals.DB_ERROR
            else:
                self.db.insertData(formData)
                return "User added"


if __name__ == '__main__':
    regDataManager = RegDataManager()
    regDataManager.saveData("save")