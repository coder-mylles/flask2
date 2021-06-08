from flask import render_template
from app import app
from .request import get_news
# Views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    articles_found = get_news("sports")
    sports_news = get_news("sports")
    entertainment_news = get_news("entertainment")
    business_news = get_news("business")
    title = "News App - Where news live on"
    return render_template('index.html' , title = title, articles_found = articles_found ) 
    return render_template('index.html' , title = title, sports_news = sports_news, entertainment_news = entertainment_news, business_news = business_news)

@app.route('/sources/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)

	title = f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles)