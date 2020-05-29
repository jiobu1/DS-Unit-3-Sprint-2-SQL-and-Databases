#insert_titanic_py

#Assignment 2B
"""
set up a new table for the Titanic data (`titanic.csv`)
"""

# #Imports
# import os
# import pandas, csv
# from io import StringIO
# from sqlalchemy import create_engine
# from dotenv import load_dotenv

# load_dotenv() #> loads contents of the .env file into the script's environment

# #https://stackoverflow.com/questions/2987433/how-to-import-csv-file-data-into-a-postgresql-table

# CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv")
# titanic = pandas.read_csv(CSV_FILEPATH)
# titanic.columns = [c.lower() for c in titanic.columns] #postgres doesn't like capitals or spaces

# URL = os.getenv('URL', default = "OOPS")
# engine = create_engine(URL)


# titanic.to_sql('titanic', engine)

#Imports
import os
import sqlite3
from dotenv import load_dotenv
import psycopg2
from psycopg2.extras import DictCursor
from psycopg2.extras import execute_values
import pandas as pd

load_dotenv() #> loads contents of the .env file into the script's environment

#Retrieve CSV 
CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "..", "module2-sql-for-analysis", "titanic.csv")

#Credentials to connect to Postgres SQL
URL = os.getenv('URL', default = "OOPS")

connection = psycopg2.connect(URL)
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR:", cursor)

# Create charactercreator_character table and insert into PostgresSQL
postgres_table = """
DROP TABLE IF EXISTS titanic;
CREATE TABLE IF NOT EXISTS titanic (
    id SERIAL PRIMARY KEY,
    survived boolean,
    pclass int4,
    full_name text,
    gender text,
    age int4,
    sib_spouse_count int4,
    parent_child_count int4,
    fare float8
);
"""
print('Postgres', postgres_table)
cursor.execute(postgres_table)

df = pd.read_csv(CSV_FILEPATH)
print(df.columns.tolist())

df["Survived"] = df["Survived"].values.astype(bool) # do this before converting to native types, because this actually converts to np.bool
df = df.astype("object") # converts numpy dtypes to native python dtypes (avoids psycopg2.ProgrammingError: can't adapt type 'numpy.int64')

# Insert data into titanic table
# how to convert dataframe to a list of tuples?
list_of_tuples = list(df.to_records(index=False))

insertion_query = f"INSERT INTO titanic (survived, pclass, full_name, gender, age, sib_spouse_count, parent_child_count, fare) VALUES %s"
execute_values(cursor, insertion_query, list_of_tuples) # third param: data as a list of tuples!

# CLEAN UP

connection.commit() # actually save the records / run the transaction to insert rows

cursor.close()
connection.close()