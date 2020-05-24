# rpg_queries.py
"""
Use sqlite3 to load and write queries to explore the data, and answer the following questions:

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
import os #using os rather than string becasue it might not work on other computers
import sqlite3

# construct a path to wherever your database exists
#DB_FILEPATH = "chinook.db"
DB_FILEPATH = os.path.join(os.path.dirname(__file__),"rpg_db.sqlite3") # relative filepath directory

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row # allow us to reference rows as dictionaries
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

# How many total Characters are there?
query1 = "SELECT COUNT(DISTINCT character_id) as total FROM charactercreator_character;"
result1 = cursor.execute(query1).fetchall()
print(f"QUESTION 1:There are {result1[0][0]} characters.\n")

# How many of each specific subclass?
cleric =" SELECT COUNT(DISTINCT character_ptr_id) as cleric FROM charactercreator_cleric;"
fighter = "SELECT COUNT(DISTINCT character_ptr_id) as fighter FROM charactercreator_fighter;"
mage = "SELECT COUNT(DISTINCT character_ptr_id) as mage FROM charactercreator_mage;"
necromancer = "SELECT COUNT(DISTINCT mage_ptr_id) as necromancer FROM charactercreator_necromancer;"
thief =" SELECT COUNT(DISTINCT character_ptr_id) as thief FROM charactercreator_thief;"

print(f"QUESTION 2:There are 5 sublclasses of characters")         
cleric_query = cursor.execute(cleric).fetchall()
print(f"There are {cleric_query[0][0]} clerics as a subclass of characters.")
fighter_query = cursor.execute(fighter).fetchall()
print(f"There are {fighter_query[0][0]} fighters as a subclass of characters.")
mage_query = cursor.execute(mage).fetchall()
print(f"There are {mage_query[0][0]} mages as a subclass of characters.")
necromancer_query = cursor.execute(necromancer).fetchall()
print(f"There are {necromancer_query[0][0]} necromancers as a subclass of characters, this is also a subclass of mage.")
thief_query = cursor.execute(thief).fetchall()
print(f"There are {thief_query[0][0]} thieves as a subclass of characters.\n")

# How many total Items?
query3= "SELECT COUNT(DISTINCT item_id) as items FROM armory_item;"
result3 = cursor.execute(query3).fetchall()
print(f"QUESTION 3: There are {result3[0][0]} items.\n")

# How many Items are weapons? How many are not?
# How many total Items?
query4= "SELECT COUNT(DISTINCT item_ptr_id) as weapons FROM armory_weapon;"
result4 = cursor.execute(query4).fetchall()
print(f"QUESTION 4: There are {result4[0][0]} weapons.")
print(f"Of the {result3[0][0]}, {(result3[0][0]-result4[0][0])} are not weapons.\n")


# How many Items does each character have? (Return first 20 rows)?
query5= "SELECT DISTINCT character_id, item_id FROM charactercreator_character_inventory GROUP BY item_id LIMIT 20;"
result5 = cursor.execute(query5).fetchall()
# print(f"There are {result5} items")
print("QUESTION 5:")
for row in result5:
    # print(row[0], row[1], row[2])
    print(row['item_id'], row['character_id'])

print('\n')

# How many Weapons does each character have? (Return first 20 rows)
query6= "SELECT COUNT(item_id), character_id FROM charactercreator_character_inventory WHERE item_id >=138 GROUP BY character_id LIMIT 20;"
result6 = cursor.execute(query6).fetchall()
print("QUESTION 5:")
# print(f"There are {result5} items")
for row in result6:
    # print(row[0], row[1], row[2])
    print(row['character_id'], row['COUNT(item_id)']) 
print('\n')

# On average, how many Items does each Character have?
query7 =  "SELECT AVG(Items) FROM (SELECT COUNT(DISTINCT item_id) as Items, character_id FROM charactercreator_character_inventory GROUP BY character_id)"
result7 =  cursor.execute(query7).fetchall()
print(f"QUESTION 7:On average, each Character has {(result7[0][0]):.0f} Items. \n")

# # On average, how many Weapons does each character have?
query8 =  "SELECT AVG(Items) FROM (SELECT COUNT(DISTINCT item_id) as Items, character_id FROM charactercreator_character_inventory WHERE item_id>=138 GROUP BY character_id)"
result8 =  cursor.execute(query8).fetchall()
print(f"QUESTION 8:On average, each Character has {(result8[0][0]):.0f} Weapons. \n")

