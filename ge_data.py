import requests
import string
import json
import pg
import urllib

#Fetch osbuddy summary
json_url = 'https://rsbuddy.com/exchange/summary.json'
response = urllib.urlopen(json_url)
osb_data = json.load(response.read())

url = 'http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item='

connection = pg.DB(host=<hostname>, user=<username>, passwd=<password>, dbname=<dbname>)
items = connection.query("select item_id from items")
connection.close()

for item_id in items:
    official = url + item_id
    #Below, take right element from "osb_data". item_id can be used to identify the right element.
    osbuddy = 
    
