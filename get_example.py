
from flask import Flask, abort, redirect, url_for, render_template, request  
app = Flask(__name__)  

import random

d = {'wiki': 'https://ru.wikipedia.org', 'google': 'https://google.com', 'abc123': 'https://my.site.ru'}

def random_url():
    x = 'http://127.0.0.1:5000/'
    for i in range (0, 10):
        x = x+random.choice('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz')
    return x

d = {'wiki': 'https://ru.wikipedia.org', 'google': 'https://google.com', 'abc123': 'https://my.site.ru'}

@app.route('/',methods = ['GET'])
def login():
    return render_template('login.html')
  
@app.route('/shorten',methods = ['POST'])  
def shorten():
    shorturl = random_url()
    longurl=request.args.get('longurl')  
    d[shorturl[22::]] = longurl  
    return shorturl

@app.route('/<ip>')
def index(ip):
    return redirect(d[ip])
   
if __name__ == '__main__':  
    app.run(debug = True)