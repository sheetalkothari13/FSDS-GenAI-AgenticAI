import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\Naresh It Classes\August\26th\emp_sal.csv")

x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values


# SUPPORT VECTOR REGRESSION-SVR

from sklearn.svm import SVR
# svr_regressor = SVR()
svr_regressor = SVR(kernel='sigmoid',degree=5,gamma='auto', C=100)

svr_regressor.fit(x,y)

svr_moddel_pred = svr_regressor.predict([[6.5]])
print(svr_moddel_pred)

# KNN - K-NEAREST NEIGHBORS
from sklearn.neighbors import KNeighborsRegressor
# knn_reg_model = KNeighborsRegressor()
knn_reg_model = KNeighborsRegressor(n_neighbors=2, weights='uniform',algorithm='brute')

knn_reg_model.fit(x,y)

knn_reg_pred = knn_reg_model.predict([[6.5]])
print(knn_reg_pred)

