# kmeans1.py
# Andrew Maner
# Use scipy.cluster.vq.kmeans to calculate clusters on un.csv, using
# kmeans, for k in 0, ..., 10.  Show the elbow plot (k vs average
# within cluster SSQ) to help find the optimum k for clustering.

import numpy as np
import scipy.cluster.vq as scv
import pandas as pd
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

# read in the data
df = pd.read_csv("un.csv")
# make a list of the names of the columns in which we're interested
colnames = ['lifeMale','lifeFemale','infantMortality','GDPperCapita']
# strip off these columns
df2 = pd.DataFrame(df[colnames])
# drop nas in place
df2.dropna(inplace=True)
# range of k values we'll use
k_list = range(1,11)
# do the kmeans for each k in the list
KM = [ scv.kmeans(df2.values, k) for k in k_list ]
# now KM contains a list of centroids and distortions (variances) for each k
# let's pull off the distortions
ave_wc_SSQ = [ var for (cent, var) in KM ]
# let's plot the elbow plot
plt.figure()
plt.scatter(k_list, ave_wc_SSQ)
plt.xlabel('Number of Clusters')
plt.ylabel('Ave. Within-Cluster SSQ')
plt.title('Elbow Plot for kMeans Clustering')
plt.show()
plt.clf()
# the plot starts to level out near k=3, so that's what we'll use
# in the next bit of code (kmeans2.py)
