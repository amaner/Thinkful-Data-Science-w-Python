# cap_NB.py
# Naive Bayes

import pandas as pd
import timeit
from sklearn.naive_bayes import GaussianNB
import sklearn.cross_validation as skcv

df = pd.read_csv('waveform.data', header=None)
colnames = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18','f19','f20','f21','class']
df.columns = colnames


# Naive Bayes w/ all features
print "Running Naive Bayes w/ all features: "
X = df[colnames[0:21]]
y = df['class']
xtrain, xtest, ytrain, ytest = skcv.train_test_split(X, y, test_size=0.33, random_state=0)
start_time = timeit.default_timer()
gnb = GaussianNB()
ypred = gnb.fit(xtrain, ytrain).predict(xtest)
diff = ypred - ytest
count = 0 
for i in range(len(diff)):
	if diff[i] == 0:
		count = count + 1

acc1 = float(count)/float(len(diff)) * 100
elapsed = timeit.default_timer() - start_time
print "elapsed time: " + str(round(elapsed, 2)) + "s"
print "Accuracy: " + str(round(acc1, 1)) + "%"
# 82.1%
# time: 0.0s

# NB w/ top 10 features
print "Running Naive Bayes with top 10 features from KMeans: "
best10 = ['f11', 'f7', 'f15', 'f6', 'f12', 'f10', 'f13', 'f5', 'f9', 'f16']
X = df[best10]
y = df['class']
xtrain, xtest, ytrain, ytest = skcv.train_test_split(X, y, test_size=0.33, random_state=0)
start_time = timeit.default_timer()
gnb = GaussianNB()
ypred = gnb.fit(xtrain, ytrain).predict(xtest)
diff = ypred - ytest
count = 0 
for i in range(len(diff)):
	if diff[i] == 0:
		count = count + 1

acc2 = float(count)/float(len(diff)) * 100
elapsed = timeit.default_timer() - start_time
print "elapsed time: " + str(round(elapsed, 2)) + "s"
print "Accuracy: " + str(round(acc2, 1)) + "%"
# 82.6% - probably due to correlations of features with outcomes
# time: 0.0s

# NB w/ least correlated features
print "Running Naive Bayes with least correlated features: "
worst = ['f1', 'f9', 'f17', 'f18', 'f19', 'f20', 'f21']
X = df[worst]
y = df['class']
xtrain, xtest, ytrain, ytest = skcv.train_test_split(X, y, test_size=0.33, random_state=0)
start_time = timeit.default_timer()
gnb = GaussianNB()
ypred = gnb.fit(xtrain, ytrain).predict(xtest)
diff = ypred - ytest
count = 0 
for i in range(len(diff)):
	if diff[i] == 0:
		count = count + 1

acc3 = float(count)/float(len(diff)) * 100
elapsed = timeit.default_timer() - start_time
print "elapsed time: " + str(round(elapsed, 2)) + "s"
print "Accuracy: " + str(round(acc3, 1)) + "%"
# 57.6%
# time: 0.0s