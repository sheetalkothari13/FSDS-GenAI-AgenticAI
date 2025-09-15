import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\Naresh It Classes\September\3-\logit classification.csv")

x = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.20, random_state=0)

# Standardization -Feature Scaling
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)

# Normalization
# from sklearn.preprocessing import Normalizer
# nc = Normalizer()
# x_train = nc.fit_transform(x_train)
# x_test = nc.transform(x_test)

# Logistic Regression - Classifier model
from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)

# there are some misclassifications, so we makes confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Model Accuracy
from sklearn.metrics import accuracy_score
ac = accuracy_score(y_test, y_pred)
print(ac)

# Classification report
from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred)
print(cr)

# Training score
bias = classifier.score(x_train, y_train)
print(bias) 

# Testing score
variance = classifier.score(x_test,y_test)
print(variance)

# if bias score is very very less than variance then the model is overfitting we use cross validation- grid search cv or random search cv
# if bias score is high and variance score is less, then the model is underfitting,then the model is retrained with more attributes
# when random state = 0, we get optimizer accuracy

# accuracy = 0.925
# bias = 0.821875
# variace = 0.925
# this is a best fit model, no over or under fitting, and the required accuracy was 90% and we got 92.50% which is satisfiesd when the test score is 20% and there is no hyper parameter tuning 

# model testing on unseen data- Validation data
# train and test happpens on seen data



