import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\Naresh It Classes\August\28th\emp_sal.csv")

x = dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values

# DECISION TREE REGRESSOR

from sklearn.tree import DecisionTreeRegressor
dtr_reg_model = DecisionTreeRegressor()
# dtr_reg_model = DecisionTreeRegressor(criterion='absolute_error',max_depth=10,splitter='random')
dtr_reg_model.fit(x,y)

dtr_reg_pred = dtr_reg_model.predict([[6.5]])
print(dtr_reg_pred)


# RANDOM FOREST

from sklearn.ensemble import RandomForestRegressor
# rfr_reg_model = RandomForestRegressor()
rfr_reg_model = RandomForestRegressor(n_estimators=6,random_state=0)
rfr_reg_model.fit(x,y)

rfr_reg_pred = rfr_reg_model.predict([[6.5]])
print(rfr_reg_pred)