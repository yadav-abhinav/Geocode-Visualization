import sqlite3
import json

conn=sqlite3.connect("geoCode.sqlite")
cursor=conn.cursor()

fHandle=open("locations.js","w")
fHandle.write('myData=[\n')
cursor.execute('''SELECT * FROM Locations''')

for eachRow in cursor.fetchall():
    locData=str(eachRow[1])
    try:
        dataJSON=json.loads(locData)
    except:
        continue
    if not('status' in dataJSON and dataJSON['status'] == 'OK'):
        continue

 
