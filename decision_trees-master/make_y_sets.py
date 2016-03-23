# make_y_sets.py
# Andrew Maner
# Thinkful 4.2
# build y_all (all y vals), y_test (subj <= 6), y_train (subj >= 27), &
# y_validate (subj >= 21 & <= 26)

import pandas as pd

df1 = pd.read_csv("y_train.txt",header=None,names=["act"])
df2 = pd.read_csv("y_test.txt",header=None,names=["act"])

# make y_all
chunks = [df1[0:346],df2[0:301],df1[347:687],df2[302:618],df1[688:1903],df2[619:1200],df1[1904:2219],df2[2101:1847],df1[2220:3604],df2[1848:2211],df1[3605:3964],df2[2212:2565],df1[3965:5065],df2[2566:2946],df1[5066:7351]]
df = pd.concat(chunks)
df.to_csv("y_all.csv",index=False,header=False)

# make y_train
df = df1[5867:7351]
df.to_csv("y_train.csv",index=False,header=False)

# make y_test
chunks = [df1[0:346],df2[0:301],df1[347:687],df2[302:618],df1[688:1314]]
df = pd.concat(chunks)
df.to_csv("y_test.csv",index=False,header=False)

# make y_validate
chunks = [df1[3965:5065],df2[2566:2946],df1[5066:5866]]
df = pd.concat(chunks)
df.to_csv("y_validate.csv",index=False,header=False)
