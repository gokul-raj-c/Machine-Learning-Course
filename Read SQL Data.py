#SQL Data Imports
import sqlite3 as sq3
import pandas as pd

#initialize path to SQLite database
path='data/'

#create connection SQL database
con=sq3.Connection(path)

#write query
query='''SELECT * FROM table_name'''

#Execute query
data=pd.read_sql(query,con)