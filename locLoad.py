# Various library modules included
import urllib
import json
import sqlite3

apiURL="http://maps.googleapis.com/maps/api/geocode/json?" # The Google GeoCodig API to fetch data in JSON
conn=sqlite3.connect("geoCode.sqlite")  # Creates a connection to sqlite database
cursor=conn.cursor()  # Cursor/handler to sqlite connection

# SQL command to create a new table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Locations(address TEXT,geoCode TEXT)''')

# Open a file to fetch locations from a file
fHandle=open("locations.data")

for line in fHandle:

    # Checks if JSON data for a particular location is present in the database or not
    loc=line.strip()
    cursor.execute('''SELECT geoCode FROM Locations WHERE address=?''',(buffer(loc),))

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
    #print dataJSON  # For testing

    # Checks whether JSON data was fetched successfully or not
    try:
        js=json.loads(str(dataJSON))
        print "Fetched data for:",loc
    except:
        continue

    # Checks the STATUS in the received JSON data
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print "FAILED TO RETRIEVE"
        continue

    # Stores the JSON data in the database
    cursor.execute('''INSERT INTO Locations(address,geoCode) VALUES(?,?)''',(buffer(loc),buffer(dataJSON)))

# Comiit all the changes in the database
conn.commit()

# For fetching JSON data for more location, add them in the 'locations.data' file
