import sqlite3
import errortypes
class DataType:
    def __init__(self, name, value, is_active=True):
        self.name    = name
        self.value   = value
        self.valuecache = []
        self.vartype = None
        self.varstate = is_active
        self.VARDB   = {CONN:sqlite3.connect("variables.db")}
        self.VARDB.update({CURSOR:CONN.cursor()})
                          
        self.ID    = 0 #fix this later
    def __str__(self):
        return f"{self.name}, no type, set to {self.value}."
    def __del__(self):
        return f"deleted variable @ {self.ID}. "
    def redefine(self, newvalue):
        if self.varstate is True:
            self.valuecache += self.value
            self.value = newvalue
        else:
            return errortypes.VariableNotActiveError()
