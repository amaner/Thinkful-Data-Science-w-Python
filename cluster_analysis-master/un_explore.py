# un_explore.py

import pandas as pd
import scipy.cluster.vq as scv

df = pd.read_csv("un.csv")

# columns?
print 'Column names: ', df.columns.values

# rows and number of countries?
print len(df['country'])
# 207

# number of non-null values in each column?
col_list = list(df.columns.values)
for x in col_list:
	test = df[x].notnull()
	print 'Col ' + x + ' non-null count:', len(test[test==True])
# of the columns of interest (not country or region), lifeMale, lifeFemale, infantMortality, and GDPperCapita
# seem the best to try to cluster on

# data type for each column?
print df.dtypes