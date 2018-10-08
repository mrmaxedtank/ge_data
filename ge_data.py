import requests
import string
import json
import pg

url1 = 'http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item='
url2 = ''

connection = pg.DB(host=<hostname>, user=<username>, passwd=<password>, dbname=<dbname>)
items = connection.query("select item_id from items")
connection.close()

for item_id in items:
    official = url1 + item_id
    osbuddy = url2 + item_id
    
