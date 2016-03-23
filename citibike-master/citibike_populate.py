# citibike_populate.py
# Andrew Maner
# Pull data from citibike, create a reference table for all stations, and
# create a table of available bikes keyed on execution time (time of pull)
# insert reference info and insert available bikes
# repeat every 60 seconds for an hour (last part)

import requests
from pandas.io.json import json_normalize
import matplotlib.pyplot as plt
import pandas as pd
import time
import sqlite3 as lite
from dateutil.parser import parse
import collections
import datetime

# download the citibike stations data in json format
r = requests.get('http://www.citibikenyc.com/stations/json')

key_list = [] # unique list of keys for each station listing
for station in r.json()['stationBeanList']:
	for k in station.keys():
		if k not in key_list:
			key_list.append(k)

# use json_normalize to convert to a pandas dataframe
df = json_normalize(r.json()['stationBeanList'])

# Challenge 3.1.3 Answers (commented out for now, but they work as expected)
# how many test stations are there?
# print "Number of test stations: "
# print df['testStation'].count()

# what is the mean number of docks?
# print "Mean number of docks: "
# print df['totalDocks'].mean()

# what is the median number of docks?
# print "Median number of docks: "
# print df['totalDocks'].median()

# what is the mean number of active docks?
# print "Mean number of active docks: "
# print df[df['statusValue'] == 'In Service']['totalDocks'].mean()

# what is the median number of active docks?
# print "Median number of active docks: "
# print df[df['statusValue'] == 'In Service']['totalDocks'].median()

# create and connect to the database
con = lite.connect('citi_bike.db')
cur = con.cursor()

# create table
with con:
	cur.execute('CREATE TABLE IF NOT EXISTS citibike_reference (id INT PRIMARY KEY, totalDocks INT, city TEXT, altitude INT, stAddress2 TEXT, longitude NUMERIC, postalCode TEXT, testStation TEXT, stAddress1 TEXT, stationName TEXT, landMark TEXT, latitude NUMERIC, location TEXT )')

#a prepared SQL statement we're going to execute over and over again
sql = "INSERT INTO citibike_reference (id, totalDocks, city, altitude, stAddress2, longitude, postalCode, testStation, stAddress1, stationName, landMark, latitude, location) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

#for loop to populate values in the database
with con:
	for station in r.json()['stationBeanList']:
		cur.execute(sql,(station['id'],station['totalDocks'],station['city'],station['altitude'],station['stAddress2'],station['longitude'],station['postalCode'],station['testStation'],station['stAddress1'],station['stationName'],station['landMark'],station['latitude'],station['location']))

# extract the column from the DataFrame and put them into a list
station_ids = df['id'].tolist()
# add the '_' to the station name and also add the data type for SQLite
station_ids = ['_' + str(x) + ' INT' for x in station_ids]

# create the table
# in this case, we're concatentating the string and joining all the station ids (now with '_' and 'INT' added)
with con:
	cur.execute("CREATE TABLE IF NOT EXISTS available_bikes ( execution_time INT, " +  ", ".join(station_ids) + ");")

# take the string and parse it into a Python datetime object
exec_time = parse(r.json()['executionTime'])

# create an entry for execution time by inserting it into the database
with con:
	cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', ((exec_time-datetime.datetime(1970,1,1)).total_seconds(),))

# iterate through the stations in the stationBeanList
id_bikes = collections.defaultdict(int) # defaultdict to store available bikes by station

# loop through the stations in the list
for station in r.json()['stationBeanList']:
	id_bikes[station['id']] = station['availableBikes']

# iterate through the defaultdict to update the values in the database
with con:
	for k, v in id_bikes.iteritems():
		cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + str((exec_time-datetime.datetime(1970,1,1)).total_seconds()) + ";")

# test to make sure everything worked
# with con:
# 	 cur = con.cursor()
#	 cur.execute("SELECT * FROM available_bikes")
#	 rows = cur.fetchall()
#	 cols = [desc[0] for desc in cur.description]
#	 df2 = pd.DataFrame(rows,columns=cols)
#	 print df2

# ok, everything worked the first time
# now let's repeat the pull and populate steps for an hour
for i in range(60):
	r = requests.get('http://www.citibikenyc.com/stations/json')
	exec_time = parse(r.json()['executionTime'])

	cur.execute('INSERT INTO available_bikes (execution_time) VALUES (?)', ((exec_time-datetime.datetime(1970,1,1)).total_seconds(),))
	con.commit()

	id_bikes = collections.defaultdict(int)
	for station in r.json()['stationBeanList']:
		id_bikes[station['id']] = station['availableBikes']

	for k, v in id_bikes.iteritems():
		cur.execute("UPDATE available_bikes SET _" + str(k) + " = " + str(v) + " WHERE execution_time = " + str((exec_time-datetime.datetime(1970,1,1)).total_seconds()) + ";")
	con.commit()

	time.sleep(60)
con.close()