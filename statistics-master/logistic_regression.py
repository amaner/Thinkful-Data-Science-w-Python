# logistic_regression.py
# Andrew Maner
# Thinkful data science with python 2.4.2

import pandas as pd 
import statsmodels.api as sm
import math

#read the data, which was cleaned during linear regression
loans = pd.read_csv("loansData_clean.csv")

# make a new column that determines whether an interest rate is < 12 or not
loans['IR_TF'] = loans['Interest.Rate'].map(lambda x: 1 if x < 12.0 else 0)

# add an intercept column
loans['Intercept'] = float(1.0)

# make a list of independent variables
ind_vars = ['Intercept','Amount.Requested','FICO.Score']

# start making our model
X = loans[ind_vars]
y = loans['IR_TF']

logit = sm.Logit(y,X)
result = logit.fit()
coeff = result.params
print coeff
print "\n"
print "The probability of getting a loan with a given FICO and requested amount is: "
print "p(FICO,Amount) = 1/(1+e^({} + {}(FICO) + {}(Amount))".format(coeff[0],coeff[2],coeff[1])
print "\n"
print "The probability of getting a $10k loan at less than 12 pct interest, with a FICO score of 720 is: "
p = 1/(1+math.exp(coeff[0]+720.0*coeff[2]+10000*coeff[1]))
print "P(720,10000) = ", p
if p < 0.70:
	print "It is highly unlikely you will get the loan."
else:
	print "You may well get the loan."
