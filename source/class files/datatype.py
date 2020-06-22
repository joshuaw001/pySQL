import sqlite3
import 
class DataType:
    def __init__(self, name, value, is_active=True):
        self.name    = name
        self.value   = value
        self.vartype = None
        self.varstate = is_active
        self.VARDB   = {CONN:sqlite3.connect("variables.db")}
        self.VARDB.update({CURSOR:CONN.cursor()})
                          
        self.ID    = 0 #fix this later
    def __str__(self):
        return f"{self.name}, no type, set to {self.value}."
    def __del__(self):
        return f"deleted variable @ {self.ID}."
