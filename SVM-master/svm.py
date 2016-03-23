# svm.py
# Andrew Maner
# Thinkful 4.6 - Support Vector Machines

# Load data from iris data set
from sklearn import datasets
iris = datasets.load_iris()

# Description of iris data set:
# 	- iris.target: 0 = setosa, 1 = versicolor, 2 = virginica
#	- iris.feature_names[0] = 'sepal length (cm)'
#	- iris.feature_names[1] = 'sepal width (cm)'
# 	- iris.feature_names[2] = 'petal length (cm)'
#	- iris.feature_names[3] = 'petal width (cm)'
# 	- iris.data[0:49, 0] = sepal length values for setosa
#	- iris.data[0:49, 1] = sepal width values for setosa
# 	- iris.data[0:49, 2] = petal length values for setosa
#	- iris.data[0:49, 3] = petal width values for setosa
#	- iris.data[50:99, 0] = sepal length values for versicolor
#	- iris.data[50:99, 1] = sepal width values for versicolor
#	- iris.data[50:99, 2] = petal length values for versicolor
#	- iris.data[50:99, 3] = petal width values for versicolor
#	- iris.data[100:149, 0] = sepal length values for virginica
#	- iris.data[100:149, 1] = sepal width values for virginica
#	- iris.data[100:149, 2] = petal length values for virginica
#	- iris.data[100:149, 3] = petal width values for virginica

# Import packages we'll need
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import svm
from matplotlib.colors import ListedColormap
import numpy as np

# A bit of visual exploration
# Build a scatter matrix of all possible pairings of features,
# using the three flower types
df = pd.DataFrame(iris.data, columns=iris.feature_names)
axes = pd.tools.plotting.scatter_matrix(df, alpha=0.2)
plt.tight_layout()
plt.savefig('scatter_matrix.png')
plt.clf()
# We can see from this scatter matrix that, in general, it is 
# easy to see how to separate setosa from the other two species, 
# regardless of features being used.  It is not easy, however,
# to see how to separate virginica from versicolor...

# To illustrate more clearly, let's plot sepal width versus
# petal length for setosa and versicolor:
plt.scatter(iris.data[0:100, 1], iris.data[0:100, 2], c=iris.target[0:100])
plt.xlabel(iris.feature_names[1])
plt.ylabel(iris.feature_names[2])
plt.savefig('setosa_versicolor_sepwid_v_petlen.png')
plt.clf()
# Very clear separation between setosa and versicolor...
# We could easily draw a line in the plane that separates the two into clusters.

# So, let's apply the SVC module to this pairing:
svc = svm.SVC(kernel='linear')
X = iris.data[0:100, 1:3]
y = iris.target[0:100]

# plot_estimator function adapted from https://github.com/jakevdp/sklearn_scipy2013
# ListedColormap is used for generating a custom colormap
cmap_light = ListedColormap(['#FFAAAA', '#AAFFAA', '#AAAAFF'])
cmap_bold = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

def plot_estimator(estimator, X, y, num):
    estimator.fit(X, y)
    x_min, x_max = X[:, 0].min() - .1, X[:, 0].max() + .1
    y_min, y_max = X[:, 1].min() - .1, X[:, 1].max() + .1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, num),
                         np.linspace(y_min, y_max, num))
    Z = estimator.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=cmap_bold)
    plt.axis('tight')
    plt.axis('off')
    plt.tight_layout()

# OK, now let's apply the plot_estimator function:
plot_estimator(svc, X, y, 100)
plt.savefig('svm_setosa_versicolor_sepwid_v_petlen.png')
plt.clf()
# As expected, we get a nice separation of setosa and versicolor
# across a line drawn in the plane.

# So, let's see how things shake out with versicolor and virginica, 
# again using sepal width versus petal length:
svc = svm.SVC(kernel='linear')
X = iris.data[50:150, 1:3]
y = iris.target[50:150]
plot_estimator(svc, X, y, 100)
plt.savefig('svm_versicolor_virginica_sepwid_v_petlen.png')
plt.clf()
# We thought it might be hard to perfectly separate versicolor from
# virginica, and this is borne out by the result.  A few plants from
# both species are mis-identified.  (However, we have properly 
# classified the vast majority of plants.)
# Note: Changing C to get a wider soft margin did nothing for this
# particular example, so the code is omitted.

# Commence operation TypeWayTooMuch...

