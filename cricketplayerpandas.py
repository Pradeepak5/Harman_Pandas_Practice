import pandas as pd
import sqlite3 as sql
connection=sql.connect("Cricketer.db")

df=pd.read_sql_query("select * from Player",connection)
print(df.head(1))
print(df.tail(1))
print(df.info())
