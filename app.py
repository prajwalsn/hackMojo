#!/usr/bin/python3
from flask import Flask , render_template
from db import db_utils
import os

# template_dir = "/Users/bhargaviv/hackathon/hackMojo/templates/"
app = Flask(__name__)



@app.route('/home')
def hello():
    return render_template('index.html')
    #return "Hello World!"


@app.route('/get_movie_names',methods = ["GET","POST"])
def get_movie_names():
    result = db_utils.get_movie_names()
    print(result)
    return result


if __name__ == '__main__': 
    print(db_utils.get_movie_names())
    app.run()