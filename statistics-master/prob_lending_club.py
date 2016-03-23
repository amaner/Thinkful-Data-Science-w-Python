# prob_lending_club.py
# Andrew Maner
# data source: https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv
# reads in data from the lending club, cleans it, and loads it into
# a pandas dataframe
# generates and saves a boxplot, a histogram, and a qq-plot for 
# the values in the "Amount.Requested" column
# for challenge 2.2.2 in Thinkful's data science with python course

import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

# read in the data
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

# clean out rows containing NAs
loansData.dropna(inplace=True)

# generate and save a boxplot for the "Amount.Requested" column
loansData.boxplot(column='Amount.Requested')
plt.savefig("lend_club_boxplot.png")
plt.clf()
# the output reveals a right-skewed distribution, with these properties:
# median amt requested = $10k, Q1 = $6k, and Q3 = $17k (IQR=$11k)
# so 50% of users request between $6k and $17k

# generate and save a histogram for the "Amount.Requested" column
loansData.hist(column='Amount.Requested')
plt.savefig("lend_club_histogram.png")
plt.clf()
# output again shows a right-skewed distribution (most people request
# relatively "small" amounts)

# generate and save a qq-plot for the "Amount.Requested" column
plt.figure()
graph = stats.probplot(loansData['Amount.Requested'],dist="norm",plot=plt)
plt.savefig("lend_club_qqplot.png")
plt.clf()
# output shows that the lending club "Amount.Requested" data is not
# normal.  this is no surprise, given the results from the boxplot
# and the histogram - we have a right-skewed distribution
