import sqlite3 as sql

db = sql.connect('news.db')
cursor = db.cursor()
x = cursor.execute("SELECT * FROM news")
x = cursor.fetchone()
print(x)
