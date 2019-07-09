#import required libraries:

import math

try:
	import sqlite3
	
except ImportError:
	import pymysql

#connect databases:

class db:
	def __init__(self):
		self.password = None
		self.username = None
		self.server   = 'localhost'
		self.name     = 'sample_db		
'
	def connect(username,password,name):
		
