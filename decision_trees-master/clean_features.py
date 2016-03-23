# clean_features.py
# Andrew Maner
# Thinkful 4.2.2 
# assumption: features.txt is in the same directory as the script.  
# data is in two columns - index in column 1 and feature names in column 2
# output: csv containing 561 cleaned feature names 

import pandas as pd
import numpy as np
import asciitable as asc

# use asciitable.read to read the data into a np.recarray
data = asc.read('features.txt')
# convert to a simple list
data = [ data[i][1] for i in range(0,561) ]
# convert to a data frame
df = pd.DataFrame(data, columns=["features"])

for i in range(0,561):
	df["features"][i] = df["features"][i].replace("-","_")
	df["features"][i] = df["features"][i].replace("()","")
	df["features"][i] = df["features"][i].replace("(","_")
	df["features"][i] = df["features"][i].replace(")","")
	df["features"][i] = df["features"][i].replace(",","_")
	df["features"][i] = df["features"][i].replace("mean","Mean")
	df["features"][i] = df["features"][i].replace("std","STD")
	df["features"][i] = df["features"][i].replace("Body","")
	

df.to_csv('features.csv', index=False)
