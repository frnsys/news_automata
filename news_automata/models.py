import datetime
from news_automata import db

class Article(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    text = db.StringField(required=True, unique=True)
    title = db.StringField(required=True, unique=True)
    concepts = db.ListField(db.StringField(), required=True)

    meta = {
            'allow_inheritance': True,
            'indexes': ['-created_at'],
            'ordering': ['-created_at']
    }
