from datetime import datetime, timedelta

from news_automata.core import evaluator, extractor, concepts
from news_automata.models import Article

#url = sys.argv[1]
url = 'http://dealbook.nytimes.com/2014/10/13/calculating-the-grim-costs-of-ebola/'

# Extract data from the url.
#entry_data, html = extractor.extract_entry_data(url)

#text = entry_data.cleaned_text
#title = entry_data.title
published = entry_data.publish_date or datetime.utcnow()
#cons = concepts.concepts(' '.join([title, text]))

#social_media_score = evaluator.score(url)

# Filter by time first.
articles = Article.objects(Q(created_at__lte=published + timedelta(days=3)) & Q(created_at__gte=published - timedelta(days=3)))

# Filter by concepts.
# We set some arbitrary concept overlap threshold, here we're using 5.
articles = [article for article in articles if set(article.concepts).intersection(cons) > 5]

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
