# cap_KNN.py

import pandas as pd
import sklearn.cross_validation as skcv
from sklearn import neighbors
from sklearn.ensemble import BaggingClassifier
import math
import timeit

df = pd.read_csv('waveform.data', header=None)
colnames = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18','f19','f20','f21','class']
df.columns = colnames
# colnames from feature extraction
best10 = ['f11', 'f7', 'f15', 'f6', 'f12', 'f10', 'f13', 'f5', 'f9', 'f16']
# the reduced data set
reduced = df[best10]
# split
X = reduced
y = df['class']
xtrain, xtest, ytrain, ytest = skcv.train_test_split(X, y, test_size=0.33, random_state=0)
# state the split sizes
print "Xtrain: ", len(xtrain) # 3350
print "Xtest: ", len(xtest) # 1650
# define k to be the square root of the number of train instances
k = int(math.sqrt(len(xtrain))) # per Duda et al
print "Using k = ", k  # 57

# KNN with k = sqrt(n) and 10 features
print "Running KNN w/ 57 neighbors and the 10 features found earlier: "
start_time = timeit.default_timer()
neigh = neighbors.KNeighborsClassifier(n_neighbors=k)
ypred = neigh.fit(xtrain, ytrain).predict(xtest)
diff = ypred - ytest
count = 0 
for i in range(len(diff)):
	if diff[i] == 0:
		count = count + 1

acc1 = float(count)/float(len(diff)) * 100
elapsed = timeit.default_timer() - start_time
print "elapsed time: " + str(round(elapsed, 2)) + "s"
print "Accuracy with 10 features: " + str(round(acc1, 1)) + "%"
# 85.3%, but probably down to correlation w/ class data
# time: 0.2s

# KNN with k = sqrt(n) and all (21) features
print "Running KNN w/ 57 neighbors and all features, for comparison: "
X = df[colnames[0:21]]
y = df['class']
xtrain, xtest, ytrain, ytest = skcv.train_test_split(X, y, test_size=0.33, random_state=0)
start_time = timeit.default_timer()
neigh = neighbors.KNeighborsClassifier(n_neighbors=k)
ypred = neigh.fit(xtrain, ytrain).predict(xtest)
diff = ypred - ytest
count = 0
for i in range(len(diff)):
	if diff[i] == 0:
		count = count + 1

acc2 = float(count)/float(len(diff)) * 100
elapsed = timeit.default_timer() - start_time
print "elapsed time: " + str(round(elapsed, 2)) + "s"
print "Accuracy with all features: " + str(round(acc2, 1)) + "%"
# 86.0% - still have the correlated features, so...
# time: 0.41s
print "Improvement using all features, vs top 10: " + str(round((acc2 - acc1)/acc1 * 100, 1)) + "%"
# 0.9% 

# KNN with 57 neighbors and only 6 features
print "Running KNN w/ 57 neighbors and the top 6 features: "
best6 = ['f11', 'f7', 'f15', 'f6', 'f12', 'f10']
reduced = df[best6]
X = reduced
y = df['class']
xtrain, xtest, ytrain, ytest = skcv.train_test_split(X, y, test_size=0.33, random_state=0)
start_time = timeit.default_timer()
neigh = neighbors.KNeighborsClassifier(n_neighbors=k)
ypred = neigh.fit(xtrain, ytrain).predict(xtest)
diff = ypred - ytest
count = 0
for i in range(len(diff)):
	if diff[i] == 0:
		count = count + 1

acc3 = float(count)/float(len(diff)) * 100
elapsed = timeit.default_timer() - start_time
print "elapsed time: " + str(round(elapsed, 2)) + "s"
print "Accuracy with top 6 features: " + str(round(acc3, 1)) + "%"
# 80.3% - still likely down to correlation
# time: 0.12s
print "Improvement using all features, vs top 6: " + str(round((acc2 - acc3)/acc3 * 100, 1)) + "%"
# 7.1%

# bagging experiment
print "Running bagging meta-estimator w/ KNN w/ 57 neighbors and 10 max features: "
bagging = BaggingClassifier(neighbors.KNeighborsClassifier(n_neighbors=k), max_samples=0.5, max_features=10)
X = df[colnames[0:21]]
y = df['class']
xtrain, xtest, ytrain, ytest = skcv.train_test_split(X, y, test_size=0.33, random_state=0)
start_time = timeit.default_timer()
ypred = bagging.fit(xtrain, ytrain).predict(xtest)
diff = ypred - ytest
count = 0

for i in range(len(diff)):
	if diff[i] == 0:
		count = count + 1

acc4 = float(count)/float(len(diff)) * 100
elapsed = timeit.default_timer() - start_time
print "elapsed time: " + str(round(elapsed, 2)) + "s"
print "Accuracy with bagging and 10 features max: " + str(round(acc4, 1)) + "%"
# 85.2 % - quite good, but which features were chosen?
# time: 1.22s

# Run with the columns most poorly correlated with the class column
print "Running KNN w/ 57 neighbors and the features most poorly correlated with the class data: "
worst = ['f1', 'f9', 'f17', 'f18', 'f19', 'f20', 'f21']
X = df[worst]
y = df['class']
start_time = timeit.default_timer()
neigh = neighbors.KNeighborsClassifier(n_neighbors=k)
ypred = neigh.fit(xtrain, ytrain).predict(xtest)
diff = ypred - ytest
count = 0
for i in range(len(diff)):
	if diff[i] == 0:
		count = count + 1

acc5 = float(count)/float(len(diff)) * 100
elapsed = timeit.default_timer() - start_time
print "elapsed time: " + str(round(elapsed, 2)) + "s"
print "Accuracy with 7 least correlated features: " + str(round(acc5, 1)) + "%"
# 86.0% - quite good, considering even all features result in underfitting
# time: 0.42s
print "Difference with results using all features: " + str(round((acc2 - acc5)/acc5 * 100, 1)) + "%"
# 0% 