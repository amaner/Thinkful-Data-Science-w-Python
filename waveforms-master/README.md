### Andrew Maner 
### Thinkful Data Science with Python Unit 5 (Capstone)

#### Introduction

Dataset: "Waveform Database Generator (Version 1)"

Downloaded from: [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Waveform+Database+Generator+%28Version+1%29)

Data source (original):  Breiman, L., Friedman, J.H., Olshen, R.A., & Stone, C.J. (1984). *Classification and Regression Trees*. Wadsworth International Group: Belmont, CA (pp. 43-49)

Information:

* 3 classes of waves (0, 1, 2)
* 21 attributes, with noise
* 5000 instances
* Each generated from combination of 2 and 3 "base" waves
* Each with mean 0 variance 1 noise added

Goal: To find most efficient (in terms of features used and processor time) naive method to classify these waveforms, with a reasonable measure of accuracy.

#### Data Exploration (cap_explore.py)

Step 1: Read the data into a 5000 x 22 pandas data frame.  Columns 1-21 contain features (and are labeled "fn", where n is the feature number), and column 22 contains the class ids (and is labeled "class").

Step 2: Set a seed and plot five (5) random combinations of waveforms, to look for commonalities and differences.  (More plots were visualized, but 5 seemed to summarize some important characteristics.)  Example:

```python
 x = range(1,22)
random.seed(0)
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
plt.savefig('two_random_waveforms_1.png')
plt.clf()
```

First pairing - instances 4222 and 3789, both of class 2.  Note the clear similarites, despite the noise.

