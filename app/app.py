#!/usr/bin/python

# Basic flask app that takes input from a form and outputs it as a "sideword" pyramid

from flask import Flask, request, render_template
from redis import Redis

app = Flask(__name__)
redis = Redis(host="redis", port=6379)


@app.route('/', methods=['GET', 'POST'])
def create_pyramid():
    if request.method == 'POST':

        character = request.form.get('char')
        number = int(request.form.get('num'))
        hits = redis.get('hits').decode('utf-8')

        return render_template('pyramid.html', number = number, character = character, hits = hits)

    # it's a GET request, increment the page counter and display the input form
    redis.incr('hits')
    return render_template('form.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
