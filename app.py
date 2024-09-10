from random import choice
from translate import Translator
import requests
import json
from flask import Flask, render_template
app = Flask(__name__)

wsgi_app = app.wsgi_app
def translate(text):
    translator= Translator(to_lang="ru")
    translation = translator.translate(text)
    return translation

def getQuote():
    url="https://api.chucknorris.io/jokes/random"
    return requests.get(url).json()["value"]

@app.route('/')
def hello():
    quote = getQuote()
    return render_template("index.html",quote=translate(quote),eng_quote = quote, random = choice(range(1,4)))

if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
