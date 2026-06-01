import pandas as pd

#SQL data imports
from pymongo import MongoClient

#create mongo connection
con=MongoClient()
con = MongoClient("mongodb://localhost:27017/")

# Atlas connection string
con = MongoClient("mongodb+srv://username:password@cluster0.xxxxx.mongodb.net/")

#choose database ( use con.list_databse_names() )
db=con.databse_name

#create a cursor object using a query
cursor = db.employees.find({"department": "IT"})

#expand cursor and constructor
df=pd.DataFrame(list(cursor))
print(df)