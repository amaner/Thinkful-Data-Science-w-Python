# cap_explore.py

# Imports
import matplotlib.pyplot as plt
import pandas as pd
import random

# Data Load
# it's 5000 rows X 22 columns
# first 21 columns are wave features, and 22nd is the class
df = pd.read_csv("waveform.data", header=None)
# let's give the columns some sensible names
# "fn" for feature n, and "class" for, well, class
colnames = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18','f19','f20','f21','class']
df.columns = colnames

# Exploration
#
# let's start off by plotting a couple waveforms (x-axis) to get an idea
# of how they look
# indices for the x-axis
x = range(1,22)
# set the seed
random.seed(0)
# random integer row indices
xind1 = random.randint(0,4999)
xind2 = random.randint(0,4999)
# let's see what class these are
print "xind1: " + str(xind1) + ", class: " + str(df.loc[xind1, 'class'])
print "xind2: " + str(xind2) + ", class: " + str(df.loc[xind2, 'class'])
plt.figure()
plt.scatter(x, df.loc[xind1, colnames[0:21]], c='r')
plt.scatter(x, df.loc[xind2, colnames[0:21]], c='b')
plt.xlabel('X')
plt.ylabel('Y')
fig_title = "wave " + str(xind1) + " & wave " + str(xind2)
plt.title(fig_title)
plt.savefig('two_random_waveforms_1.png')
plt.clf()
# got two forms of class 2, distinct similarities
xind1 = random.randint(0,4999)
xind2 = random.randint(0,4999)
print "xind1: " + str(xind1) + ", class: " + str(df.loc[xind1, 'class'])
print "xind2: " + str(xind2) + ", class: " + str(df.loc[xind2, 'class'])
plt.figure()
plt.scatter(x, df.loc[xind1, colnames[0:21]], c='r')
plt.scatter(x, df.loc[xind2, colnames[0:21]], c='b')
plt.xlabel('X')
plt.ylabel('Y')
fig_title = "wave " + str(xind1) + " & wave " + str(xind2)
plt.title(fig_title)
plt.savefig('two_random_waveforms_2.png')
plt.clf()
# got two forms of class 0, again distinct similarities
xind1 = random.randint(0,4999)
xind2 = random.randint(0,4999)
print "xind1: " + str(xind1) + ", class: " + str(df.loc[xind1, 'class'])
print "xind2: " + str(xind2) + ", class: " + str(df.loc[xind2, 'class'])
plt.figure()
plt.scatter(x, df.loc[xind1, colnames[0:21]], c='r')
plt.scatter(x, df.loc[xind2, colnames[0:21]], c='b')
plt.xlabel('X')
plt.ylabel('Y')
fig_title = "wave " + str(xind1) + " & wave " + str(xind2)
plt.title(fig_title)
plt.savefig('two_random_waveforms_3.png')
plt.clf()
# got forms of class 0 and 1, some similarities, but many clear differences
# (would reinforce in some spots, but would nearly cancel in others)
xind1 = random.randint(0,4999)
xind2 = random.randint(0,4999)
print "xind1: " + str(xind1) + ", class: " + str(df.loc[xind1, 'class'])
print "xind2: " + str(xind2) + ", class: " + str(df.loc[xind2, 'class'])
plt.figure()
plt.scatter(x, df.loc[xind1, colnames[0:21]], c='r')
plt.scatter(x, df.loc[xind2, colnames[0:21]], c='b')
plt.xlabel('X')
plt.ylabel('Y')
fig_title = "wave " + str(xind1) + " & wave " + str(xind2)
plt.title(fig_title)
plt.savefig('two_random_waveforms_4.png')
plt.clf()
# got forms of class 0 and 2, very different - would almost cancel each other
xind1 = random.randint(0,4999)
xind2 = random.randint(0,4999)
print "xind1: " + str(xind1) + ", class: " + str(df.loc[xind1, 'class'])
print "xind2: " + str(xind2) + ", class: " + str(df.loc[xind2, 'class'])
plt.figure()
plt.scatter(x, df.loc[xind1, colnames[0:21]], c='r')
plt.scatter(x, df.loc[xind2, colnames[0:21]], c='b')
plt.xlabel('X')
plt.ylabel('Y')
fig_title = "wave " + str(xind1) + " & wave " + str(xind2)
plt.title(fig_title)
plt.savefig('two_random_waveforms_5.png')
plt.clf()
# got forms of class 1 and 2, some similarities, but many distinct differences
# (would reinforce in some spots, but cancel in several others)

# OK, so we've plotted a few waveforms, and seen that forms of different classes
# have distinct features while having some similarities.  Interesting...
# Let's look at plotting a few features against each other...

yind1 = random.randint(1,21)
yind2 = random.randint(1,21)
print "feature1= f" + str(yind1)
print "feature2= f" + str(yind2)
plt.figure()
plt.scatter(df.loc[:, "f"+str(yind1)],df.loc[:, "f"+str(yind2)], c='rg')
plt.xlabel('f' + str(yind1))
plt.ylabel('f' + str(yind2))
plt.title('f' + str(yind1) + ' vs f' + str(yind2))
plt.savefig('features_1.png')
plt.clf()
# got features 11 and 20 - tightly balled together - not correlated
yind1 = random.randint(1,21)
yind2 = random.randint(1,21)
print "feature1= f" + str(yind1)
print "feature2= f" + str(yind2)
plt.figure()
plt.scatter(df.loc[:, "f"+str(yind1)],df.loc[:, "f"+str(yind2)], c='rg')
plt.xlabel('f' + str(yind1))
plt.ylabel('f' + str(yind2))
plt.title('f' + str(yind1) + ' vs f' + str(yind2))
plt.savefig('features_2.png')
plt.clf()
# got features 6 and 16 - seem to be quadratically correlated
yind1 = random.randint(1,21)
yind2 = random.randint(1,21)
print "feature1= f" + str(yind1)
print "feature2= f" + str(yind2)
plt.figure()
plt.scatter(df.loc[:, "f"+str(yind1)],df.loc[:, "f"+str(yind2)], c='rg')
plt.xlabel('f' + str(yind1))
plt.ylabel('f' + str(yind2))
plt.title('f' + str(yind1) + ' vs f' + str(yind2))
plt.savefig('features_3.png')
plt.clf()
# got features 6 and 13 - seem to be linearally correlated
# one more time
yind1 = random.randint(1,21)
yind2 = random.randint(1,21)
print "feature1= f" + str(yind1)
print "feature2= f" + str(yind2)
plt.figure()
plt.scatter(df.loc[:, "f"+str(yind1)],df.loc[:, "f"+str(yind2)], c='rg')
plt.xlabel('f' + str(yind1))
plt.ylabel('f' + str(yind2))
plt.title('f' + str(yind1) + ' vs f' + str(yind2))
plt.savefig('features_4.png')
plt.clf()
# got features 20 and 21 - tightly balled

# OK, so we see that some features are correlated (strongly, perhaps?) and might be
# redundant, while others aren't at all correlated.  Also interesting...
# print out the correlation matrix
print "Correlation matrix: "
print df.corr()
# features 4, 5, 6 7, 11, 12, 13 are correlated (> 0.4) with the class data...
# It might be wise to use the least correlated features when classifying.
# Let's look at this in a heat map:
R = df.corr()
from pylab import pcolor, show, colorbar, xticks, yticks
from numpy import arange
pcolor(R)
colorbar()
yticks(arange(0.5,22.5),range(0,22))
xticks(arange(0.5,22.5),range(0,22))
show()