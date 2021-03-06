# weather_api.py
# Andrew Maner
# 
# 

import requests
import sqlite3 as lite
import datetime

my_api_key = '7f3925a0ebb862d29f5eac7573dc51d4'
my_api_url = 'https://api.forecast.io/forecast/' + my_api_key
# dictionary of 5 cities with lat/lons
cities = {  "Atlanta": '33.762909,-84.422675',
			"Denver": '39.761850,-104.881105',
			"Miami": '25.775163,-80.208615',
			"Nashville": '36.171800,-86.785002',
			"Seattle": '47.620499,-122.350876' 
		}

# set the time for "now" - the time the code is executed
# this makes the reference time the same for all queries
now = datetime.datetime.now()

# set up the db
con = lite.connect('weather_api.db')
cur = con.cursor()
# set up the tables
with con:
	cur.execute('CREATE TABLE IF NOT EXISTS temp ( day_recorded INT, Atlanta REAL, Denver REAL, Miami REAL, Nashville REAL, Seattle REAL )')

# we go back 30 days, and start iterating daily from there
# day_of_query starts 30 days in the past (from now)
day_of_query = now - datetime.timedelta(days=30)
# fill in the days
with con:
	while day_of_query < now:
		cur.execute("INSERT INTO temp ( day_recorded ) VALUES (?)", (int(day_of_query.strftime('%s')),))
		day_of_query += datetime.timedelta(days=1)

# loop through the cities we've chosen and get data
# using the api
for k,v in cities.iteritems():
	# start the query at 30 days ago for each city
	day_of_query = now - datetime.timedelta(days=30)
	while day_of_query < now:
		# tack onto my_api_url the lat/lon pairs and the query day
		r = requests.get(my_api_url + '/' + v + ',' + day_of_query.strftime('%Y-%m-%dT12:00:00'))
		# set the REAL value for each city to the max temperature on the query day
		with con:
			cur.execute('UPDATE temp SET ' + k + ' = ' + str(r.json()['daily']['data'][0]['temperatureMax']) + ' WHERE day_recorded = ' + day_of_query.strftime('%s'))
		# increment the query date by 1 day
		day_of_query += datetime.timedelta(days=1)
# close the connection to the db
con.close()
