import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = pd.read_csv(r"D:\Naresh It Classes\August\20th\Investment.csv")

x = dataset.iloc[:,:-1]
y = dataset.iloc[:,4]

x = pd.get_dummies(x,dtype=int)

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

m = regressor.coef_ 
print(m)

c = regressor.intercept_
print(c)

#adding constant 1 for every record
# x = np.append(arr = np.ones((50,1)).astype(int), values = x , axis = 1)

x = np.append(arr = np.full((50,1),42467).astype(int), values = x , axis = 1)


# to solve the business problem and the find out the best one to invest in or the independent attribute thats causing a lot of impact in the dependent attribute
# we use this method of backward elimination

import statsmodels.api as sm

x_opt = x[:,[0,1,2,3,4,5]]

regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()
regressor_OLS.summary()


# R2 > AdjustedR2 Good Model(Perfect)
# we got t-test becoz it is a sample
# all the maths computation is done by statsmodel.api
# Highest p-value is x4
# if p>0.05 we eliminate these attributes
# here p-value of x4 => 0.990 which is greater than 0.05 -> we eliminate the attribute
# this is calle reject the null hypothesis

# directly remove the unnecessary index
# here removed 4th index
x_opt = x[:,[0,1,2,3,5]]
regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()
regressor_OLS.summary()

# here romoved the 5th index
x_opt = x[:,[0,1,2,3]]
regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()
regressor_OLS.summary()

x_opt = x[:,[0,1,3]]
regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()
regressor_OLS.summary()

x_opt = x[:,[0,1]]
regressor_OLS = sm.OLS(endog=y, exog=x_opt).fit()
regressor_OLS.summary()

#Final Verdict-> INVEST MORE IN x1 (DIGITAL MARKETING) TO GAIN HIGHER PROFITS

# you can do the eleminationin 1 single step or do this way in multiple steps removing 1 after other
# p-value is used in stocks like 'grow'
# p-value=0.05
# it is used to reject the null hypothesis
# it is used compare and eliminate the attribute
# BACKWARD ELEMINATION
# it comes under Recursive Feature Elimination

# Q) How to Eliminate features in ML model?
# -> Business understaning
# -> based in p-value
# -> based on PCA
# -> based on decision tree

bias = regressor.score(x_train, y_train)
bias

variance = regressor.score(x_test, y_test)
variance

# visualize train data point 
# plt.scatter(x_train, y_train, color = 'red') 
# plt.plot(x_train, regressor.predict(x_train), color = 'blue')
# plt.title('(Training set)')
# plt.xlabel('Years of Experience')
# plt.ylabel('Salary')
# plt.show()

# The problem: x_train is NOT a single column — after pd.get_dummies(), it became a DataFrame with multiple columns.
# Matplotlib expects x to be 1D for scatter/plotting, but you are giving it a matrix → hence the ValueError.



