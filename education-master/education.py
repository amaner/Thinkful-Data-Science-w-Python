# education.py
# Andrew Maner

import sqlite3 as lite
import pandas as pd
import numpy as np
import statsmodels.api as sm
from scipy import stats
import matplotlib.pyplot as plt

# connect to education.db (populated by edu_pop.py and gdp_pop.py)
con = lite.connect('education.db')

# grab the data we need:
# we'll use ave_yrs from edu_life, and _1999 - _2010 in gdp_pop
# some country names don't match up, so we'll do an inner join
df = pd.read_sql_query("SELECT ave_yrs, _1999, _2000, _2001, _2002, _2003, _2004, _2005, _2006, _2007, _2008, _2009, _2010 FROM edu_life INNER JOIN gdp WHERE name=country",con)
# some rows contain all NaN (or mostly NaN), so get rid of these
df = df.dropna()

# separate the ave_yrs and gdp data so we can average gdp data across columns
edu = df['ave_yrs']
gdp = df[['_1999','_2000','_2001','_2002','_2003','_2004','_2005','_2006','_2007','_2008','_2009','_2010']]
gdp = gdp.mean(axis=1)

# build the OLS model
y = np.matrix(edu.astype(float)).transpose()
x = np.matrix(gdp.astype(float)).transpose()
# take the log of the x variable, because its scale is so ridiculous compared to that of y 
x = np.log(x)

# correlation
corr = stats.pearsonr(y,x)
print corr
# corr = 0.45 => somewhat correlated

# add a constant to x for OLS
X = sm.add_constant(x)
# make the model
model = sm.OLS(y,X)
f = model.fit()

print f.summary()
# r-squared = 0.204 => only 20% of variation in edu_life is described by log(mean(gdp))
# slope = 0.592 w/ p-value of 0.000 => significant
# so, there is some relationship between the two.  not terribly strong, but it is there.
# scatter plot also shows an increasing linear trend