![alt text](https://github.com/amaner/waveforms/blob/master/two_random_waveforms_1.png)

Second pairing - instances 2102 and 1294, both of class 0.  Note again the clear similarities.

![alt text](https://github.com/amaner/waveforms/blob/master/two_random_waveforms_2.png)

Third pairing - instances 2556 and 2024.  These are from classes 0 and 1, respectively, and have clear differences *and* similarities.  

![alt text](https://github.com/amaner/waveforms/blob/master/two_random_waveforms_3.png)

Fourth pairing - instances 3918 and 1516.  These are from 0 and 2, respectively, and are very much different (would almost cancel).

![alt text](https://github.com/amaner/waveforms/blob/master/two_random_waveforms_4.png)

Fifth pairing - instances 2382 and 2916.  These are from classes 1 and 2, respectively, and have clear differences *and* similarities (as in the third pairing).

![alt text](https://github.com/amaner/waveforms/blob/master/two_random_waveforms_5.png)

This is by no means an exhaustive exploration of how waveforms of different (and equal) classes compare and contrast, but we can see that some class pairings have quite distinct differences, while others are a bit more difficult to tell apart.  In addition, waveforms of the same class are likely to display clear similarities.

Step 3: Plot four (4) random combinations of features, to look for commonalities (correlations) and differences.

Example:

```python
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
```

First pairing - features 11 and 20.  These are tightly balled together, showing little if any correlation.

![alt text](https://github.com/amaner/waveforms/blob/master/features_1.png)

Second pairing - features 6 and 16.  Clear evidence of some correlation here.

![alt text](https://github.com/amaner/waveforms/blob/master/features_2.png)

Third pairing - features 13 and 6.  Again, clear evidence of correlation.

![alt text](https://github.com/amaner/waveforms/blob/master/features_3.png)

Fourth pairing - features 20 and 21.  These are tightly balled together, showing little if any correlation.

![alt text](https://github.com/amaner/waveforms/blob/master/features_4.png)

Step 4: Look for correlations among features and between features and the class variable.

```python
print df.corr()
from pylab import pcolor, show, colorbar, xticks, yticks
from numpy import arange
pcolor(R)
colorbar()
yticks(arange(0.5,22.5),range(0,22))
xticks(arange(0.5,22.5),range(0,22))
show()
```

From this we can see that some distinct patterns.  For example, neighboring features (in terms of index) tend to be positively correlated (e.g. features 5 and 6), while non-neighboring features (in terms of index) tend to be negatively correlated (e.g. features 6 and 14).  In addition, it is apparent that "mid" features (indices 9-15) tend to be positively correlated with class, while "low" features (indices 1-7) tend to be negatively correlated with class.  In addition, some features have practially no correlation with class.  (This will be important.) 

![alt text](https://github.com/amaner/waveforms/blob/master/correlation_heatmap.png)

#### Feature Extraction (cap_rand_forest_extract.py)

A 500 estimator Random Forest classifier was fit to the data and the top 10 importances were used to identify the 10 features considered "most important" by the RFC.  These turned out to be (in decreasing order) f11, f7, f15, f6, f12, f10, f13, f5, f9, and f16.  Most of these are fairly well correlated with the class variable, so they are suspect.  (They will automatically provide good results using most classification algorithms.)  Nevertheless, we will experiment with them, and with the ones least correlated with class (f1, f9, f17, f18, f19, f20, and f21).

#### Classification (several files)

Several standard classification algorithms were tested for accuracy and for speed.  The results are shown by algorithm.  In all cases, the data was split into training and test sets (xtrain, xtest, ytrain, ytest) using the train_test_split function in the sklearn.cross_validation package. 

Data split method:

```python
X = df[ insert the name of a list of relevant feature names (column indices) ]
y = df['class']
xtrain, xtest, ytrain, ytest = sklearn.cross_validation.train_test_split(X, y, test_size=0.33, random_state=0)
```

##### Naive Bayes (cap_NB.py)

In each case, a Gaussian Naive Bayes (NB) classifier (from the sklearn.naive_bayes module) was fit to the training set (which would vary, depending on column names chosen).

Fit method:

```python
gnb = GaussianNB()
ypred = gnb.fit(xtrain, ytrain).predict(xtest)
```

###### All features (1-21)

Using all features (as a sort of baseline) resulted in an accuracy rating of 82.1%, and took 0.0s (using the timeit module).  This should be about as good as it will get, since this is using the full set of features (in particular, the ones that are strongly correlated with class).

###### Top 10 features (as discussed above)

Using the top 10 features resulted in an accuracy of 82.6%, and took the same amount of time (0.0s, according to timeit).  This result is suspect, as is the one above, given the fact that several of the top 10 features are correlated (abs > 0.4) with class.

###### 6 features least correlated with class (as discussed above)

Using the 6 features least correlated with class resulted in an accuracy of 57.6%, and took about 0.0s.  This is very poor relative to the results obtained using all features, but indicates that Naive Bayes is not a good choice of classification algorithm for this data set.

##### KNN (cap_KNN.py)

k-Nearest Neighbors (KNeighborsClassifier, from the sklearn.ensemble module) was run using k=57 (square root of number of instances, per Duda et al), and with a few combinations of features (top 10, all 21, top 6, bagging with 10 features max, and 6 least correlated).

KNN Method:

```python
from sklearn import neighbors
neigh = neighbors.KNeighborsClassifier(n_neighbors=k)
ypred = neigh.fit(xtrain, ytrain).predict(xtest)
```

###### Top 10 features

Using the top 10 features resulted in an accuracy of 85.3%, and took approximately 0.2s.  Again, these results are suspect due to correlation.

###### All 21 features

Using the full set of features resulted in an accuracy of 86.0%, and took approximately 0.41s.  Suspect, again...

###### Top 6 features

Using the top 6 features resulted in an accuracy of 80.3%, and took approximately 0.12s.  It is interesting that we could retain greater than 80% accuracy using only 6 features (11, 7, 15, 6, 12, 10).  Of these, features 6 and 7 are the least correlated with class (but the others are fairly well correlated with class).

###### Bagging experiment with a maximum of 10 features

Chaining the bagging and KNN algorithms, with a maximum of 10 features (the ids of which are unknown), resulted in an accuracy of 85.2% and took approximately 1.22s.  This is remarkably close to the results obtained using all features, and execution time was fairly rapid.  A drawback here is that the ids are not output, so we may have just used some of the highly correlated (with class) features.

Bagging experiment method:

```python
from sklearn.ensemble import BaggingClassifier
bagging = BaggingClassifier(neighbors.KNeighborsClassifier(n_neighbors=k), max_samples=0.5, max_features=10)
X = df[colnames[0:21]]
y = df['class']
xtrain, xtest, ytrain, ytest = skcv.train_test_split(X, y, test_size=0.33, random_state=0)
ypred = bagging.fit(xtrain, ytrain).predict(xtest)
```

######  6 features least correlated with class

Using the "bottom 6" features resulted in a very nice accuracy (relatively speaking) of 86.0%, and took approximately 0.42s.  We can conclude here that KNN matches well with this dataset, provided we do not use feature columns that are well-correlated with the class variable.  

##### SVM (cap_SVM.py)

A linear Support Vector Classifier was fit to the training data, and used to predict outcomes for the test data.

SVM method:

```python
import sklearn.cross_validation as skcv
from sklearn import svm
X = df[insert the name of a list of relevant column names]
y = df['class']
xtrain, xtest, ytrain, ytest = skcv.train_test_split(X, y, test_size=0.33, random_state=0)
supp = svm.SVC(kernel='linear')
ypred = supp.fit(xtrain, ytrain).predict(xtest)
```

The SVC was run against all 21 features, the top 10 features, and the "bottom 6" features, as in the NB case.  The results were almost the same: strong accuracy in the first two cases (likely due to correlation), and poor accuracy in the final case.  Times were reasonably fast (ranging from 0.3s to 0.6s), but we can conclude that SVM is not a good match for this dataset.

##### LDA (cap_LDA.py)

A Linear Discriminant Analysis classifier was fit to the training data, and used to predict the outcomes for the test data.

LDA method:

```python
import sklearn.cross_validation as skcv
from sklearn.lda import LDA
X = df[insert the name of a list of relevant column names]
y = df['class']
xtrain, xtest, ytrain, ytest = skcv.train_test_split(X, y, test_size=0.33, random_state=0)
clf = LDA()
ypred = clf.fit(xtrain, ytrain).predict(xtest)
```

LDA was run against all 21 features, the top 10 features, and the "bottom 6" features, as in the previous case.  The results were almost the same: strong accuracy in the first two cases (likely due to correlation), and poor accuracy in the final case.  Times were extremely fast (about 0.01s), but we can conclude that LDA is not a good match for this dataset.

##### Gradient Boosting (cap_GB.py)

A Gradient Boosting classifier was fit to the training data, and used to predict the outcomes for the test data.

GB method:

```python
import sklearn.cross_validation as skcv
import sklearn.ensemble as ske
X = df[insert the name of a list of relevant column names]
y = df['class']
xtrain, xtest, ytrain, ytest = skcv.train_test_split(X, y, test_size=0.33, random_state=0)
gb = ske.GradientBoostingClassifier(n_estimators=100, random_state=0)
ypred = gb.fit(xtrain, ytrain).predict(xtest)
```

GB was run against all 21 features, the top 10 features, and the "bottom 6" features, as in the previous case.  The results were almost the same: strong accuracy in the first two cases (likely due to correlation), and poor accuracy in the final case.  Times were very slow (ranging from 1.12s in the final case, to 2.82s in the first case), and we can conclude that GB is not a good match for this dataset.

##### Additional Classifiers

Stochastic Gradient Descent (cap_SGD.py) - Fair accuracy with all 21 and top 10 features, but very poor accuracy with "bottom 6."  Very fast execution times, but poor match with the dataset.

AdaBoost Clustering (cap_ABC.py) - Good accuracy with all 21 and top 10 features, but poor accuracy with "bottom 6." Good execution times (roughly 0.5s), but poor match with dataset.

#### Conclusion

Running k-Nearest Neighbors with k = 57 against the 6 features least correlated with the outcomes gave the best, most trustworthy results.  Obviously, more time could be spent tweaking parameters of the various classifiers, but these are good starting baselines.  Further honing of KNN results could be achieved.