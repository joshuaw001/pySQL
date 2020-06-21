import sqlite3
class DataType:
    def __init__(self, name, value):
        self.name  = name
        self.value = value
        self.VARDB = {CONN:sqlite3.connect("variables.db")}
        self.VARDB.update({CURSOR:CONN.cursor()})
                          
        self.ID    = 0 #fix this later
