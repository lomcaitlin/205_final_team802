from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import requests, json

app = Flask(__name__)
bootstrap = Bootstrap(app)

ratings = {}

@app.route('/') # TODO: update template to look pretty :')
def index():
    r = requests.get('https://api.openbrewerydb.org/breweries')
    data = r.json()
    return render_template('index.html', list=data)

@app.route('/like')
def up():
    print("up")
    return "test"

@app.route('/dislike')
def down():
    print("down")
    return "test"