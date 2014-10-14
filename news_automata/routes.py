from flask import render_template

from news_automata import app
from .core import get_articles, get_articles_completed

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        url = form.url.data
        #results = get_articles(url)
        results = get_articles_completed(url)
        return render_template('results.html', results=results)
    return render_template('index.html', form=form)


from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Required

class InputForm(Form):
    url = StringField('url', validators=[Required()])
