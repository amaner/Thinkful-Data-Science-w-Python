# gdp_pop.py
# Andrew Maner
# accesses gdp market indicator csv file
# and populates a table in education.db
# with the 1999 - 2010 information therein

# function that converts a string to an integer
# or returns None if empty
def IntegerOrNull(value):
	try:
		return int(float(value))
	except:
		return None

import sqlite3 as lite
import csv
import pandas as pd

con = lite.connect('education.db')
cur = con.cursor()

# create the gdp table
cur.execute('CREATE TABLE IF NOT EXISTS gdp (country TEXT, _1999 INT, _2000 INT, _2001 INT, _2002 INT, _2003 INT, _2004 INT, _2005 INT, _2006 INT, _2007 INT, _2008 INT, _2009 INT, _2010 INT)')
# prepare the gdp data insert statement
sql = "INSERT INTO gdp (country, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)"

with open('ny.gdp.mktp.cd_Indicator_en_csv_v2/ny.gdp.mktp.cd_Indicator_en_csv_v2.csv','rU') as inputFile:
	next(inputFile)
	next(inputFile)
	header = next(inputFile)
	inputReader = csv.reader(inputFile)
	for line in inputReader:
		with con:
			data = {
					'country' : line[0],
					'1999' : IntegerOrNull(line[43]),
					'2000' : IntegerOrNull(line[44]),
					'2001' : IntegerOrNull(line[45]),
					'2002' : IntegerOrNull(line[46]),
					'2003' : IntegerOrNull(line[47]),
					'2004' : IntegerOrNull(line[48]),
					'2005' : IntegerOrNull(line[49]),
					'2006' : IntegerOrNull(line[50]),
					'2007' : IntegerOrNull(line[51]),
					'2008' : IntegerOrNull(line[52]),
					'2009' : IntegerOrNull(line[53]),
					'2010' : IntegerOrNull(line[54])
				}
			cur.execute(sql,(data['country'],data['1999'],data['2000'],data['2001'],data['2002'],data['2003'],data['2004'],data['2005'],data['2006'],data['2007'],data['2008'],data['2009'],data['2010']))
		
# let's see if that worked
#with con:
#	cur = con.cursor()
#	cur.execute("SELECT * FROM gdp")
#	rows = cur.fetchall()
#	cols = [desc[0] for desc in cur.description]
#	df = pd.DataFrame(rows,columns=cols)
#	print df
