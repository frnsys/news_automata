import json
from news_automata.models import Article
from news_automata.core.concepts import concepts

from datetime import datetime
from dateutil.parser import parse

datapath = '/Users/ftseng/Desktop/articles.json'

with open(datapath, 'r') as data:
    for article in json.load(data):
        # Handle MongoDB JSON dates.
        date = article['created_at']['$date']
        if isinstance(date, int):
            article['created_at'] = datetime.fromtimestamp(date/1000)
        else:
            article['created_at'] = parse(article['created_at']['$date'])

        Article(
                title=article['title'],
                text=article['text'],
                created_at=article['created_at'],
                concepts=concepts(article['text']))
