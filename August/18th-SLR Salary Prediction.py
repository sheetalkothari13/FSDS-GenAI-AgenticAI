import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\Naresh It Classes\August\14th Regression, Simple Linear Regression\Salary_Data.csv")

x = dataset.iloc[:,:-1]
y = dataset.iloc[:,-1]

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size = 0.2,random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train, y_train)

y_pred = regressor.predict(x_test)

plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_train, regressor.predict(x_train),color='blue')
plt.title('Salary vs Experience(Test Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

# predicted points are red color
# actualpoints or line is blue color

m = regressor.coef_
c = regressor.intercept_

(m*12)+c  #for someone with 12 years of exp
(m*20)+c

bias = regressor.score(x_train,y_train)
bias

variance = regressor.score(x_test,y_test)
variance

# Stats for ML

print(dataset.mean())

print(dataset.median())

print(dataset['Salary'].mode())

print(dataset.var())

print(dataset['Salary'].var())

print(dataset.std())

print(dataset['Salary'].std())

from scipy.stats import variation
variation(dataset.values)

variation(dataset['Salary'])  #variation - it's a measure of how spread out or dispersed data points are from each other and from the average value

dataset.corr()

dataset['Salary'].corr(dataset['YearsExperience'])

dataset.skew()

dataset['Salary'].skew()

dataset.sem()  #standard error

import scipy.stats as stats

dataset.apply(stats.zscore)

#gives no. of rows
a = dataset.shape[0]
b = dataset.shape[1]

degree_of_freedom = a-b
print(degree_of_freedom)

#ssr
y_mean = np.mean(y)
SSR = np.sum((y_pred-y_mean)**2)
print(SSR)

#sse
y=y[0:6]
SSE = np.sum((y-y_pred)**2)
print(SSE)

#sst
mean_total = np.mean(dataset.values)
SST = np.sum((dataset.values-mean_total)**2)
print(SST)

#r^2
r_square = 1-SSR/SST
print(r_square)    #good model coz in range 0-1

