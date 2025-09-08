import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\Naresh It Classes\August\25th\emp_sal.csv")

x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

#linear regression degree =1 
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(x,y)

plt.scatter(x,y, color = 'red')
plt.plot(x,lin_reg.predict(x),color='blue')
plt.title('Linear Regression graph')
plt.xlabel('Position Level')
plt.ylabel("Salary")
plt.show()

lin_model_pred = lin_reg.predict([[6.5]])
print(lin_model_pred)

#polynomial featreus is alg that by default contains degree 2
from sklearn.preprocessing import PolynomialFeatures
# poly_reg = PolynomialFeatures()
poly_reg = PolynomialFeatures(degree = 8)
x_poly = poly_reg.fit_transform(x)

poly_reg.fit(x_poly,y)

#for degree=2, we fit x_poly and y
lin_reg_2 = LinearRegression()
lin_reg_2.fit(x_poly,y)

plt.scatter(x,y,color='red')
plt.plot(x,lin_reg_2.predict(poly_reg.fit_transform(x)),color='blue')
plt.title('Truth or bluff(poly reg)')
plt.xlabel('position level')
plt.ylabel('salary')
plt.show()

poly_model_pred = lin_reg_2.predict(poly_reg.fit_transform([[6.5]]))
print(poly_model_pred)

# every ml models accuracy increases by doing hyper parameter tunings,
# in LLms its called fine tuning
# chatgpt has 405 billion parameter, thats y its called Large Language Model



