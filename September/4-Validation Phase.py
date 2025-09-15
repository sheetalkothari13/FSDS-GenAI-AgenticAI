import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\Naresh It Classes\September\4-\logit classification.csv")

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


# FUTURE PREDICTION
dataset1 = pd.read_csv(r"D:\Naresh It Classes\September\4-\final1.csv")

d2 = dataset1.copy()

dataset1 = dataset1.iloc[:,[3,4]].values

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
M = sc.fit_transform(dataset1)

y_pred1 = pd.DataFrame()

d2['Logistic_model_fut_pred'] = classifier.predict(M)
d2.to_csv('4-validationFinal.csv')

# we do multiple model testing,
# we build the model with seen data, predict on unseen data,compare with live data, we do the testing
# then after multipple testing we take the avg and find the accuracy
