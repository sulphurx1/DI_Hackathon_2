from datetime import datetime
import database as db

# create an instance of the DatabaseNews class
db_news = db.DatabaseNews()

# create a dictionary representing a news item
news_item2 = {
    'title': 'Test news item2',
    'link': 'https://example.com/news/test2',
    'keywords': 'test, news2',
    'creator': 'John Dont',
    'video_url': 'https://example.com/news/test/video',
    'description': 'This is a test news item.',
    'content': 'hasdsff',
    'pub_date': '2022-02-03 10:30:40',
    'full_description': 'This is the full description of the test news item.',
    'image_url': 'https://example.com/news/test/image.jpg',
    'source_id': 'example.com',
    'country': 'US',
    'category': 'test',
    'business': 'test business',
    'language': 'en'
}

# call the update_news_table method with the news item dictionary
db_news.update_news_table(news_item2)
