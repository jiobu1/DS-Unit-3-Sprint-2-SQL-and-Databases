#rpg_mongo_queries.py
"""
use [MongoDB queries](https://docs.mongodb.com/manual/tutorial/query-documents/) to answer
the same questions as you did from the first module (when the RPG data was in
SQLite).

    How many total Characters are there?
    How many of each specific subclass?
    How many total Items?
    How many of the Items are weapons? How many are not?
    How many Items does each character have? (Return first 20 rows)
    How many Weapons does each character have? (Return first 20 rows)
    On average, how many Items does each Character have?
    On average, how many Weapons does each character have?

To complete the assignment you should write a file rpg_queries.py that imports sqlite3 and 
programmatically executes and reports results for the above queries.
"""

#Imports
import pymongo
from dotenv import load_dotenv

load_dotenv()

#Establish MongoDB connection
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority")

