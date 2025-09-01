import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
import pickle
import os


dataset = pd.read_csv(r"C:\Users\Sheetal\SheetalProjects\August\20th-MLR House price\House_data.csv")

dataset.head()

print(dataset.isnull().any())

dataset.dtypes

dataset = dataset.drop(['id','date'], axis=1)
# dataset = dataset[(dataset <= 999999).all(axis=1)]

# Reset index after deletion (optional)
# dataset = dataset.reset_index(drop=True)


y = dataset.iloc[:, 0]
x = dataset.iloc[:, 1:4]

x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=0)

regressor = LinearRegression()
regressor.fit(x_train,y_train)

y_pred = regressor.predict(x_test)

m = regressor.coef_
m

c = regressor.intercept_
c

x = np.append(arr = np.full((21613,1),67512).astype(int),values = x,axis = 1)


x_opt = x[:,[0,1,3]]
regressor_OLS = sm.OLS(endog=y,exog =x_opt).fit()#endog-garbage in,exog = garbage out(fit in and fit out)
regressor_OLS.summary()
# Nothing is “wrong” if R² = Adjusted R². Just interpret it as your predictors being strong or having only one predictor.

filename = 'multiple_linear_regression_model.pkl'
with open(filename, 'wb') as file:
    pickle.dump(regressor, file)
print("Model has been pickled and saved as multiple_linear_regression_model.pkl")

print("Full path:", os.path.abspath(filename))
