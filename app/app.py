#!/usr/bin/python

# Basic flask app that takes input from a form and outputs it as a "sideword" pyramid

from flask import Flask, request, render_template
from redis import Redis
#import os

app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route('/', methods=['GET', 'POST'])
def create_pyramid():
    if request.method == 'POST':
        character = request.form.get('char')
        number = int(request.form.get('num'))
        hits = redis.get('hits').decode('utf-8')

        return render_template('pyramid.html', number = number, character = character, hits = hits)

    redis.incr('hits')
    return '''<form method="POST">
		Character: <input type="text" name="char"><br>
		Number: <input type="text" name="num"><br>
		<input type="submit" value="Submit"><br>
           </form>'''


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
