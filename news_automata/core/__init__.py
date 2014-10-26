from datetime import datetime
from . import similarity, evaluator, extractor, concepts, summarizer
from ..models import Article

def get_articles(url):
    """
    Pass in a url of some article, and get
    articles talking about the same thing.
    """
    # Extract data from the url.
    entry_data, html = extractor.extract_entry_data(url)

    text = entry_data.cleaned_text
    title = entry_data.title
    published = entry_data.publish_date or datetime.utcnow() # default to now, not very accurate tho
    cons = concepts.concepts(' '.join([title, text]))

    social_media_score = evaluator.score(url)

    articles = similarity.top_similar_articles(published, cons)

    # Score and summarize each article
    for article in articles:
        if not article.summary:
            article.score = evaluator.score(article.url)
            article.summary = summarizer.summarize(article.title, article.text)
            article.save()

    # Sort the articles by popularity score.
    articles.sort(key= lambda x: x.score, reverse=True)
    return articles


def query_articles(query):
    """
    Search articles based on a concept query.
    """
    #articles = list(Article.objects(concepts__in=[query]).order_by('-score')[:25])
    articles = list(Article.objects(concepts__iexact=query).order_by('-score')[:25])

    # Score and summarize each article
    for article in articles:
        if not article.summary:
            article.score = evaluator.score(article.url)
            article.summary = summarizer.summarize(article.title, article.text)
            article.save()

    return articles
