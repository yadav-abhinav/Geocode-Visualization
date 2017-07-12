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

    latitude=dataJSON["results"][0]["geometry"]["location"]["lat"]
    longitude=dataJSON["results"][0]["geometry"]["location"]["lng"]
    location=dataJSON["results"][0]["formatted_address"]

    try:
        op="["+str(latitude)+","+str(longitude)+",'"+str(location)+"'],"+'\n'
        fHandle.write(op)
    except:
        print "ERROR IN STORING DATA IN where.js"
        continue
fHandle.write("];\n")
fHandle.close()
cursor.close()
