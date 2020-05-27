#titanic_mongo.py

"""
Reproduce (debugging as needed) the live lecture task of setting up and 
inserting the RPG data into a MongoDB instance, and add the code you write 
to do so here. Then answer the following question (can be a comment in 
the top of your code or in Markdown) 
- "How was working with MongoDB different from working with PostgreSQL? 
What was easier, and what was harder?
"""

import pymongo 
import os
import sqlite3
import psycopg2
import pandas as pd 
import numpy as np 
from itertools import chain
from dotenv import load_dotenv

load_dotenv()

#1. Connect to rpg_db.sqlite3
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module1-introduction-to-sql", "rpg",  "rpg_db.sqlite3") # relative filepath directory
connection = sqlite3.connect(DB_FILEPATH)

#2. Pull info from charactercreator_character table into a pandas dataframe
rpg_df  = pd.read_sql_query("SELECT * FROM charactercreator_character", connection)
print(rpg_df.head())
print(rpg_df.shape)

connection.close()

#3. Establish MongoDB connection
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority")
db = client.rpg_database # "test_database" or whatever you want to call it
collection = db.charactercreator_character

collection.delete_many({})

#4. Insert Data into DB
collection.insert_many(rpg_df.to_dict("records")) #Insert into DB

#5. Confirm table was inserted
print(collection.find_one())



#references
#https://datacarpentry.org/python-ecology-lesson/09-working-with-sql/index.html
#https://sricharanphp.blogspot.com/2020/01/insert-pandas-dataframe-into-mongodb.html