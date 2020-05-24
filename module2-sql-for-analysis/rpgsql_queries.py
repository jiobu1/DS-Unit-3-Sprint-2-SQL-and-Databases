#rpgsql_queries.py

#Assignment 2A
"""
Set up and inserting the RPG data into a PostgreSQL database
"""


#Imports
import os
import sqlite3
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import DictCursor
from psycopg2.extras import execute_values
import json
import pandas as pd

# print('CWD', os.getcwd())
# print('file', __file__)

load_dotenv() #> loads contents of the .env file into the script's environment

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module1-introduction-to-sql", "rpg",  "rpg_db.sqlite3") # relative filepath directory
connection = sqlite3.connect(DB_FILEPATH)
print('CONNECTION', connection)

connection.row_factory = sqlite3.Row # allow us to reference rows as dictionaries
cursor = connection.cursor()
print('CURSOR', cursor)

#1. Pull info from charactercreator_character table
query  = 'SELECT * FROM charactercreator_character;'
results = cursor.execute(query).fetchall()
# for row in result:
#     # print(row[0], row[1], row[2])
#     print(row['character_id'], row['name'], row['level'], row['exp'], row['hp'], row['strength'], row['intelligence'], row['dexterity'], row['wisdom']) 

#Credentials to connect to Postgres SQL
RPG_NAME = os.getenv("RPG_NAME", default='OOPS')
RPG_USER = os.getenv("RPG_USER", default='OOPS')
RPG_PASSWORD = os.getenv("RPG_PASSWORD", default='OOPS')
RPG_HOST = os.getenv("RPG_HOST", default='OOPS')

pg_connection = psycopg2.connect(dbname=RPG_NAME, user=RPG_USER, password=RPG_PASSWORD, host=RPG_HOST)
print("CONNECTION:", pg_connection)

pg_cursor = pg_connection.cursor()
print("CURSOR:", pg_cursor)


# Create charactercreator_character table and insert into PostgresSQL

#2. Create table
table_name = "charactercreator_character"

query1 = f"""CREATE TABLE IF NOT EXISTS {table_name}(
        character_id SERIAL PRIMARY KEY, 
        name VARCHAR(30), 
        level INT, 
        exp INT, 
        hp INT,
        strength INT, 
        intelligence INT, 
        dexterity INT, 
        wisdom INT);"""
print('SQL', query1)
pg_cursor.execute(query1)

#3. Add data to table
execute_values(pg_cursor, """INSERT INTO charactercreator_character (character_id, name, level, exp, hp, strength, intelligence, dexterity, wisdom) VALUES %s;""", [tuple(row) for row in results]) 

pg_connection.commit()