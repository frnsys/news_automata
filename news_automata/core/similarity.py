"""
Similarity
==============

Calculates the similarity between two articles.
"""

from datetime import datetime, timedelta
from mongoengine import Q

from news_automata.models import Article

def top_similar_articles(published, concepts, top_n=10):
    threshold = 5

    # Filter by time first.
    articles = Article.objects(Q(created_at__lte=published + timedelta(days=3)) & Q(created_at__gte=published - timedelta(days=3)))

    # Filter by concepts.
    # We use some arbitrary concept overlap threshold.
    return [article for article in articles if len(set(article.concepts).intersection(concepts)) > threshold][:top_n]
