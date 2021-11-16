from flask import *
from flask import request
from nltk.util import pr
from textblob import TextBlob
from flask_cors import CORS, cross_origin
import enchant
import sys

app = Flask(__name__)
CORS(app)
irish_dict = enchant.PyPWL("words.txt")

@app.route('/en', methods = ['GET','POST'])
def english():
    data = str(request.form['words'])
    data1 = TextBlob(data)
    print(data1)
    return str(data1.correct())

@app.route('/ir', methods = ['GET','POST'])
def irish():
    res =""
    irish_words = (request.form['words']).split(" ")
    irish_words1 = []
    for irish_word in irish_words:
        if(irish_word!=''):
            irish_words1.append(irish_word)
    for irish_word in irish_words1:
        word_exists = irish_dict.check(irish_word)
        if word_exists:
            res = res + " " + irish_word
        if not word_exists:
            suggestions = irish_dict.suggest(irish_word)
            res = res + " " + suggestions[0]
    print(irish_words)
    return res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
