import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline

from sklearn import preprocessing
# from sklearn.preproccessing import PolynomialFeatures
from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import r2_score

dataset = pd.read_csv(r"D:\Naresh It Classes\August\21st Regularization techniques\car-mpg.csv")
dataset.head(5)

dataset = dataset.drop(['car_name'],axis=1)
dataset['origin'] = dataset['origin'].replace({1:'america', 2:'europe', 3:'asia'})

dataset = pd.get_dummies(dataset,columns=['origin'],dtype=int)
dataset = dataset.replace('?',np.nan)

dataset = dataset.apply(pd.to_numeric,errors='ignore')
numeric_cols = dataset.select_dtypes(include=[np.number]).columns    # filling missing values with median for numeric column
dataset[numeric_cols] = dataset[numeric_cols].apply(lambda x: x.fillna(x.median()))
# Convert possible columns to numeric.
# Identify numeric columns.
# Replace missing values in those numeric columns with their median.

dataset.head(5)

#Model Building
x = dataset.drop(['mpg'],axis=1)
y = dataset[['mpg']]

# Scaling down
x_s = preprocessing.scale(x)
x_s = pd.DataFrame(x_s,columns = x.columns)

y_s = preprocessing.scale(y)
y_s = pd.DataFrame(y_s,columns=y.columns)

dataset.shape

x_train,x_test,y_train,y_test = train_test_split(x_s,y_s, test_size=0.3, random_state=1)


regression_model = LinearRegression()
regression_model.fit(x_train, y_train)

for idx, col_name in enumerate(x_train.columns):
    print('The coefficient for {} is {}'.format(col_name, regression_model.coef_[0][idx]))
    
intercept = regression_model.intercept_[0]
print('The intercept is {}'.format(intercept))

# Regularized Ridge Regression-L2
#alpha factor here is lambda (penalty term) which helps to reduce the magnitude of coeff
ridge_model = Ridge(alpha = 0.5)
ridge_model.fit(x_train, y_train)

print('Ridge model coef: {}'.format(ridge_model.coef_))
#As the data has 10 columns hence 10 coefficients appear here  

# Regularization Lasso Regression-L1
lasso_model = Lasso(alpha = 0.2)
lasso_model.fit(x_train, y_train)

print('Lasso model coef: {}'.format(lasso_model.coef_))

#Simple Linear Model
print(regression_model.score(x_train, y_train))
print(regression_model.score(x_test, y_test))

print('*************************')

#Ridge
print(ridge_model.score(x_train, y_train))
print(ridge_model.score(x_test, y_test))

print('*************************')

#Lasso
print(lasso_model.score(x_train, y_train))
print(lasso_model.score(x_test, y_test))