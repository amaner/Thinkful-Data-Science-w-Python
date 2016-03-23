# markov.py
# quick run-through of markov probabilities
# market probabilities example
# Thinkful 2.8.1 "Overview of Markov Models"
# transition matrix is labeled as P (standard)
#
# if x0 is the state on the 0-th day, then
# the nth day is xn = x0 * P^n
# example: we start with a bull market x0 = [1 0 0]
# the probabilities n transitions later are [1 0 0]*P^n
# (just the first row of the resulting matrix)


import pandas as pd
import numpy as np

P = pd.DataFrame({'bear':[0.8,0.075,0.25],'bull':[0.15,0.9,0.25],'stagnant':[0.05,0.025,0.5]},index=["bear","bull","stagnant"])
print "The probabilities after 1 transition"
print P
print "\n"

Pt = P
for i in range(2,101):
	Pt = Pt.dot(P)
	if (i == 2 or i == 5 or i == 10 or i == 20 or i == 50 or i == 100):
		print "The probabilities after " + str(i) + " transitions:"
		print Pt
		print "\n"

bear = np.array([1,0,0])
print "The probabilities are converging to:"
print bear.dot(Pt)