from flask import Flask, request, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
import requests
import json

app = Flask(__name__)
bootstrap = Bootstrap(app)

ratings = {}

def reorder(list):
    # order the rankings dict
    if len(ratings.items()) > 0:
        order = dict(sorted(ratings.items(), key=lambda item: item[1], reverse=True))
    else:
        order = ratings
    # make dict with list ids as key
    temp = {}
    for i in list:
        temp[i['id']] = i
    # ordered list of items
    list = {}
    for id in order:
        if id in temp:
            list[id] = temp[id]
            list[id]["likes"] = order[id]
            temp.pop(id)
    for leftover in temp:
        list[leftover] = temp[leftover]
    return list

@app.route('/')
def index():
    r = requests.get('https://api.openbrewerydb.org/breweries')
    data = r.json()
    data = reorder(data)
    return render_template('index.html', list=data)

@app.route('/about')
def about():
    return render_template('about.html')

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
    res = reorder(res)
    return render_template('index.html', list=res)

@app.route('/like/<id>')
def up(id):
    if id in ratings:
        ratings[id] += 1;
    else:
        ratings[id] = 1;
    # return redirect(request.referrer)
    return redirect(url_for('index'))

@app.route('/dislike/<id>')
def down(id):
    if id in ratings:
        ratings[id] -= 1;
    else:
        ratings[id] = -1;
    # return redirect(request.referrer)
    return redirect(url_for('index'))

@app.route('/breweries/<brewery_id>')
def brewery(brewery_id):
    r = requests.get(f'https://api.openbrewerydb.org/breweries/{brewery_id}')
    data = r.json()
    return render_template('brewery.html', brewery = data)

if __name__ == "__main__":
    app.run(debug=True)
