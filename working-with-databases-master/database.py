# database.py
# Andrew Maner
# connect to getting_started.db, create cities and weather
# tables (drop if they already exist), populate these tables,
# join the data together, load into a pandas dataframe,
# print out the cities having July as the warmest month in a 
# complete sentence
# need to spend more time figuring out pandas and formatting...
# will work on it this weekend

import sqlite3 as lite
import pandas as pd

# build cities and weather tuples for use in population
cities = (('New York City','NY'),('Boston','MA'),
	('Chicago','IL'),('Miami','FL'),('Dallas','TX'),
	('Seattle','WA'),('Portland','OR'),('San Francisco','CA'),
	('Los Angeles','CA'),('Washington','DC'),('Houston','TX'),
	('Las Vegas','NV'),('Atlanta','GA'))

weather = (('New York City',2013,'July','January',62),
	('Boston',2013,'July','January',59),
	('Chicago',2013,'July','January',59),
	('Miami',2013,'August','January',84),
	('Dallas',2013,'July','January',77),
	('Seattle',2013,'July','January',61),
	('Portland',2013,'July','December',63),
	('San Francisco',2013,'September','December',64),
	('Los Angeles',2013,'September','December',75),
	('Washington',2013,'July','January',67),
	('Houston',2013,'July','January',80),
	('Las Vegas',2013,'July','December',80),
	('Atlanta',2013,'July','January',72))

# form the connection
con = lite.connect('getting_started.db')

with con:
	# get a cursor object from con
	cur = con.cursor()
	# drop the cities and weather tables if they exist
	cur.execute("DROP TABLE IF EXISTS cities")
	cur.execute("DROP TABLE IF EXISTS weather")
	# create the cities and weather tables
	cur.execute("CREATE TABLE cities(name text, state text)")
	cur.execute("CREATE TABLE weather(city text, year integer, warm_month text, cold_month text, average_high integer)")
	# insert the cities tuple data into the cities table
	cur.executemany("INSERT INTO cities VALUES(?,?)",cities)
	# insert the weather tuple data into the weather table
	cur.executemany("INSERT INTO weather VALUES(?,?,?,?,?)",weather)
	# pull and join the data from cities and weather
	# get only those cities with warmest month = July
	cur.execute("SELECT name, state FROM weather INNER JOIN cities ON city=name WHERE warm_month='July'")
	rows = cur.fetchall()
	# put this into a data frame
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows,columns=cols)
	# print out the results
	print "The cities that are warmest in July are:"
	print df
	
