from flask import render_template,request,redirect,url_for
from . import main
from ..requests import get_news,get_articles
from ..models import News

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    sports_news = get_news("sports")
    entertainment_news = get_news("entertainment")
    business_news = get_news("business")
    title = "News App - Where news live on"
    return render_template('index.html' , title = title, sports_news = sports_news,entertainment_news = entertainment_news, business_news = business_news)  #, 

@main.route('/news/<id>')
def articles(id):
	'''
	view articles page
	'''
	articles = get_articles(id)

	title = f'NH | {id}'

	return render_template('articles.html',title= title,articles = articles)

