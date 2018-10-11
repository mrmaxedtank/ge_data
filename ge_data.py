import requests
import string
import json
import pg
import urllib
import ConfigParser

#Set variables
Config.read('/path/to/conf')
username = Config.get('credentials', 'username')
password = Config.get('credentials', 'password')
hostname = Config.get('database', 'host')
dbname = Config.get('database', 'dbname')
url = 'http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item='
GeUpdated = False

#Fetch osbuddy summary
json_url = 'https://rsbuddy.com/exchange/summary.json'
response = urllib.urlopen(json_url)
osb_data = json.load(response.read())

#Fetch item list
connection = pg.DB(host=hostname, user=username, passwd=password, dbname=dbname)
items = connection.query("select item_id from items")

for item_id in items:
    #Fetch data from official GE database
    official = url + item_id
    official_response = urllib.urlopen(official)
    official_data = json.load(response.read())
    #HERE: parse official_data, compare price with last result for specific item.
    #If different; register new price in new record and set GeUpdated to True
    #If equal; next item    
    official_last_price = connection.execute('select limit 1 price from records where source = ? and item_id = ? order by record_datetime desc', ('osbuddy', item_id))
    official_new_price = 
    if last_price <> new_price
        #Insert record into database
        GeUpdated = True
    else
    break
    
    #Below, take right element from "osb_data". item_id can be used to identify the right element.
    osbuddy = 
    #Compare osbuddy price to last osbuddy price
    #If different; register new price
    #If equal; next    
break

if GeUpdated == True
    #Create notification
    #Create record in third table; "updates"?
end

connection.close()
