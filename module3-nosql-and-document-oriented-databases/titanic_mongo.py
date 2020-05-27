#rpg_mongo.py

"""
Put Titanic data in Big Data! That is, try to load `titanic.csv` from yesterday
into your MongoDB cluster.

"""

import pymongo 
import os
import pandas as pd 
import numpy as np 

from dotenv import load_dotenv

load_dotenv()

"""
STEPS:
   1. from pymongo import MongoClient.
   2. import pandas as pd.
   3. client = MongoClient()
   4. db=client.test.
   5. employee = db.employee.
   6. df = pd.read_csv("input.csv") #csv file which you want to import.
   7. records_ = df.to_dict(orient = 'records')
   8. result = db.employee.insert_many(records_ )
"""

#1. Connect to rpg_db.sqlite3
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module2-sql-for-analysis", "titanic.csv")
titanic = pd.read_csv(CSV_FILEPATH) # relative filepath directory
print(titanic.head())
print(titanic.shape)

#3. Establish MongoDB connection
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority")
db = client.titanic_database # "test_database" or whatever you want to call it
collection = db.passengers


#4. Insert Data into DB
collection.insert_many(titanic.to_dict("records")) #Insert into DB

#5. Confirm table was inserted
print(collection.find_one())