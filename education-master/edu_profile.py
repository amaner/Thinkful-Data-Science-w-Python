import sqlite3 as lite
import pandas as pd
import matplotlib.pyplot as plt 

con = lite.connect('education.db')
cur = con.cursor()

with con:
	cur = con.cursor()
	cur.execute("SELECT * FROM edu_life")
	rows = cur.fetchall()
	cols = [desc[0] for desc in cur.description]
	df = pd.DataFrame(rows,columns=cols)

print "median age for male data set: ", df['male_yrs'].median()
print "mean age for male data set: ", df['male_yrs'].mean()
print "median age for female data set: ", df['female_yrs'].median()
print "mean age for female data set: ", df['female_yrs'].mean()
print "\n"

df['male_yrs'].hist()
plt.show()
plt.clf()

df['female_yrs'].hist()
plt.show()
plt.clf()

# girls seem to go to school longer - on average - than do boys
# both distributions are roughly symmetric, not revealing any
# significant skew or patterns (other than approximate symmetry)
