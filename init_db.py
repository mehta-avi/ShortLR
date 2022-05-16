import sqlite3

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.execute(f.read())

connection.commit()
connection.close()
