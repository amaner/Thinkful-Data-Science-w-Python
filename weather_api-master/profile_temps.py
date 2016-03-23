# profile_temps.py
# in weather_api
# Andrew Maner
# profile the temps stored in the weather_api database

import sqlite3 as lite
import pandas as pd

con = lite.connect('weather_api.db')
with con:
	cur = con.cursor()
	cur.execute("SELECT * FROM temp")
	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows, columns=cols)
	
	# ranges
	print "The range of temps in Atlanta: ", df['Atlanta'].max() - df['Atlanta'].min()
	print "The range of temps in Denver: ", df['Denver'].max() - df['Denver'].min()
	print "The range of temps in Miami: ", df['Miami'].max() - df['Miami'].min()
	print "The range of temps in Nashville: ", df['Nashville'].max() - df['Nashville'].min()
	print "The range of temps in Seattle: ", df['Seattle'].max() - df['Seattle'].min()
	print "\n"
	# means
	print "The mean temp for Atlanta: ", df['Atlanta'].mean()
	print "The mean temp for Denver: ", df['Denver'].mean()
	print "The mean temp for Miami: ", df['Miami'].mean()
	print "The mean temp for Nashville: ", df['Nashville'].mean()
	print "The mean temp for Seattle: ", df['Seattle'].mean()
	print "\n"
	# variances
	print "The temp variance for Atlanta: ", df['Atlanta'].var()
	print "The temp variance for Denver: ", df['Denver'].var()
	print "The temp variance for Miami: ", df['Miami'].var()
	print "The temp variance for Nashville: ", df['Nashville'].var()
	print "The temp variance for Seattle: ", df['Seattle'].var()
	# largest temp change
	print "\n"
	print "Denver had the largest temperature change over the time period.  This is not surprising,"
	print "as Denver is drier than the other cities, and thus will experience larger temperature swings."
	print "In addition, Denver is nearer the center of the country, and thus does not have the"
	print "benefit of having a large body of water serve as a temperature swing mitigator."