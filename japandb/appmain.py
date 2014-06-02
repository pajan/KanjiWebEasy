# appmain.py
# root thing

from flask import Flask, redirect
from japandb import data, templates

app = Flask(__name__)
templates.setup(app)

@app.route('/')
def index():
    return templates.render('index',
        kanji_count=data.get_kanji_count(),
        kanji_total = data.get_kanji_total(),
        word_count=data.get_word_count(),
        word_total = data.get_word_total()
    )

@app.route('/kanji/<kanji>')
def show_kanji(kanji):
    info = data.get_kanji_info(kanji)
    if not info:
        return redirect('/')
    return templates.render('kanji', kanji=kanji, info=info, words=info['words'])

@app.route('/word/<word>')
def show_word(word):
    word_info = data.get_word_info(word)
    if not word_info:
        return redirect('/')
    
    # flatten kanji array
    word_info['kanji'] = list(''.join(word_info['kanji']))
    
    return templates.render('word', word=word, info=word_info)
