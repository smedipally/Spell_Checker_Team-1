from flask import Flask
from flask import request
from textblob import TextBlob
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
@app.route('/', methods = ['GET','POST'])
def index():
    data = str(request.form['words'])
    data1 = TextBlob(data)
    return str(data1.correct())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


