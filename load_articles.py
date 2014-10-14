"""
This loads an argos.corpora article dump into mongo
in a way this program can use.
"""

import json
from news_automata.models import Article
from news_automata.core.concepts import concepts

from datetime import datetime
from dateutil.parser import parse

datapath = '/home/ftseng/articles.json'

with open(datapath, 'r') as data:
    articles = json.load(data)
    total = len(articles)
    print(total)
    for idx, article in enumerate(articles):
        print(idx/total)
        # Handle MongoDB JSON dates.
        date = article['created_at']['$date']
        if isinstance(date, int):
            article['created_at'] = datetime.fromtimestamp(date/1000)
        else:
            article['created_at'] = parse(article['created_at']['$date'])

        a = Article(
                title=article['title'],
                text=article['text'],
                url=article['ext_url'],
                created_at=article['created_at'],
                concepts=concepts(article['text']))
        a.save()
