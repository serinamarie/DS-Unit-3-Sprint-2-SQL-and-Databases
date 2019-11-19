# imports
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# load data
df = pd.read_csv('titanic.csv')

# elephantsql
database = 'soegyzdx'
user = 'soegyzdx'
password = '5hH2U1n9Xj5lCEqPzDKS1iV18MHef2jS'
host = 'salt.db.elephantsql.com'

# connect to python postgresql db adapter
pg_conn = psycopg2.connect(database=database, user=user, password=password,
                           host=host)

# create cursor obj
curs = pg_conn.cursor()

# TABLE TO INSERT INTO
'''
create_passenger_table = """
    CREATE TABLE passenger (
        id INT,
        survived INT,
        pclass INT,
        name VARCHAR(30),
        sex VARCHAR(10),
        age REAL,
        siblings_spouses_aboard INT,
        parents_children_aboard INT,
        fare REAL
    );
"""

curs.execute(create_passenger_table)

pg_connect.commit()
'''

db_string = 'postgres://soegyzdx:5hH2U1n9Xj5lCEqPzDKS1iV18MHef2jS@salt.db.elephantsql.com:5432/soegyzdx'
engine = create_engine(db_string)

pg_conn_2 = engine.connect()

'''
df.to_sql('Titanic', pg_conn_2)
'''

pg_conn.close()

pg_conn_2.close()
