"""
This loads an argos.corpora article dump into mongo
in a way this program can use.
"""

from news_automata.models import Article
from news_automata.core import evaluator

total = len(Article.objects)
print(total)
for idx, article in enumerate(Article.objects):
    print(idx/total)
    if article.score == 0:
        article.score = evaluator.score(article.url)
        article.save()
