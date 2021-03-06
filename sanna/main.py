#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'wmkeilLinguist'

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
app.config['MONGO_URI'] = 'mongodb://Sanna:sanna1974@ds133166.mlab.com:33166/langilsna'

mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template("/index.html")

@app.route('/word/<word>', methods=['GET', 'POST'])
def wordDisplay(word):
    result = request.args.get('searchword')
    db = mongo.db.sannaWords
    entry = db.find_one({"English meaning": word}) or db.find_one({"Sanna word": word})
    return render_template('word.html', word=word, entry=entry, result=result)

@app.route('/results', methods=['GET', 'POST'])
def resultDisplay():
    word = request.args.get('searchword')
    db = mongo.db.sannaWords
    entries = db.find({"$or": [
     {"English meaning": { "$regex": "%s" % word}},
     {"Sanna word": { "$regex": "%s" % word} }
    ]})

    # for entry in entries:
    #     print(entry['Sanna word'])

    return render_template('results.html', word=word, entries=entries)

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
    raw = open("cypriotArabic.txt", "rU", encoding="utf-8").read()
    result = request.args.get("searchword")
    
    concordance = get_concordance(str(word), raw)
    for phrase in concordance:
        print(phrase)
    return render_template('corpusLookup.html', concordance=concordance, result=result, word=word)


"""MUST be at end of program | CONFIG FOR HEROKU DEPLOYMENTS"""
if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)	
