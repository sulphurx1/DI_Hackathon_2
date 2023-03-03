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

from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os.path


class DatabaseNews:
    def __init__(self):
        self.engine = create_engine('sqlite:///news.db', echo=True)
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()
        self.Base = declarative_base()

        class News(self.Base):
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

        self.News = News

        db_file = 'news.db'
        if not os.path.isfile(db_file):
            self.Base.metadata.create_all(self.engine)

    def update_news_table(self, news):
        if not isinstance(news, dict):
            raise TypeError('News should be a dictionary.')

        try:
            # Check if dictionary has missing keys and replace with 'not provided'
            for key in self.News.__table__.columns.keys():
                if key not in news:
                    news[key] = 'not provided'
            
            # Transform pubDate to date
            pub_date = datetime.strptime(news['pubDate'], '%Y-%m-%d').date()

            # Create a News object
            news_item = self.News(
                title=news['title'],
                link=news['link'],
                keywords=news['keywords'],
                creator=news['creator'],
                video_url=news['video_url'],
                description=news['description'],
                content=news['content'],
                pub_date=pub_date,
                full_description=news['full_description'],
                image_url=news['image_url'],
                source_id=news['source_id'],
                country=news['country'],
                category=news['category'],
                business=news['business'],
                language=news['language']
            )
            
            # Add the News object to the session and commit the changes
            self.session.add(news_item)
            self.session.commit()
        except Exception as e:
            print(f"An exception occurred while updating the news table: {e}")
