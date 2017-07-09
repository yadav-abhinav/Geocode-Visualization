import urllib
import json
import sqlite3

apiURL="http://maps.googleapis.com/maps/api/geocode/json?"
conn=sqlite3.connect("geoCode.sqlite")
cursor=conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Locations(address TEXT,geoCode TEXT)''')