# We've looked at setosa v versicolor / sepal wid v petal len
# and versicolor v virginica / sepal wid v petal len.
# Let's now look at the other possible combinations...

# setosa v versicolor / sepal len v sepal wid
svc=svm.SVC(kernel='linear')
X = iris.data[0:100, 0:2]
y = iris.target[0:100]
plot_estimator(svc,X, y, 100)
plt.savefig('svm_setosa_versicolor_seplen_v_sepwid.png')
# Again, we have a nice separation btw setosa and versicolor.

# setosa v versicolor / sepal len v petal len
svc = svm.SVC(kernel='linear')
X = iris.data[0:100, [0,2]]
y = iris.target[0:100]
plot_estimator(svc, X, y, 100)
plt.savefig('svm_setosa_versicolor_seplen_v_petlen.png')
# Good separation, as expected...

# setosa v versicolor / sepal len v petal wid
svc = svm.SVC(kernel='linear')
X = iris.data[0:100, [0,3]]
y = iris.target[0:100]
plot_estimator(svc, X, y, 100)
plt.savefig('svm_setosa_versicolor_seplen_v_petwid.png')
# Good separation, as expected...

# setosa v versicolor / sepal wid v petal wid
svc = svm.SVC(kernel='linear')
X = iris.data[0:100, [1,3]]
y = iris.target[0:100]
plot_estimator(svc, X, y, 100)
plt.savefig('svm_setosa_versicolor_sepwid_v_petwid.png')
# Good separation, as expected...

# setosa v versicolor / petal len v petal wid
svc = svm.SVC(kernel='linear')
X = iris.data[0:100, [2,3]]
y = iris.target[0:100]
plot_estimator(svc, X, y, 100)
plt.savefig('svm_setosa_versicolor_petlen_v_petwid.png')
# Good sepration, as expected...

# setosa v virginica / sepal len v sepal wid
svc = svm.SVC(kernel='linear')
X = np.concatenate((iris.data[0:50, [0,1]], iris.data[100:150, [0,1]]), axis=0)
y = np.concatenate((iris.target[0:50], iris.target[100:150]), axis=0)
plot_estimator(svc, X, y, 100)
plt.savefig('svm_setosa_virginica_seplen_v_sepwid.png')
# Good separation, but one misclassification...
# Varying C does not change this.

# setosa v virginica / sepal len v petal len
svc = svm.SVC(kernel='linear')
X = np.concatenate((iris.data[0:50, [0,2]], iris.data[100:150, [0,2]]), axis=0)
y = np.concatenate((iris.target[0:50], iris.target[100:150]), axis=0)
plot_estimator(svc, X, y, 100)
plt.savefig('svm_setosa_virginica_seplen_v_petlen.png')
# Excellent separation...

# setosa v virginica / sepal len v petal wid
svc = svm.SVC(kernel='linear')
X = np.concatenate((iris.data[0:50, [0,3]], iris.data[100:150, [0,3]]), axis=0)
y = np.concatenate((iris.target[0:50], iris.target[100:150]), axis=0)
plot_estimator(svc, X, y, 100)
plt.savefig('svm_setosa_virginica_seplen_v_petwid.png')
# Excellent separation...

# setosa  v virginica / sepal wid v petal len
svc = svm.SVC(kernel='linear')
X = np.concatenate((iris.data[0:50, [1,2]], iris.data[100:150, [1,2]]), axis=0)
y = np.concatenate((iris.target[0:50], iris.target[100:150]), axis=0)
plot_estimator(svc, X, y, 100)
plt.savefig('svm_setosa_virginica_sepwid_v_petlen.png')
# Excellent separation...

# setosa  v virginica / sepal wid v petal wid
svc = svm.SVC(kernel='linear')
X = np.concatenate((iris.data[0:50, [1,3]], iris.data[100:150, [1,3]]), axis=0)
y = np.concatenate((iris.target[0:50], iris.target[100:150]), axis=0)
plot_estimator(svc, X, y, 100)
plt.savefig('svm_setosa_virginica_sepwid_v_petwid.png')
# Excellent separation...

# setosa  v virginica / petal len v petal wid
svc = svm.SVC(kernel='linear')
X = np.concatenate((iris.data[0:50, [2,3]], iris.data[100:150, [2,3]]), axis=0)
y = np.concatenate((iris.target[0:50], iris.target[100:150]), axis=0)
plot_estimator(svc, X, y, 100)
plt.savefig('svm_setosa_virginica_petlen_v_petwid.png')
# Excellent separation...

