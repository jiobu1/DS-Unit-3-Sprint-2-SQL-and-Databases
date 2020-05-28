#insert_titanic_py

#Assignment 2B
"""
set up a new table for the Titanic data (`titanic.csv`)
"""

#Imports
import os
import pandas, csv
from io import StringIO
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

#https://stackoverflow.com/questions/2987433/how-to-import-csv-file-data-into-a-postgresql-table

CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv")
titanic = pandas.read_csv(CSV_FILEPATH)
titanic.columns = [c.lower() for c in titanic.columns] #postgres doesn't like capitals or spaces

URL = os.getenv('URL', default = "OOPS")
engine = create_engine(URL)


titanic.to_sql('titanic', engine)