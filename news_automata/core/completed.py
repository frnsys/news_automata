from datetime import datetime
from . import similarity, evaluator, extractor, concepts, summarizer

def get_articles_completed(url):
    # Extract data from the url.
    entry_data, html = extractor.extract_entry_data(url)

    text = entry_data.cleaned_text
    title = entry_data.title
    published = entry_data.publish_date or datetime.utcnow() # default to now, not very accurate tho
    cons = concepts.concepts(' '.join([title, text]))

    social_media_score = evaluator.score(url)

    articles = similarity.top_similar_articles(published, cons)

    # Score each article
    for article in articles:
        article.score = evaluator.score(article.url)
        article.summary = summarizer.summarize(article.title, article.text)

    # Sort the articles by score.
    articles.sort(key= lambda x: x.score, reverse=True)
    return articles
