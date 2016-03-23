# time_series.py
# Andrew Maner

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.graphics.tsaplots as st

df = pd.read_csv('LoanStats3b.csv',header=1,low_memory=False)
df.dropna(inplace=True)

# covert string to datetime object in pandas
df['issue_d_format'] = pd.to_datetime(df['issue_d'])
# df time series
dfts = df.set_index('issue_d_format')
# year month summary
yms = dfts.groupby(lambda x : x.year*100 + x.month).count()
# loan count summary
lcs = yms['issue_d']

# create an index for the months
# the large numerical spacing between 201212 and 201301 was creating strange
# artifacts in the plot.  this works better
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
# make the plot
plt.plot(x,np.asarray(lcs),linewidth=1.0)
plt.show()
plt.clf()
# there's a definite linear, increasing trend... 
# let's first try diffs
lcs_d1 = lcs.diff()
plt.plot(x,np.asarray(lcs_d1),linewidth=1.0)
plt.show()
# trend is gone
# we could have used the signal package like this (with same result):
# import scipy.signal as sig
# lcs_dt = sig.detrend(lcs)
# plt.plot(x,lcs_dt,linewidth=2.0)
# plt.show()

# now plot the ACF of the transformed series
plt.figure()
st.plot_acf(lcs_d1)
plt.show()
plt.clf()

# and PACF
plt.figure()
st.plot_pacf(lcs_d1)
plt.show()
plt.clf()

print "no autocorrelated structures"