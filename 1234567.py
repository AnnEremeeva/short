from flask import abort, redirect, url_for

@app.route('/')
def index():
    return redirect(url_for('login'))



import os
from flask import Flask,redirect

app = Flask(__name__)


d = {'/wiki': 'https://ru.wikipedia.org', '/google': 'https://google.com', '/abc123': 'https://my.site.ru'}
for key in d:
    if(a == key[1::]):
        @app.route(key)
        def proj_redirect():
            return redirect(d[key], code=302)