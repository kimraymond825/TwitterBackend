from flask import Flask
from flask import jsonify
import json
from flask import request


app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Twitter Backend"

@app.route('/like')
def like():
    return jsonify(like = 10)

@app.route('/like/create')
def like_create():
    return jsonify(like = 10)

@app.route('/like/read')
def like_read():
    data_as_dict = readit("like.txt")
    return jsonify(data_as_dict)

@app.route('/like/update', methods = ['POST'])
def like_update():
    requested_value = int(request.form['like'])
    data_as_dict = updateit("like.txt","like", requested_value)
    return jsonify(data_as_dict)

@app.route('/retweet')
def retweet():
    return jsonify(Retweet = 10)


@app.route('/retweet/create')
def retweet_create():
    return jsonify(Retweet = 10)

@app.route('/retweet/read')
def retweet_read():
    data_as_dict = readit("retweet.txt")
    return jsonify(data_as_dict)

@app.route('/retweet/update', methods = ['POST'])
def retweet_update():
    requested_value = int(request.form['retweet'])
    data_as_dict = updateit("retweet.txt", "retweet", requested_value)
    return jsonify(data_as_dict)


"""
Open file.

PATH:
    ** PWD = "/Users/Owner/Desktop/Code/twitterBackend/"

    1. Absoulte path => "/Users/Owner/Desktop/Code/twitterBackend/server.py"
    2. Relative path => "server.py"

def open(filename, permission, ...):
    ...

permissions:
 - w(write)
 - w+(read and write)
 - r(read)
 - r+(read and write)
 - a(append)
 ...
"""
def read_data(filename):
    with open(filename) as f:
        content = f.read()
        print(content)
        return content

def write_data(filename, content):
    with open(filename, 'w') as f:
        print(content)
        f.write(content)

def readit(filename):
    data = read_data(filename)
    data_as_dict = json.loads(data)
    return data_as_dict

def updateit(filename, keyname, requested_value):
    data_as_dict = readit(filename)
    value = data_as_dict[keyname]
    value += requested_value
    data_as_dict[keyname] = value
    data_as_string = json.dumps(data_as_dict)
    write_data(filename, data_as_string)
    return data_as_dict




app.run(debug = True)