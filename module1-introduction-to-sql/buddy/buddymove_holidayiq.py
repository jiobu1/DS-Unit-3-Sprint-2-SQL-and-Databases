
"""
Load the data (use pandas) from the provided file buddymove_holidayiq.csv (the BuddyMove Data Set) - you should have 249 rows, 7 columns, and no missing values. The data reflects the number of place reviews by given users across a variety of categories (sports, parks, malls, etc.).

Using the standard sqlite3 module:

    Open a connection to a new (blank) database file buddymove_holidayiq.sqlite3
    Use df.to_sql (documentation) to insert the data into a new table review in the SQLite3 database

Then write the following queries (also with sqlite3) to test:

    Count how many rows you have - it should be 249!
    How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?
    (Stretch) What are the average number of reviews for each category?

Your code (to reproduce all above steps) should be saved in buddymove_holidayiq.py, and added to the repository along with the generated SQLite database.

"""
#Imports
import os #using os rather than string becasue it might not work on other computers
import sqlite3
import pandas as pd
import numpy as np

#Checking csv to make sure it is imported correctly
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.csv")
buddymove_holidayiq = pd.read_csv(CSV_FILEPATH)
print(buddymove_holidayiq.head())
print(buddymove_holidayiq.shape)

#code used to create new sqlite db
# connection = sqlite3.connect('buddymove_holidayiq.sqlite3')
# cursor.execute('CREATE TABLE buddymove_holidayiq (User ID, Sports, Religious, Nature, Theater, Shopping, Picnic)')
# connection.commit()

# buddymove_holidayiq.to_sql('buddymove_holidayiq', connection, if_exists = 'replace', index = True )


# # construct a path to wherever your database exists
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3") # relative filepath directory

connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row # allow us to reference rows as dictionaries
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

#Count how many rows you have - it should be 249!
query1 = "SELECT COUNT(*) FROM buddymove_holidayiq"
result1 = cursor.execute(query1).fetchall()
print(f"QUESTION1: There are {result1[0][0]} rows. \n")

#How many users who reviewed at least 100 Nature in the category also reviewed at least 100 in the Shopping category?
query2 = "SELECT COUNT(Nature>=100), COUNT(Shopping>=100) FROM buddymove_holidayiq WHERE Nature = Shopping"
alt_query = """
SELECT COUNT (*)
FROM buddymove_holidayiq
WHERE NATURE >=100 AND Shopping >=100 
"""
result_alt = cursor.execute(alt_query).fetchall()
result2 = cursor.execute(query2).fetchall()
print(f"QUESTION 2:There are {result2[0][0]} where the review for Nature and Shopping are both at least 100.\n")
print(f"QUESTION 2:There are {result_alt[0][0]} where the review for Nature and Shopping are both at least 100.\n")



 #(Stretch) What are the average number of reviews for each category?
sports = "SELECT AVG(Sports) FROM buddymove_holidayiq"
religious = "SELECT AVG(Religious) FROM buddymove_holidayiq"
nature = "SELECT AVG(Nature) FROM buddymove_holidayiq"
theatre = "SELECT AVG(Theatre) FROM buddymove_holidayiq"
shopping = "SELECT AVG(Shopping) FROM buddymove_holidayiq"
picnic = "SELECT AVG(Picnic) FROM buddymove_holidayiq"

print('STRETCH')
sports_query = cursor.execute(sports).fetchall()
print(f"There average sports review is {(sports_query[0][0]):.0f}")
religious_query = cursor.execute(religious).fetchall()
print(f"There average sports review is {(religious_query[0][0]):.0f}")
nature_query = cursor.execute(nature).fetchall()
print(f"There average sports review is {(nature_query[0][0]):.0f}")
theatre_query = cursor.execute(theatre).fetchall()
print(f"There average sports review is {(theatre_query[0][0]):.0f}")
shopping_query = cursor.execute(shopping).fetchall()
print(f"There average sports review is {(shopping_query[0][0]):.0f}")
picnic_query = cursor.execute(picnic).fetchall()
print(f"There average sports review is {(picnic_query[0][0]):.0f}")


