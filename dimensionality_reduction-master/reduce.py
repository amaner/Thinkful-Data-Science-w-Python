# reduce.py
# Andrew Maner
# Thinkful Data Sci w/ Python Unit 4.7
# Dimensionality Reduction

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.decomposition import PCA
from sklearn.lda import LDA
import pylab as pl
from sklearn.neighbors import KNeighborsClassifier

iris = datasets.load_iris()
X = iris.data
y = iris.target
features = iris.feature_names
targets = iris.target_names

# shape of iris data
print "IRIS dataset shape:", X.shape

# plot the iris data - sepal length v sepal width
plt.figure()
for c, i, target in zip("rgb", [0,1,2], targets):
	plt.scatter(X[y == i, 0], X[y == i, 1], c=c, label=target)
plt.legend()
plt.xlabel(features[0])
plt.ylabel(features[1])
plt.title('Iris Data')
plt.show()
plt.clf()
# good separation btw setosa and the others, but
# poor separation btw versicolor & virginica

pca = PCA(n_components=2)
X_pca = pca.fit(X).transform(X)
# new shape
print "PCA reduced shape:", X_pca.shape
print "PCA components (2):", pca.components_
print "PCA explained variance ratio (first two components):", pca.explained_variance_ratio_
print "Meaning of the components:"
for component in pca.components_:
	print " + ".join("%.3f x %s" % (value, name) 
		for value, name in zip(component, features))

# plot the PCA
plt.figure()
for c, i, target in zip("rgb", [0,1,2], targets):
	plt.scatter(X_pca[y == i, 0], X_pca[y == i, 1], c=c, label=target)
plt.legend()
plt.title('PCA of Iris Data')
plt.show()
plt.clf()
# significantly better separation btw virg and vers

# do KNN on the data
neigh = KNeighborsClassifier(n_neighbors=3)
y_pred = neigh.fit(X_pca, y).predict(X_pca)
pl.scatter(X_pca[:,0], X_pca[:, 1], c=y_pred)
pl.show()
pl.clf()
# roughly the same...?

lda = LDA(n_components=2)
X_lda = lda.fit(X,y).transform(X)
# new shape
print "LDA reduced shape:", X_lda.shape

# plot the LDA
plt.figure()
for c, i, target in zip("rgb", [0,1,2], targets):
	plt.scatter(X_lda[ y == i, 0], X_lda[y == i, 1], c=c, label=target)
plt.legend()
plt.title('LDA of Iris Data')
plt.show()
plt.clf()
# good separation between the three species

# do KNN again
neigh = KNeighborsClassifier(n_neighbors=3)
y_pred = neigh.fit(X_lda, y).predict(X_lda)
pl.scatter(X_lda[:,0], X_lda[:, 1], c=y_pred)
pl.show()
pl.clf()
# again, roughly the same...?
