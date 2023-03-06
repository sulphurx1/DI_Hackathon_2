import requests
import json
import sqlite3 as sql

conn = sql.connect("Database.db")

cursor = conn.cursor()
cursor.execute('CREATE TABLE News(title TEXT, creator TEXT, description TEXT, content TEXT, pubDate TEXT, image_url TEXT)')

request_post = requests.get('https://newsdata.io/api/1/news?apikey=pub_18376a701dfc2ce56259f7b1ccc11e41718e2&q=sport&country=gb,us&language=en&category=business,entertainment,health,politics,sports')

data = json.loads(request_post.content)

for index in range(len(data['results']) - 1):
    title = ''.join(data['results'][index]['title'])
    creator = ''.join(data['results'][index]['creator'])
    description = (data['results'][index]['description'])
    content = ''.join(data['results'][index]['content'])
    pubDate = ''.join(data['results'][index]['pubDate'])
    image_url = (data['results'][index]['image_url'])

    cursor.execute('INSERT INTO News VALUES (title, creator, description, content, pubDate, image_url)')

cursor.execute('SELECT * from News')
cursor.fetchall()
conn.commit()
conn.close()




