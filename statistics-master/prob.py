# prob.py
# Andrew Maner
# submission for challenge 2.2.1 in Thinkful's data science with python course
# outputs frequencies, creates and saves a boxplot, creates and
# saves a histogram, and creates and saves a qq-plot for some given data
# - purpose is to demonstrate ability to utilize these basic
# features of matplotlib.pyplot

import collections
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# make a simple discrete data set
x = [1,1,1,1,1,1,1,1,2,2,2,3,4,4,4,4,5,6,6,6,7,7,7,7,7,7,7,7,8,8,9,9]

# calculate and output the frequencies of elements in this list
c = collections.Counter(x)
count_sum = sum(c.values())
for k,v in c.iteritems():
	print "The frequency of number " + str(k) + " is " + str(float(v)/count_sum)

# create and save a boxplot of the data
plt.boxplot(x)
plt.savefig("boxplot.png")
plt.clf()

# create and save a histogram of the data
plt.hist(x, histtype='bar')
plt.savefig("histogram.png")
plt.clf()

# create and save a qq-plot of the data
plt.figure()
graph = stats.probplot(x, dist="norm", plot=plt)
plt.savefig("qqplot.png")
