from guizero import App, TextBox
import pathlib
import math
from pathlib import Path
import os

class db:
	_password = "8888"
	_username = "Sql_undefinedUser"
	_server   = "localhost"
	_name     = "sample_db"
                
	def connect(username,password,name):
                if _password == password:
                	pass
	def disconnect(name):


class db_files:
	class dir:
		curr_dir = os.getcwd()
		
		def letter_to_number(letters):   
    			letters = letters.lower()
    			dictionary = {'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26}
    			strlen = len(letters)
    			number = dictionary[letters]
    			return number
		
	class dbf:
		def save(code,path):
			with open(path,"a") as file:
        		for i in code:
           		 _code = db_files.dir.letter_to_number(code)
            	file.write(_code)
		return True
	
		def load(path):
    			with open(path,"r") as file:
        			for i in file.read():
           				return i
	
	class tbl:
		def save(code,path):
    		with open(path,"a") as file:
        	for i in code:
        		_code = db_files.dir.letter_to_number(code)
        		file.write(_code)
        return True
	
		def load(path):
    			with open(path,"r") as file:
        			for i in file.read():
           				return i
	
	class intf:
		pass
"""
basic data storage structure
c:/-->
-pySQL
--db
---dbname#1
----name.dbf
----tblname#1
-----name.tbl
-----name.intf
"""

def buildDir():
    pass

with open("c:/pysql") as sysdir:
	if not sysdir.exists():
                pass

app = App()
Query = TextBox()
