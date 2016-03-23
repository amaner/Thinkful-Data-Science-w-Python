# chi_squared.py
# Andrew Maner
# data source: https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv
# reads in data from the lending club, cleans it, and loads it into
# a pandas dataframe
# for challenge 2.2.3 in Thinkful data science with python class

from scipy import stats
import collections
import pandas as pd

# load the data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# drop null rows
loansData.dropna(inplace=True)
# frequencies
freq = collections.Counter(loansData['Open.CREDIT.Lines'])
# establish significance level
alpha = 0.05
chi, p = stats.chisquare(freq.values())
print "chi: " + str(chi)
print "p: " + str(p)
if p < alpha:
	print "Reject the null hypothesis. The results are NOT distributed evenly."
else:
	print "Do not reject the null hypothesis. The results ARE distributed evenly."
