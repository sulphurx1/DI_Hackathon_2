# use SQL Alchemy to create an sql lite database

# create a table for news  with the following fields

# if the table exists, do not create it again
# "title": text
# "link": text
# "keywords": text
# "creator":text
# "video_url": text
# "description": text
# "Content": text
# "pubDate": date
# "full_description": text
# "image_url": text
# "source_id": text
# -"country": text
# -"category": text
# "business":text
# "language":text
# news key - primary key

# create a class for updating the table with new data
# pass the parameters from API news to the table
# map the API news to the table fields:  # "title": text
# "link": text
# "keywords": text
# "creator":text
# "video_url": text
# "description": text
# "Content": text
# "pubDate": date
# "full_description": text
# "image_url": text
# "source_id": text
# -"country": text
# -"category": text
# "business":text
# "language":text

# create a function to transform this date
# "pubDate": "2022-02-03 10:30:40",
# to 2022-02-03

import os.path
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3
import os.path

engine = create_engine('sqlite:///news.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class News(Base):
    __tablename__ = 'newstable'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    link = Column(String)
    keywords = Column(String)
    creator = Column(String)
    video_url = Column(String)
    description = Column(String)
    content = Column(String)
    pub_date = Column(Date)
    full_description = Column(String)
    image_url = Column(String)
    source_id = Column(String)
    country = Column(String)
    category = Column(String)
    business = Column(String)
    language = Column(String)


db_file = 'news.db'
if not os.path.isfile(db_file):
    Base.metadata.create_all(engine)


def update_news_table(news):
    # news take a list of news items
    if not isinstance(news, list):
        news = [news]
    for item in news:
        # Transform pubDate to date
        pub_date = datetime.strptime(
            item['pubDate'], '%Y-%m-%d').date()

        # Create a News object
        news_item = News(
            title=item['title'],
            link=item['link'],
            keywords=item['keywords'],
            creator=item['creator'],
            video_url=item['video_url'],
            description=item['description'],
            content=item['content'],
            pub_date=pub_date,
            full_description=item['full_description'],
            image_url=item['image_url'],
            source_id=item['source_id'],
            country=item['country'],
            category=item['category'],
            business=item['business'],
            language=item['language']
        )

        # Add the News object to the session and commit the changes
        session.add(news_item)
        session.commit()
