import sqlite3
from sqlite3 import Error
from continue_dev_configs.Utils import Utils

class Database:
    def create(self):
        try:
            conn = sqlite3.connect("database_" + Utils.create() + ".db")
        except Error as e:
            print(e)
            
        
        