# edu_pop.py
# Andrew Maner
# Thinkful Data Science With Python 3.3

# we're going to use scraperwiki instead of beautiful soup, just cuz...
import scraperwiki as SW
# and lxml is a good html scraping library
import lxml.html as LH
# we'll use sqlite for the edu db
import sqlite3 as lite
# and pandas for data frames
import pandas as pd

# create the edu db
con = lite.connect('education.db')
cur = con.cursor()
with con:
	cur.execute('CREATE TABLE IF NOT EXISTS edu_life (name TEXT, year INT, ave_yrs INT, male_yrs INT, female_yrs INT)')
# a prepared sql statement to use when inserting data later on
sql = "INSERT INTO edu_life (name, year, ave_yrs, male_yrs, female_yrs) VALUES(?,?,?,?,?)"

# the un education data site
url = "http://web.archive.org/web/20110514112442/http://unstats.un.org/unsd/demographic/products/socind/education.htm"

# scraperwiki srape of the site will be the site as a string
results = SW.scrape(url)

# use lxml.html to pull the pure html
root = LH.fromstring(results)

# loop across all table rows in the site
# using cssselect (from lxml.html)
for tr in root.cssselect("div[align='left'] tr"):
	# select all table data elements from the row
	tds = tr.cssselect("td")
	# if we have the right number (12) of them, then
	# we're in the country table
	if len(tds)==12:
		# country index = 0, year of study index = 1,
		# average (of males & females) yrs in school index = 4,
		# male yrs in school index = 7, and
		# female yrs in school index = 10
		# create a dictionary for the country - not a neccesary step
		data = {
			'name' : tds[0].text_content(),
			'year' : int(tds[1].text_content()),
			'ave_yrs' : int(tds[4].text_content()),
			'male_yrs' : int(tds[7].text_content()),
			'female_yrs' : int(tds[10].text_content())
		}
		with con:
			cur.execute(sql,(data['name'],data['year'],data['ave_yrs'],data['male_yrs'],data['female_yrs']))
