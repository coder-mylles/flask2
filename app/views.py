from flask import render_template
from app import app
from .request import get_news

# Views
@app.route('/')
@@ -8,5 +9,7 @@ def index():
    '''
    View root page function that returns the index page and its data
    '''

    articles_found = get_news("sports")
    title = "News App - Where news live on"
    return render_template('index.html' , title = title) 
    return render_template('index.html' , title = title, articles_found = articles_found )