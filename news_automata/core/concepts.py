"""
Conceptor
==============

Concept extraction from text.
"""

import json
import string
from urllib import request, error
from urllib.parse import urlencode

import ner
from sklearn.feature_extraction.text import HashingVectorizer

from config import KNOWLEDGE_HOST
from .vectorize import Tokenizer

def strip(text):
    """
    Removes punctuation from the beginning
    and end of text.
    """
    punctuation = string.punctuation + '“”‘’–"'
    return text.strip(punctuation)

def concepts(docs, strategy='stanford'):
    """
    Named entity recognition on
    a text document or documents.

    Requires that a Stanford NER server or a DBpedia Spotlight
    server is running at argos.conf.APP['KNOWLEDGE_HOST'],
    depending on which strategy you choose.

    Args:
        | docs (list)       -- the documents to process.
        | doc (str)         -- the document to process.
        | strategy (str)    -- the strategy to use, default is `stanford`. can be `stanford` or `spotlight`.

    Returns:
        | list              -- list of all entity mentions
    """
    if type(docs) is str:
        docs = [docs]

    entities = []

    tagger = ner.SocketNER(host=KNOWLEDGE_HOST, port=8080)

    for doc in docs:
        try:
            ents = tagger.get_entities(doc)
        except UnicodeDecodeError as e:
            Exception('Unexpected unicode decoding error: {0}'.format(e))
            ents = {}

        # We're only interested in the entity names,
        # not their tags.
        names = [ents[key] for key in ents]

        # Flatten the list of lists.
        names = [strip(name) for sublist in names for name in sublist]

        entities += names

    return entities


def vectorize(concepts):
    """
    This vectorizes a list or a string of concepts;
    the regular `vectorize` method is meant to vectorize text documents;
    it is trained for that kind of data and thus is inappropriate for concepts.
    So instead we just use a simple hashing vectorizer.
    """
    h = HashingVectorizer(input='content', stop_words='english', norm=None, tokenizer=Tokenizer())
    if type(concepts) is str:
        # Extract and return the vector for the single document.
        return h.transform([concepts]).toarray()[0]
    else:
        return h.transform(concepts)
