# cap_SVM.py

import pandas as pd
from sklearn import svm
import sklearn.cross_validation as skcv
import timeit

df = pd.read_csv('waveform.data', header=None)
colnames = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18','f19','f20','f21','class']
df.columns = colnames

# Running linear SVC with all features
print "Running linear SVC with all features: "
X = df[colnames[0:21]]
y = df['class']
xtrain, xtest, ytrain, ytest = skcv.train_test_split(X, y, test_size=0.33, random_state=0)
start_time = timeit.default_timer()
supp = svm.SVC(kernel='linear')
ypred = supp.fit(xtrain, ytrain).predict(xtest)
diff = ypred - ytest
count = 0 
for i in range(len(diff)):
	if diff[i] == 0:
		count = count + 1

acc1 = float(count)/float(len(diff)) * 100
elapsed = timeit.default_timer() - start_time
print "elapsed time: " + str(round(elapsed, 2)) + "s"
print "Accuracy: " + str(round(acc1, 1)) + "%"
# 87.2%
# time: 0.48s

# Run with top 10 features from KMeans
print "Running linear SVC with top 10 features: "
best10 = ['f11', 'f7', 'f15', 'f6', 'f12', 'f10', 'f13', 'f5', 'f9', 'f16']
X = df[best10]
y = df['class']
xtrain, xtest, ytrain, ytest = skcv.train_test_split(X, y, test_size=0.33, random_state=0)
start_time = timeit.default_timer()
supp = svm.SVC(kernel='linear')
ypred = supp.fit(xtrain, ytrain).predict(xtest)
diff = ypred - ytest
count = 0 
for i in range(len(diff)):
	if diff[i] == 0:
		count = count + 1

acc2 = float(count)/float(len(diff)) * 100
elapsed = timeit.default_timer() - start_time
print "elapsed time: " + str(round(elapsed, 2)) + "s"
print "Accuracy: " + str(round(acc2, 1)) + "%"
# 85.2% - probably due to correlations between features and outcomes
# 0.3s

# Run with the columns most poorly correlated with the class column
print "Running linear SVC with least correlated features: "
worst = ['f1', 'f9', 'f17', 'f18', 'f19', 'f20', 'f21']
X = df[worst]
y = df['class']
xtrain, xtest, ytrain, ytest = skcv.train_test_split(X, y, test_size=0.33, random_state=0)
start_time = timeit.default_timer()
supp = svm.SVC(kernel='linear')
ypred = supp.fit(xtrain, ytrain).predict(xtest)
diff = ypred - ytest
count = 0 
for i in range(len(diff)):
	if diff[i] == 0:
		count = count + 1

acc3 = float(count)/float(len(diff)) * 100
elapsed = timeit.default_timer() - start_time
print "elapsed time: " + str(round(elapsed, 2)) + "s"
print "Accuracy: " + str(round(acc3, 1)) + "%"
# 56.1%
# 0.6s
