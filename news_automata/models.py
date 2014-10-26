import datetime
from news_automata import db

class Article(db.Document):
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    text = db.StringField(required=True)
    title = db.StringField(required=True)
    url = db.StringField(required=True)
    concepts = db.ListField(db.StringField())
    summary = db.ListField(db.StringField())
    score = db.FloatField()

    meta = {
            'allow_inheritance': True,
            'indexes': ['-created_at'],
            'ordering': ['-created_at']
    }
