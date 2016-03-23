# stats.py
# Andrew Maner
# Thinkful Lesson 2.1.1 Challenge
# A script that prints the mean, median, mode, range, variance,
# and standard deviation of the alcohol and tobacco datasets, with 
# full text

import pandas as pd
from scipy import stats

data = '''Region, Alcohol, Tobacco
North, 6.47, 4.03
Yorkshire, 6.13, 3.76
Northeast, 6.19, 3.77
East Midlands, 4.89, 3.34
West Midlands, 5.63, 3.47
East Anglia, 4.52, 2.92
Southeast, 5.89, 3.20
Southwest, 4.79, 2.71
Wales, 5.27, 3.53
Scotland, 6.08, 4.51
Northern Ireland, 4.02, 4.56'''

# split the data on newlines
data = data.splitlines()

# now split again on commas
data = [i.split(', ') for i in data]

# convert to a pandas dataframe
column_names = data[0]
data_rows = data[1::]
df = pd.DataFrame(data_rows, columns = column_names)

# convert alcholo and tobacco numbers to float
df['Alcohol'] = df['Alcohol'].astype(float)
df['Tobacco'] = df['Tobacco'].astype(float)

print "Weekly Alcohol Expenditures in Great Britain:"
print "The range of alcohol expenditures is {0:.2f} GBP.".format(max(df['Alcohol'])-min(df['Alcohol']))
print "The mean alcohol expenditure is {0:.2f} GBP.".format(df['Alcohol'].mean())
print "The median alcohol expenditure is {0:.2f} GBP.".format(df['Alcohol'].median())
print "The mode of the alcohol expenditure data set is {} GBP.".format(stats.mode(df['Alcohol'])[0])
print "The variance of the alcohol expenditure data set is {0:.2f}.".format(df['Alcohol'].var())
print "The standard deviation of the alcohol expenditure data set is {0:.2f} GBP.".format(df['Alcohol'].std())
print "\n"
print "Weekly Tobacco Expenditures in Great Britain:"
print "The range of tobacco expenditures is {0:.2f} GBP.".format(max(df['Tobacco'])-min(df['Tobacco']))
print "The mean tobacco expenditure is {0:.2f} GBP.".format(df['Tobacco'].mean())
print "The median tobacco expenditure is {0:.2f} GBP.".format(df['Tobacco'].median())
print "The mode of the tobacco expenditure data set is {} GBP.".format(stats.mode(df['Tobacco'])[0])
print "The variance of the tobacco expenditure data set is {0:.2f}.".format(df['Tobacco'].var())
print "The standard deviation of the tobacco expenditure data set is {0:.2f} GBP.".format(df['Tobacco'].std())
