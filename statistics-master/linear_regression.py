# linear_regression.py
# Andrew Maner
# Thinkful challenge 2.3.3 (a bit of 2.3.2 included)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# read in the data
loans = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
# drop null rows
loans.dropna(inplace=True)
# strip % symbols from interest.rate and months & years from loan.length
loans['Interest.Rate'] = loans['Interest.Rate'].map(lambda x: x.rstrip('%'))
loans['Loan.Length'] = loans['Loan.Length'].map(lambda x: x.rstrip('months'))
loans['Loan.Length'] = loans['Loan.Length'].map(lambda x: x.rstrip('years'))
# convert fico.range ranges to single values and store in new column fico.score
loans['FICO.Score'] = loans['FICO.Range'].astype(str)
loans_list = loans['FICO.Score'].tolist()
fico = []
for array in range(len(loans_list)):
	loan = loans_list[array].split("-")
	fico.append(int(loan[0]))
loans['FICO.Score'] = fico

# make and save a histogram of the FICO.Score data
plt.figure()
p = loans['FICO.Score'].hist()
plt.savefig("FICO_histogram.png")
plt.clf()
# this is not a gaussian distribution

# create a scatterplot matrix to look for relationships
a = pd.scatter_matrix(loans,alpha=0.05,figsize=(10,10))
plt.savefig("scatter_matrix.png")
# this reveals a linear relationship btw fico score and interest rate
# and a linear relationship btw monthly income and loan amount
# so perhaps we should use fico and loan amount as independent variables

# extract some columns for analysis
intrate = loans['Interest.Rate'].astype(float)
loanamt = loans['Amount.Funded.By.Investors'].astype(float)
fico = loans['FICO.Score'].astype(float)

# dependent variable
y = np.matrix(intrate).transpose()
# independent variables
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
# input matrix
x = np.column_stack([x1,x2])

# linear model
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()

print 'Coefficients: ', f.params[0:2]
print 'Intercept: ', f.params[2]
print 'p-values: ', f.pvalues 
print 'R-Squared: ', f.rsquared 

# all p-values are MUCH less than a typical level of significance, like 0.05
# so we know our intercept is non-zero, as are our coefficients.  most important
# are the coefficients, since we now know we have legitimate relationships
# btw x1 and x2 and y
# in addition, the R-Squared is about 0.66. in other words, roughly 66% of the variation in 
# interest rates (in this data) can be explained by loan amounts and fico scores

# save our clean loans data for later
loans.to_csv('loansData_clean.csv',header=True,index=False)