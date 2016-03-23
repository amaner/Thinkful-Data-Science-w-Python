# kmeans2.py
# Andrew Maner
# Using the k (3) we selected with kmeans1.py, we cluster the UN
# dataset and plot all possible relationships between GDPperCapita
# and the other variables.  Plots are color-coded to illustrate
# clustering.

import pandas as pd
import scipy.cluster.vq as scv
import numpy as np
import matplotlib.pyplot as plt

# read in the UN data
df = pd.read_csv( 'un.csv' )
colnames = [ 'lifeMale','lifeFemale','infantMortality','GDPperCapita' ]
# subset by our relevant columns
df2 = pd.DataFrame( df[ colnames ] )
# drop nas in place
df2.dropna(inplace=True)
# GDP values are MUCH larger than the others, so 
# apply sqrt to these to bring them in line with other columns
# df2['GDPperCapita'] = df2['GDPperCapita'].apply(np.sqrt)
# apply scv.kmeans2 with k = 3 (chosen w/ kmeans1.py)
km2 = scv.kmeans2( df2.values, 3, minit='points' )
# append 'km3' to colnames
colnames.append('km3')
# restructure df2 to account for borked up indexing due to dropna
col1 = df2.lifeMale.tolist()
col1 = pd.Series( [ round(col1[i],1) for i in range(len(col1)) ] )
col2 = df2.lifeFemale.tolist()
col2 = pd.Series( [ round(col2[i],1) for i in range(len(col2)) ] )
col3 = df2.infantMortality.tolist()
col3 = pd.Series( [ round(col3[i],1) for i in range(len(col3)) ] )
col4 = df2.GDPperCapita.tolist()
col4 = pd.Series( [ round(col4[i],1) for i in range(len(col4)) ] )
col5 = km2[1].tolist()
col5 = pd.Series( [ int(col5[i]) for i in range(len(col5)) ] )
# concat these columns into df2
df2 = pd.concat([col1,col2,col3,col4,col5], axis=1)
df2.columns = colnames

# now let's see how our clustering did...

# first, GDPperCapita vs infantMortality
plt.figure()
plt.scatter( df2['GDPperCapita'], df2['infantMortality'], c=df2['km3'], cmap=plt.cm.Paired)
plt.xlabel('Per Capita GDP (sqrt(USD))')
plt.ylabel('Infant Mortality (per 1000)')
plt.show()
plt.clf()
# the clustering looks sensible
# 1st cluster: countries with medium to high infant mortalities and low GDP - poorly developed countries?
# 2nd cluster: countries with low to medium infant mortalities and low to medium GDPs- developing countries?
# 3rd cluster: countries with low infant mortalities and medium to high GDPs - most developed countries?

# second, GDPperCapita vs lifeMale
plt.figure()
plt.scatter( df2['GDPperCapita'], df2['lifeMale'], c=df2['km3'], cmap=plt.cm.Paired)
plt.xlabel('Per Capita GDP (sqrt(USD))')
plt.ylabel('Male Life Expectancy (yrs)')
plt.show()
plt.clf()
# again, clustering looks sensible
# 1st cluster: countries with low male life expectancies and low GDPs - poorly developed countries?
# 2nd cluster: countries with medium life expectancies and low to medium GDPs - developing countries?
# 3rd cluster: countries with high life expectancies and higher GDPs - most developed countries?

# and finally, GDPperCapita vs lifeFemale
plt.figure()
plt.scatter( df2['GDPperCapita'], df2['lifeFemale'], c=df2['km3'], cmap=plt.cm.Paired )
plt.xlabel('Per Capita GDP (sqrt(USD))')
plt.ylabel('Female Life Expectancy (yrs)')
plt.show()
plt.clf()
# same results as in the GDP vs male life case
