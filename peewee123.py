from flask import Flask, abort, redirect, url_for, render_template, request  
from peewee import *
import random
app = Flask(__name__)

db = SqliteDatabase('statistic.db')
class Staturl(Model):
    longurl = CharField()
    shorturl = CharField()
    Statisticurl = FloatField(null=True)

    class Meta:
        database = db

Staturl.create_table()

def add_url(long, short):
    row = Staturl(longurl = long, shorturl = short, Statisticurl = 0)
    row.save()
    
def update_stat(ip):
    stat = Staturl.get(Staturl.shorturl == ip)
    stat.Statisticurl +=1
    stat.save()
    
def get_stat(short):
    stat = Staturl.get(Staturl.Statisticurl == short)
    return stat.Statisticurl

def get_shorturl(short):
    stat = Staturl.get(Staturl.shorturl == short)
    return stat.shorturl

def random_string():
    x = ''
    for i in range (0, 10):
        x = x+random.choice('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz')
    return x

Staturl.create_table()

@app.route('/',methods = ['GET'])
def index():
    return render_template('index.html')
  
@app.route('/shorten',methods = ['POST', 'GET'])  
def shorten():
    x = request.url_root
    shorturl = x + random_string()
    longurl=request.args.get('longurl')
    if(longurl[:4:] != 'http'):
        longurl = 'https://' + longurl
    row = Staturl.create(longurl = longurl, shorturl = shorturl, Statisticurl = 0)
    for person in Staturl.select():
        print(person)    
    return shorturl

@app.route('/getstatistics', methods = ['GET'])
def getstatistics():
    return render_template('statistics.html')

@app.route('/statistics', methods = ['POST', 'GET'])
def statistics():   
    x = request.url_root
    staturl=request.args.get('staturl')
    return 'Statistics ' +  str(get_stat(staturl))

@app.route('/<ip>', methods = ['POST', 'GET'])
def redir(ip):
    update_stat(ip)
    return redirect(get_shorturl(ip))

if __name__ == '__main__':  
    app.run(debug = True)