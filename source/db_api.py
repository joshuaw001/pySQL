#import required libraries:

import math

try:
	import sqlite3
	
except ImportError:
	import pymysql

#connect databases:

class db:
	def __init__(self):
		self.password = “8888”
		self.username = “Sql_undefinedUser”
		self.server   = “localhost”
		self.name     = “sample_db”
                
	def connect(username,password,name):
                if self.password == username:
                        
