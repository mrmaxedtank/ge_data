import requests
import string
import json
import pg
import urllib
import ConfigParser

#Set variables
Config.read('/path/to/conf')
Username = Config.get('Credentials', 'username')
Password = Config.get('Credentials', 'password')
Hostname = Config.get('Database', 'host')
Dbname = Config.get('Database', 'dbname')
Url = 'http://services.runescape.com/m=itemdb_oldschool/api/catalogue/detail.json?item='
GeUpdated = False

#Fetch osbuddy summary
JsonUrl = 'https://rsbuddy.com/exchange/summary.json'
Response = requests.get(JsonUrl).text
OsbData = json.load(Response)

#Fetch item list
Connection = pg.DB(host=Hostname, user=Username, passwd=Password, dbname=Dbname)
Items = connection.query("select item_id from items")

for ItemId in Items:
    #Fetch data from official GE database
    Official = Url + ItemId
    OfficialResponse = urllib.urlopen(Official)
    OfficialData = json.load(response.read())
    #HERE: parse official_data, compare price with last result for specific item.
    #If different; register new price in new record and set GeUpdated to True
    #If equal; next item    
    OfficialLastPrice = connection.execute('select limit 1 price from records where source = ? and item_id = ? order by record_datetime desc', ('osrs', ItemId))
    OfficialNewPrice = 
    if OfficialLastPrice <> OfficialNewPrice
        #Insert record into database
        #Todo: Check if ID works like this, create variable for timestamp of "now". Create and test this before taking care of osbuddy segment.
        connection.execute('INSERT INTO records (id, record_datetime, item_id, price, source' VALUES (?, ?, ?, ?, ?)', ('', '', ItemId, OfficialNewPrice, 'osrs'))
        GeUpdated = True
    else
        #Add logging for else?
    break
    
    #Below, take right element from "osb_data". item_id can be used to identify the right element.
    OsbuddyLastPrice = connection.execute('select limit 1 price from records where source = ? and item_id = ? order by record_datetime desc', ('osbuddy', ItemId))
    Osbuddy = print(OsbData[ItemId]['overall_average'])
    #Compare osbuddy price to last osbuddy price
    if OsbuddyLastPrice <> Osbuddy
    #If different; register new price
    #If equal; next    
    else
        #Add logging for else?
    break
break

if GeUpdated == True
    #Create notification
    #Create record in third table; "updates"?
end

Connection.close()
