# make_x_sets.py
# Andrew Maner
# Thinkful 4.2
# build x_all (all x vals), x_test (subj <= 6), x_train (subj >= 27), &
# x_validate (subj >= 21 & <= 26)

import pandas as pd
import numpy as np

feature_df = pd.read_csv("features.csv",header=0)
feature_list = list(feature_df.values.flatten())

xtrain = np.loadtxt('X_train.txt')
xtest = np.loadtxt('X_test.txt')
df1 = pd.DataFrame(xtrain,columns=feature_list)
df2 = pd.DataFrame(xtest, columns=feature_list)

# make x_all
chunks = [df1[0:346],df2[0:301],df1[347:687],df2[302:618],df1[688:1903],df2[619:1200],df1[1904:2219],df2[2101:1847],df1[2220:3604],df2[1848:2211],df1[3605:3964],df2[2212:2565],df1[3965:5065],df2[2566:2946],df1[5066:7351]]
df = pd.concat(chunks)
df.to_csv("x_all.csv",index=False,header=False)

# make x_train
df = df1[5867:7351]
df.to_csv("x_train.csv",index=False,header=False)

# make x_test
chunks = [df1[0:346],df2[0:301],df1[347:687],df2[302:618],df1[688:1314]]
df = pd.concat(chunks)
df.to_csv("x_test.csv",index=False,header=False)

# make x_validate
chunks = [df1[3965:5065],df2[2566:2946],df1[5066:5866]]
df = pd.concat(chunks)
df.to_csv("x_validate.csv",index=False,header=False)
