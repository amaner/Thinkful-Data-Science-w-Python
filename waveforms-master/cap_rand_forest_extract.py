# cap_KMeans_extract.py

import pandas as pd
import sklearn.ensemble as ske
import matplotlib.pyplot as plt

df = pd.read_csv('waveform.data', header=None)
colnames = ['f1','f2','f3','f4','f5','f6','f7','f8','f9','f10','f11','f12','f13','f14','f15','f16','f17','f18','f19','f20','f21','class']
df.columns = colnames
# break data into waveforms vs classes
features = colnames[0:21]
X = df[features]
y = df['class']
# find the most important features using random forest classifier
clf = ske.RandomForestClassifier(n_estimators=500, oob_score=True)
clf = clf.fit(X,y)
importances = clf.feature_importances_
print(type(importances))
top10_indices = importances.argsort()[-10:][::-1]
top10_features = [colnames[x] for x in top10_indices]
print top10_features
# ['f11', 'f7', 'f15', 'f6', 'f12', 'f10', 'f13', 'f5', 'f9', 'f16']
top10_scores = [importances[x] for x in top10_indices]
print top10_scores
# [0.10343269130661191, 0.080404298280227632, 0.077732863890841539, 0.076252297585869142, 0.070796270284234575, 0.070303937041961681, 0.059142045157806133, 0.057781315985070532, 0.052106144783530692, 0.05082533844588992]
# let's plot them
x = range(1,11)
plt.figure()
plt.scatter(top10_indices+1,top10_scores,c='r')
plt.xlabel('index')
plt.ylabel('importance score')
plt.title('Top 10 Importance Scores')
plt.savefig('top_10_features.png')
plt.clf()


