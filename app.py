#importing libraries
import os
import numpy as np
import flask
import pickle
from flask import Flask, render_template, request
import praw
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Use pickle to load in the pre-trained model.
loaded_model = pickle.load(open("model/model.pkl", 'rb'))

reddit = praw.Reddit(client_id='R30fcxAZLJ7Wyw',
                     client_secret='8Zf87krHYa_zXRXPWEF8hK2Twfs',
                     user_agent='project1',
                     username = 'gbatra',
                     password = "HOLYMOLY1999"
                    )

flairs={0:'Politics',1:'Non-Political',2:'AskIndia', 3:"[R]eddiquette", 4:'Science/Technology', 5:'Policy/Economy', 6:'Business/Finance', 7:'Scheduled', 8:'Sports', 9:'Food', 10:'Photography', 11:'AMA', 12:'Coronavirus'}

def preprocess_input(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text)
    filtered_sentence = [w for w in word_tokens if not w in stop_words]
    filtered_sentence = ''
    for w in word_tokens:
        if w not in stop_words:
            if w.isalnum():
                w = w.lower()
                filtered_sentence = filtered_sentence + ' ' + w
    filtered_sentence = " ".join(filtered_sentence.split())
    return(filtered_sentence)


def detect_flair(url,loaded_model):

    submission = reddit.submission(url=url)

    data = {}

    data['title'] = submission.title
    data['url'] = submission.url

    submission.comments.replace_more(limit=None)
    comment = ''
    for top_level_comment in submission.comments:
        comment = comment + ' ' + top_level_comment.body

    data["comment"] = comment
    data['title'] = preprocess_input(data['title'])
    data['comment'] = preprocess_input(data['comment'])
    data['combine'] = data['title'] + ' ' + data['comment']

    return flairs[loaded_model.predict([data['title']])[0]]


#creating instance of the class
app=Flask(__name__)

#to tell flask what url shoud trigger the function index()
@app.route('/' ,  methods=['GET', 'POST'])
# @app.route('/index')
def index():
    if flask.request.method == 'GET':
        return flask.render_template('index.html')

    if flask.request.method == 'POST':
        url = flask.request.form['posturl']
        prediction = detect_flair(url, loaded_model)
        return flask.render_template('index.html', result = str(prediction))

if __name__=='__main__':
    app.secret_key = os.urandom(12)
    app.run(host='0.0.0.0', debug=True)