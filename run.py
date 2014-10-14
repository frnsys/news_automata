from datetime import datetime
from news_automata.core import similarity, evaluator, extractor, concepts

#url = sys.argv[1]
url = 'http://dealbook.nytimes.com/2014/10/13/calculating-the-grim-costs-of-ebola/'

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

# Sort the articles by score.
articles.sort(key= lambda x: x.score, reverse=True)
print(articles)

"""
[X] Extract entry data
[X] Score the url
- Search the database for articles sharing the same concepts.
    - For each result, filter by data (within +/- 3 days of this one)
    - For each remaining result, calculate similarity
    - Filter by threshold
    - For each remaining result, summarize each
    - Sort by social media score
- ``

TO DO:
- Load articles into mongo with concepts
"""
