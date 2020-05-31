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
import os
from dotenv import load_dotenv

load_dotenv()

#Establish MongoDB connection
DB_USER = os.getenv("MONGO_USER", default="OOPS")
DB_PASSWORD = os.getenv("MONGO_PASSWORD", default="OOPS")
CLUSTER_NAME = os.getenv("MONGO_CLUSTER_NAME", default="OOPS")

client = pymongo.MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@{CLUSTER_NAME}.mongodb.net/test?retryWrites=true&w=majority")

db = client.rpg_json # "test_database" or whatever you want to call it
collection = db.rpg_db

#1. How many characters are there?
character_count = collection.count_documents({'model': 'charactercreator.character'})
print(f"QUESTION 1: There are {character_count} characters.\n")

#2. How many of each specific subclass?
print("QUESTION 2:")
for subclass in ['cleric', 'fighter', 'mage', 'necromancer', 'thief']:
    character_subclass_count = collection.count_documents({'model': 'charactercreator.'+subclass})
    print(f"There are {character_subclass_count} {subclass}s as a subclass of characters.")
print('\n')

#3. How many total items?
item_count = collection.count_documents({'model':'armory.item'})
print(f"QUESTION 3: There are {item_count} items.\n")

#4. How many Items are weapons? How many are not? 
weapon_count = collection.count_documents({'model':'armory.weapon'})
print("QUESTION 4:") 
print(f"There are {weapon_count} weapons.")
print(f"{item_count - weapon_count} are not weapons.\n")

#5. How many items does each character have?(Return first 20 rows)
characters = collection.find({'model': 'charactercreator.character'})
print("QUESTION 5:")
for character in characters[:20]:
    print(character['fields']['name'], len(character['fields']['inventory']))
print('\n')

#6. How many Weapons does each character have? (Return first 20 rows)
characters = collection.find({'model': 'charactercreator.character'})
weapons = collection.find({'model':'armory.weapon'})
weapon_pk = [weapon['pk'] for weapon in weapons ]
for character in characters[:20]:
    inventory = character['fields']['inventory']
    num_weapons = len([item for item in inventory if item in weapon_pk ])
    print(character['fields']['name'], num_weapons)
print('\n')



#7. On average, how many Items does each Character have?
average_items = item_count/character_count
print(f"QUESTION 7: Each character has about {average_items:.2f} items.\n" )

#8. On average, how many weapons does each character have?
average_weapons = weapon_count/character_count
print(f"QUESTION 8: Each character has about {average_weapons:.2f} weapons.\n" )