# multivariate.py
# Andrew Maner
# load 2012-2013 lending club statists
# use income (annual_inc) as expl var to model interest rates (int_rate)
# as response var
# add home ownership (home_ownership) to the model
# does this impact the significance of the coefficients in the univariate model?
# add the interaction of home_ownership and annual_inc as a new term
# how does this impact the new model?

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

loans = pd.read_csv("LoanStats3c.csv")
loans.dropna(inplace=True)
# remove % symbols from int_rate col and cast back to float
loans['int_rate'] = loans['int_rate'].astype(str).map(lambda x: x.rstrip('%')).astype(float)

# pull out the relevant columns for our univariate model
intrate = loans['int_rate']
annualinc = loans['annual_inc']

# the model
f = sm.OLS(intrate, sm.add_constant(annualinc)).fit()

print f.summary()

# Intercept - the p-value for the intercept is far less than any level of significance we 
# might choose, so it is significant
# Income slope - the p-value for the slope coefficient is 0.157, which is greater than any
# LOS we might choose, so it is NOT significant
# R-squared - the r-squared is 0.003, so only about 0.3% of variation in interest rates
# is described by annual income.  this is not a good model.

print "\n"

# now add home_ownership to the mix
homeown = loans['home_ownership']
# make dummy variables because homeown is categorical (MORTGAGE, OWN, RENT)
dummies = pd.get_dummies(homeown)
# build the X variable
X = pd.concat([annualinc, dummies], axis=1)
# this has too many dummies - we will fall into the dummy variable multicollinearity trap - so
# we drop the OWN variable (chosen for no reason at all).  coefficients on MORTGAGE and RENT
# will show effect relative to OWN

X.drop(['OWN'], inplace=True, axis=1)
X = X.applymap(np.int)
# now add a constant column for the intercept
X = sm.add_constant(X)
# the model
f = sm.OLS(intrate, X).fit()

print f.summary()
# Intercept - the p-value for the int is < any alhpa we might use, so it is significant
# Income coeff - p-value is 0.102, so it is NOT significant
# MORTGAGE - coeff p-value is 0.596, so it is NOT significant
# RENT - coeff p-value is 0.613, so it is NOT significant
# R-squared - the r-squared is 0.007, so only about 0.7% of variation in interest rates is
# described by the model.  this is not a good model.

# Home ownership and annual income are likely to be correlated, so let's try an interaction variable:
# annual_inc * home_ownership

# interaction variable
mort = dummies['MORTGAGE']
rent = dummies['RENT']
inc_mort = annualinc * mort
inc_rent = annualinc * rent
interact = pd.concat([inc_mort, inc_rent], axis=1)

# set up the model
X = pd.concat([annualinc, dummies, interact], axis=1)
X.drop(['OWN'], inplace=True, axis=1)
# column names got dropped from interaction
X.columns = ['annual_inc', 'MORTGAGE', 'RENT', 'inc_mort', 'inc_rent']
X = sm.add_constant(X)
# the model
f = sm.OLS(intrate, X).fit()

print f.summary()

# Intercept - the p-value for the int is < any alpha we might use, so it is significant
# income coeff - p-value is 0.137, so it is NOT significant
# home ownership coeffs - p-values for the dummy vars are > any alpha we might use, so they
# are NOT significant
# interaction - p-values are > any alpha we might use, so these are NOT significant
# R-squared - the r-squared is 0.01, so about 1% of variation in interest rates is 
# described by the model.  this is not a good model