# versicolor  v virginica / sepal len v sepal wid
svc = svm.SVC(C=100.0, kernel='linear')
X = iris.data[50:150, [0,1]]
y = iris.target[50:150]
plot_estimator(svc, X, y, 100)
plt.savefig('svm_versicolor_virginica_seplen_v_sepwid.png')
# Poor classification with many incorrect assignments...
# Adjustment of C does not fix this.

# versicolor  v virginica / sepal len v petal len
svc = svm.SVC(kernel='linear')
X = iris.data[50:150, [0,2]]
y = iris.target[50:150]
plot_estimator(svc, X, y, 100)
plt.savefig('svm_versicolor_virginica_seplen_v_petlen.png')
# Decent classification, with a few incorrect assignments...
# Adjustment of C does not fix this.

# versicolor  v virginica / sepal len v petal wid
svc = svm.SVC(kernel='linear')
X = iris.data[50:150, [0,3]]
y = iris.target[50:150]
plot_estimator(svc, X, y, 100)
plt.savefig('svm_versicolor_virginica_seplen_v_petwid.png')
# Decent classification, with a few (4) incorrect assignments...
# Adjustment of C does not fix this.

# versicolor  v virginica / sepal wid v petal wid
svc = svm.SVC(kernel='linear')
X = iris.data[50:150, [1,3]]
y = iris.target[50:150]
plot_estimator(svc, X, y, 100)
plt.savefig('svm_versicolor_virginica_sepwid_v_petwid.png')
# Decent classification, with a few (5) incorrect assignments...
# Adjustment of C does not fix this.

# versicolor  v virginica / petal len v petal wid
svc = svm.SVC(kernel='linear')
X = iris.data[50:150, [2,3]]
y = iris.target[50:150]
plot_estimator(svc, X, y, 100)
plt.savefig('svm_versicolor_virginica_petlen_v_petwid.png')
# Decent classification, with a few (4) incorrect assignments...
# Adjustment of C does not fix this.

# Now for all three
# all three plants / sepal len v sepal wid
svc = svm.SVC(kernel='linear')
X = iris.data[0:150,[0,1]]
y = iris.target[0:150]
plot_estimator(svc, X, y, 500)
plt.savefig('svm_allthree_seplen_v_sepwid.png')
# Good classification of setosa, but versicolor and virginica have
# many improper assignments...
# Adjustment of C does not fix this.

# all three plants / sepal len v petal len
svc = svm.SVC(kernel='linear')
X = iris.data[0:150,[0,2]]
y = iris.target[0:150]
plot_estimator(svc, X, y, 500)
plt.savefig('svm_allthree_seplen_v_petlen.png')
# Good classification of setosa, but versicolor and virginica have
# a few (6) improper assignments...
# Adjustment of C does not fix this.

# all three plants / sepal len v petal wid
svc = svm.SVC(kernel='linear')
X = iris.data[0:150,[0,3]]
y = iris.target[0:150]
plot_estimator(svc, X, y, 500)
plt.savefig('svm_allthree_seplen_v_petwid.png')
# Good classification of setosa, but versicolor and virginica have
# a few (5) improper assignments...
# Adjustment of C does not fix this.

# all three plants / sepal wid v petal len
svc = svm.SVC(kernel='linear')
X = iris.data[0:150,[1,2]]
y = iris.target[0:150]
plot_estimator(svc, X, y, 500)
plt.savefig('svm_allthree_sepwid_v_petlen.png')
# Good classification of setosa, but versicolor and virginica have
# several (7) improper assignments...
# Adjustment of C does not fix this.

# all three plants / sepal wid v petal wid
svc = svm.SVC(kernel='linear')
X = iris.data[0:150,[1,3]]
y = iris.target[0:150]
plot_estimator(svc, X, y, 500)
plt.savefig('svm_allthree_sepwid_v_petwid.png')
# Good classification of setosa, but versicolor and virginica have
# a few (5) improper assignments...
# Adjustment of C does not fix this.

# all three plants / petal len v petal wid
svc = svm.SVC(kernel='linear')
X = iris.data[0:150,[2,3]]
y = iris.target[0:150]
plot_estimator(svc, X, y, 500)
plt.savefig('svm_allthree_petlen_v_petwid.png')
# Good classification of setosa, but versicolor and virginica have
# a few (4) improper assignments...
# Adjustment of C does not fix this.
