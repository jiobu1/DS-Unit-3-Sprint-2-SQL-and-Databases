import sqlite3


connection = sqlite3.connect('table.db')
print("CONNECTION:", connection)

cursor = connection.cursor()
print("CURSOR", cursor)

create_query = """
            CREATE TABLE IF NOT EXISTS blank (
                id SERIAL PRIMARY KEY,
                column1 INTEGER,
                column2 VARCHAR(30)
            );
"""

cursor.execute(create_query)

insert_query = """
INSERT INTO blank (id, column1, column2) values(1, 10, 'Jisha');"""

cursor.execute(insert_query)

select_query = """SELECT * FROM blank"""
cursor.execute(select_query).fetchall()
print(cursor.execute(select_query).fetchall())

insert_query1 = """
INSERT INTO blank (id, column1, column2) values(2, 35, 'Jennifer');"""
cursor.execute(insert_query1)

insert_query2 =  """
INSERT INTO blank (id, column1, column2) values(3, 29, 'Theda');"""
cursor.execute(insert_query2)

select_query1 = """SELECT * FROM blank"""
print(cursor.execute(select_query1).fetchall())
