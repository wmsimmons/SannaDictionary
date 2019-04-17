#!/usr/bin/env python
# -*- coding: utf-8 -*-

from corpusLookup import get_concordance
from flask import Flask, flash
from flask_bootstrap import Bootstrap
from flask import render_template, request, url_for
from flask_pymongo import PyMongo
from nltk import * 
import os


app = Flask(__name__)
Bootstrap(app)

"""for the app and mongo configs"""
app.config['SECRET_KEY'] = '3bjd&hdj3%7@hdmSAN&**NA&**DICT&**%$324d'
app.config['MONGO_DBNAME'] = 'sanna'
app.config['MONGO_URI'] = 'mongodb://LinguistLango:Australia7!@ds133166.mlab.com:33166/langilsna'

mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("/index.html")

@app.route('/word/<word>', methods=['GET', 'POST'])
def wordDisplay(word):
    result = request.args.get('searchword')
    db = mongo.db.sannaWords
    entry = db.find_one({"English meaning":word}) or db.find_one({"Sanna word":word})
    return render_template('word.html', word=word, entry=entry, result=result)

@app.route('/results', methods=['GET', 'POST'])
def resultDisplay():
    word = request.args.get('searchword')
    return render_template('results.html', word=word)

@app.route('/aboutproject')
def aboutProj():
	return render_template('aboutProject.html')

@app.route('/contextsearch', methods=['GET', 'POST'])
def concordanceSearch():
    context_word = request.args.get('searchword')
    return render_template("concordanceSearch.html", context_word=context_word)

@app.route('/concordanceresults')
def concordResults():
    context_word = request.args.get('searchword')
    return render_template('concordanceResults.html', context_word=context_word)


@app.route('/lookup/<word>')
def concordance(word):
    raw = open("C:/Users/langu/Desktop/qafasTaMalti/sanna/sannadictsite/cypriotArabic.txt", "rU", encoding="utf-8").read()
    result = request.args.get("searchword")
    
    concordance = get_concordance(str(word), raw)
    for phrase in concordance:
        print(phrase)
    return render_template('corpusLookup.html', concordance=concordance, result=result, word=word)


"""MUST be at end of program"""
if __name__ == '__main__':
    app.run(debug=False)	
