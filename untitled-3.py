from peewee import *

db = SqliteDatabase('statistic.db')

class Staturl(Model):
    longurl = CharField()
    shorturl = CharField()
    Statisticurl = FloatField(null=True)

    class Meta:
        database = db
        table_name = "staturl"