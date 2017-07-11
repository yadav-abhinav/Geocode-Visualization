import urllib
import json
import sqlite3

apiURL="http://maps.googleapis.com/maps/api/geocode/json?"
conn=sqlite3.connect("geoCode.sqlite")
cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Locations(address TEXT,geoCode TEXT)''')

fHandle=open("locations.data")
count=0

for line in fHandle:
    if count>100:
        print 'Retrieved 100 records. Please restart to proceed'
        break
    loc=line.strip()
    cur.execute('''SELECT geoCode FROM Locations WHERE address=?''',(buffer(loc),))

    try:
        data=cursor.fetchone()[0]
        print 'Geocode found for address',loc
        continue
    except:
        pass

    # Fetching data from Google GeoCoding api

    URL=apiURL + urllib.urlencode({"sensor":"false","address":loc})

    urlOpen=urllib.urlopen(URL)
    dataJSON=urlOpen.read()

    count=count+1

    try:
        js=json.loads(str(dataJSON))
    except:
        continue

    if js[status] != 'OK':
        print "FAILED TO RETRIEVE"
        print dataJSON
        continue

    
