from peewee import *

db = SqliteDatabase('statistic.db')

class Staturl(Model):
    longurl = CharField()
    shorturl = CharField()
    Statisticurl = CharField()

    class Meta:
        database = db
        table_name = "staturl"