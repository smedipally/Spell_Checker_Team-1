from flask import Flask
from flask import request
from nltk.util import pr
from textblob import TextBlob
from flask_cors import CORS, cross_origin
import enchant
import sys
from textblob import Word
from textblob import en
from textblob.en import suggest
import json
app = Flask(__name__)
CORS(app)



#irish_dict = enchant.PyPWL("abcd.txt")

irish_dict = enchant.request_pwl_dict("irishwebf.txt")

@app.route('/en', methods = ['GET','POST'])
def english():
    data = str(request.form['words'])
    w = Word(data)
    suggests = w.spellcheck()
    suggestions = []
    for suggest in suggests:
        suggestions.append(suggest[0])
    print(suggestions)
    return json.dumps(suggestions) #str(suggestions)

    # data1 = TextBlob(data)
    # print(data1)
    # return str(data1.correct())

@app.route('/ir', methods = ['GET','POST'])
def irish():
    irish_word = str(request.form['words'])
    if(not irish_word or irish_word == " "): 
        return json.dumps([])
    word_exists = irish_dict.check(irish_word)
    if word_exists:
        return json.dumps([irish_word])
    else:
        suggestions = irish_dict.suggest(irish_word)
        print(suggestions)
        print(json.dumps(suggestions))
        return json.dumps(suggestions,ensure_ascii=False)


# @app.route('/ir', methods = ['GET','POST'])
# def irish():
#     res =""
#     irish_words = (request.form['words']).split(" ")
#     for irish_word in irish_words:
#         word_exists = irish_dict.check(irish_word)
#         if word_exists:
#             res = res + " " + irish_word
#         if not word_exists:
#             suggestions = irish_dict.suggest(irish_word)
#             res = res + " " + suggestions[0]
#     return res

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
