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


def psql_insert_copy(table, conn, keys, data_iter):
    dbapi_conn = conn.connection
    with dbapi_conn.cursor() as cur:
        s_buf = StringIO()
        writer = csv.writer(s_buf)
        writer.writerows(data_iter)
        s_buf.seek(0)
        columns = ', '.join('"{}"'.format(k) for k in keys)
        if table.schema:
            table_name = '{}.{}'.format(table.schema, table.name)
        else:
            table_name = table.name
        sql = 'COPY {} ({}) FROM STDIN WITH CSV'.format(table_name, columns)
        cur.copy_expert(sql=sql, file=s_buf)


load_dotenv() #> loads contents of the .env file into the script's environment

URL = os.getenv('URL', default = "OOPS")
engine = create_engine(URL)


CSV_FILEPATH = os.path.join(os.path.dirname(__file__), "titanic.csv")
titanic = pandas.read_csv(CSV_FILEPATH)

titanic.to_sql('my_table', engine, method=psql_insert_copy)