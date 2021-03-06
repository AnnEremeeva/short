
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
    
def update_stat(ip):
    stat = Staturl.get(Staturl.shorturl == ip)
    stat.Statisticurl +=1
    stat.save()
    
def get_stat(short):
    stat = Staturl.get(Staturl.shorturl == short)
    return stat.Statisticurl

def get_shorturl(short):
    stat = Staturl.get(Staturl.shorturl == short)
    return stat.longurl

def random_string():
    x = ''
    for i in range (0, 10):
        x = x+random.choice('AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz')
    return x

Staturl.create_table()


@app.route('/favicon.ico')
def favicon():
    return ''

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
    marker = ''
    for i in Staturl.select():
        if(i.longurl == longurl):
            marker = i.shorturl
    print()
    if(marker == ''):
        row = Staturl.create(longurl = longurl, shorturl = shorturl[len(x)::], Statisticurl = 0)
    else:
        row = Staturl.get(Staturl.longurl == longurl)
    return render_template('short.html', long = row.longurl, short = row.shorturl, stat = x + 'getstatistics')

@app.route('/getstatistics', methods = ['GET'])
def getstatistics():
    return render_template('getstat.html')

@app.route('/statistics', methods = ['POST', 'GET'])
def statistics():   
    x = request.url_root
    staturl=request.args.get('staturl')
    stat = Staturl.get(Staturl.shorturl == staturl[len(x)::])
    a = 'Statistics ' +  str(stat.Statisticurl)
    return render_template('statistics.html', stat = a, long = stat.longurl, short = x + stat.shorturl)

@app.route('/<ip>', methods = ['POST', 'GET'])
def redir(ip):
    update_stat(ip)
    return redirect(get_shorturl(ip))

if __name__ == '__main__':  
    app.run(debug = True)