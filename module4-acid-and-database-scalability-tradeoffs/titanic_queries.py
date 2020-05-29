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

def cursor_connection_close(connection, cursor):
    cursor.close()
    # connection.commit()
    connection.close()

#- How many passengers survived, and how many died?
sql_com1 = """
            SELECT survived, COUNT(*) 
            FROM titanic 
            GROUP BY survived
            ORDER BY survived DESC;"""
pg_cursor.execute(sql_com1)
rows1 = pg_cursor.fetchall()
rows_result1 = [r[1] for r in rows1]
labels1 = ['survived', 'died']
for label, row in zip(labels1, rows_result1):
    print(f'Passengers who {label}: {row}')


#- How many passengers were in each class?
sql_com2 = """
            SELECT pclass, COUNT(*) 
            FROM titanic 
            GROUP BY pclass
            ORDER BY pclass ASC;"""
pg_cursor.execute(sql_com2)
rows2 = pg_cursor.fetchall()
rows_result2 = [r[1] for r in rows2]
labels2 = ['1st class', '2nd class', '3rd class']
for label, row in zip(labels2, rows_result2):
    print(f'Passengers in {label}: {row}')

#- How many passengers survived/died within each class?
sql_com3 = """
            SELECT survived, pclass, COUNT(*)
            FROM titanic
            GROUP by pclass, survived
            ORDER by survived DESC, pclass ASC;"""
pg_cursor.execute(sql_com3)
rows3 = pg_cursor.fetchall()
rows_result3 = [r[2] for r in rows3]
labels3 = ['1st class who lived', '2nd class who lived',
           '3rd class who lived', '1st class who died', '2nd class who died',
           '3rd class who died']
for label, row in zip(labels3, rows_result3):
    print(f'Passengers in {label}: {row}')


#- What was the average age of survivors vs nonsurvivors?
sql_com4 = """
            SELECT AVG(age), survived
            FROM titanic
            GROUP BY survived
            ORDER BY survived DESC;"""
pg_cursor.execute(sql_com4)
rows4 = pg_cursor.fetchall()
rows_result4 = [r[0] for r in rows4]
labels4 = ['survivors', 'nonsurvivors']
for label, row in zip(labels4, rows_result4):
    print(f'Average of {label}: {row:.2f}')

#- What was the average age of each passenger class?
sql_com5 = """
            SELECT AVG(age), pclass
            FROM titanic
            GROUP BY pclass;"""
pg_cursor.execute(sql_com5)
rows5 = pg_cursor.fetchall()
rows_result5 = [r[0] for r in rows5]
labels5 = ['1st class', '2nd class', '3rd class']
for label, row in zip(labels5, rows_result5):
    print(f'Average age of {label} passenger: {row:.2f}')

#- What was the average fare by passenger class? By survival?
sql_com6a = """
           SELECT AVG(fare), pclass
           FROM titanic
           GROUP BY pclass;"""
pg_cursor.execute(sql_com6a)
rows6a = pg_cursor.fetchall()
rows_result6a = [r[0] for r in rows6a]
labels6a = ['1st class', '2nd class', '3rd class']
for label, row in zip(labels6a, rows_result6a):
    print(f'Average fare of {label} passengers: {row:.2f}')

sql_com6b = """
           SELECT AVG(fare), survived
           FROM titanic
           GROUP BY survived;"""
pg_cursor.execute(sql_com6b)
rows6b = pg_cursor.fetchall()
rows_result6b = [r[0] for r in rows6b]
labels6b = ['survivors', 'nonsurvivors']
for label, row in zip(labels6b, rows_result6b):
    print(f'Average fare of {label}: {row:.2f}')

#- How many siblings/spouses aboard on average, by passenger class? By survival?
sql_com7a = """
           SELECT AVG(sib_spouse_count), pclass
           FROM titanic
           GROUP BY pclass;"""
pg_cursor.execute(sql_com7a)
rows7a = pg_cursor.fetchall()
rows_result7a = [r[0] for r in rows7a]
labels7a = ['1st class', '2nd class', '3rd class']
for label, row in zip(labels7a, rows_result7a):
    print(f'Average number of siblings/spouses of {label} passengers: {row:.2f}')

sql_com7b = """
           SELECT AVG(sib_spouse_count), survived
           FROM titanic
           GROUP BY survived;"""
pg_cursor.execute(sql_com7b)
rows7b = pg_cursor.fetchall()
rows_result7b = [r[0] for r in rows7b]
labels7b = ['survivors', 'nonsurvivors']
for label, row in zip(labels6b, rows_result7b):
    print(f'Average number of siblings/spouses of {label}: {row:.2f}')


#- How many parents/children aboard on average, by passenger class? By survival?
sql_com8a = """
           SELECT AVG(parent_child_count), pclass
           FROM titanic
           GROUP BY pclass;"""
pg_cursor.execute(sql_com8a)
rows8a = pg_cursor.fetchall()
rows_result8a = [r[0] for r in rows8a]
labels8a = ['1st class', '2nd class', '3rd class']
for label, row in zip(labels8a, rows_result8a):
    print(f'Average number of parents/children of {label} passengers: {row:.2f}')

sql_com8b = """
           SELECT AVG(parent_child_count), survived
           FROM titanic
           GROUP BY survived;"""
pg_cursor.execute(sql_com8b)
rows8b = pg_cursor.fetchall()
rows_result8b = [r[0] for r in rows8b]
labels8b = ['survivors', 'nonsurvivors']
for label, row in zip(labels6b, rows_result8b):
    print(f'Average number of parents/children of {label}: {row:.2f}')

# #- Do any passengers have the same name?
# sql_com9 = """
# """

# # - (Bonus! Hard, may require pulling and processing with Python) How many married
# #   couples were aboard the Titanic? Assume that two people (one `Mr.` and one
# #   `Mrs.`) with the same last name and with at least 1 sibling/spouse aboard are
# #   a married couple. 
# sql_com4 = """
# """


