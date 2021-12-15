from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
import requests
import json



app = Flask(__name__)
bootstrap = Bootstrap(app)

ratings = {}

r = requests.get('https://api.openbrewerydb.org/breweries')
data = r.json()

@app.route('/')  # TODO: update template to look pretty :')
def index():
    return render_template('index.html', list=data)


@app.route('/about')
def about():
    return render_template('about.html',list=data)


@app.route("/search", methods=['POST'])
def searchBrewery():
    text = request.form['breweryName']
    res = []
    for i in range(len(data)):
        print(data[i])
        if data[i]['name'] == text:
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
    return render_template('brewery.html', list = data, brewery_id = brewery_id)


if __name__ == "__main__":
    app.run(debug=True)