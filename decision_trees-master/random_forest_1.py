# random_forest_1.py
# Andrew Maner
#
# load UCI HAR dataset (already separated into x_train, x_test, x_validate,
# y_train, y_test, y_validate, and features csv files)
# 
# fit a random forest classifier (w/ 500 estimators) to the xtrain data
# output the top 10 most important features and their importance scores
#
# test the model on the test and validate sets
# output accuracy scores for the model's performance on the test and validate sets
# output precision score, recall score, and f1 score for the model's performance
# on the test set
# output the model's confusion matrix for the test set

import pandas as pd
import sklearn.ensemble as ske
import sklearn.metrics as skm
import numpy as np
import matplotlib.pyplot as plt

# load the feature names (as dataframe) and convert to list
feature_df = pd.read_csv("features.csv",header=0)
feature_list = list(feature_df.values.flatten())

# load xtrain set and use feature_list to label its columns
xtrain = pd.read_csv("x_train.csv",header=None,names=feature_list)
# load the ytrain set as well
ytrain = pd.read_csv("y_train.csv",header=None,names=["activity"])

# set up a 500 estimator random random_forest
clf = ske.RandomForestClassifier(n_estimators=500, oob_score=True)
# fit it to the xtrain and ytrain data
clf = clf.fit(xtrain,ytrain.activity)
# get the oob_score
print clf.oob_score_
# we get 0.9919

# get the importance scores
importances = np.array(clf.feature_importances_)
# get the top 10 indices of features
top10_indices = importances.argsort()[-10:][::-1]
print top10_indices
# we get 56, 40, 52, 58, 49, 558, 53, 42, 50, 41
# but which features are these?
top10_features = [feature_list[x] for x in top10_indices]
print top10_features
# tGravityAcc_energy_X, tGravityAcc_Mean_X, tGravityAcc_min_X, tGravityAcc_energy_Z, 
# tGravityAcc_max_X, angle_X_gravityMean, tGravityAcc_min_Y, tGravityAcc_Mean_Z,
# tGravityAcc_max_Y, tGravityAcc_Mean_Y
# and what are their scores?
top10_scores = [importances[x] for x in top10_indices]
print top10_scores
# 0.03275m 0.03063, 0.03034, 0.02846, 0.02786, 0.02531, 0.01754, 0.01653, 0.01607, 0.01589

# find accuracy scores...
# first we need to load the training and validation sets
xtest = pd.read_csv("x_test.csv",header=None,names=feature_list)
xval = pd.read_csv("x_validate.csv",header=None,names=feature_list)
ytest = pd.read_csv("y_test.csv",header=None,names=["activity"])
yval = pd.read_csv("y_validate.csv",header=None,names=["activity"])
# and then get predictions (as arrays)
test_pred = clf.predict(xtest)
val_pred = clf.predict(xval)
# now we can get the scores
print skm.accuracy_score(ytest, test_pred)
# accuracy score for test set: 0.80923
print skm.accuracy_score(yval, val_pred)
# accuracy score for validation set: 0.81780

# find precision, recall, and F1 scores on the test set
print skm.precision_score(ytest, test_pred)
# precision score 0.81887
print skm.recall_score(ytest, test_pred)
# 0.80923
print skm.f1_score(ytest, test_pred)
# 0.80710

# plot confusion matrix
cm = skm.confusion_matrix(ytest, test_pred)
plt.matshow(cm)
plt.title('Confusion Matrix')
plt.colorbar()
plt.ylabel('True Label')
plt.xlabel('Predicted Label')
plt.show()

# done!