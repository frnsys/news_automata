from flask import render_template, request, jsonify

from news_automata import app
from .core import get_articles, query_articles

@app.route('/', methods=['GET', 'POST'])
def index():
    form = InputForm()
    if form.validate_on_submit():
        url = form.url.data
        results = get_articles(url)
        return render_template('results.html', results=results)
    return render_template('index.html', form=form)


@app.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form['query']
    articles = query_articles(query)
    data = {'results':[]}
    for article in articles:
        data['results'].append({
                'title': article.title,
                'url': article.url,
                'concepts': article.concepts,
                'summary': article.summary,
                'popularity': article.score,
                'published': article.created_at
        })
    return jsonify(data)


from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import Required

class InputForm(Form):
    url = StringField('url', validators=[Required()])
