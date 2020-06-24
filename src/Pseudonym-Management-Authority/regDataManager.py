from src.CommonVariables import Generals
from DBManager.dbConnectionManager import DB


class RegDataManager:
    def __init__(self):
        self.db = DB()

    def saveData(self, formData):
        if self.db.connectUserRegisterDB(Generals.REG_DB):
            print(formData)
