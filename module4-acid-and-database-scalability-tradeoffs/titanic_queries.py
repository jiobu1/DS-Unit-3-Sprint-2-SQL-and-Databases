#titanic_queries.py
"""
Practice! Go back to both your deployed PostgreSQL (Titanic data) and MongoDB
(RPG data) instances - use [MongoDB
queries](https://docs.mongodb.com/manual/tutorial/query-documents/) to answer
the same questions as you did from the first module (when the RPG data was in
SQLite). With PostgreSQL, answer the following:

- How many passengers survived, and how many died?
- How many passengers were in each class?
- How many passengers survived/died within each class?
- What was the average age of survivors vs nonsurvivors?
- What was the average age of each passenger class?
- What was the average fare by passenger class? By survival?
- How many siblings/spouses aboard on average, by passenger class? By survival?
- How many parents/children aboard on average, by passenger class? By survival?
- Do any passengers have the same name?
- (Bonus! Hard, may require pulling and processing with Python) How many married
  couples were aboard the Titanic? Assume that two people (one `Mr.` and one
  `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
  a married couple. 
"""

import os
import psycopg2
from psycopg2.extras import DictCursor
from psycopg2.extras import execute_values
from dotenv import load_dotenv

load_dotenv() #> loads contents of the .env file into the script's environment

URL = os.getenv('URL', default = "OOPS")

pg_connection = psycopg2.connect(URL)
print("CONNECTION:", pg_connection)

pg_cursor = pg_connection.cursor()
print("CURSOR:", pg_cursor)

query1 = """SELECT COUNT(survived) FROM passengers WHERE survived = TRUE;"""
result1 = pg_cursor.execute(query1)
result1.fetchall()

