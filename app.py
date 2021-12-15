from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
import requests
import json



app = Flask(__name__)
bootstrap = Bootstrap(app)

ratings = {}

@app.route('/')
def index():
    r = requests.get('https://api.openbrewerydb.org/breweries')
    data = r.json()
    return render_template('index.html', list=data)


@app.route('/about')
def about():
    r = requests.get('https://api.openbrewerydb.org/breweries')
    data = r.json()
    return render_template('about.html',list=data)


@app.route("/search", methods=['POST'])
def searchBrewery():
    r = requests.get('https://api.openbrewerydb.org/breweries')
    data = r.json()
    text = request.form['breweryName']
    res = []
    for i in range(len(data)):
        print(data[i])
        if text.lower() in data[i]['name'].lower():
            res.append(data[i])
    return render_template('index.html', list=res)


@app.route('/like')
def up():
    print("up")
    return "test"


@app.route('/dislike')
def down():
    print("down")
    return "test"

@app.route('/breweries/<brewery_id>')
def brewery(brewery_id):
    r = requests.get(f'https://api.openbrewerydb.org/breweries/{brewery_id}')
    data = r.json()
    return render_template('brewery.html', brewery = data)


if __name__ == "__main__":
    app.run(debug=True)