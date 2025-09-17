import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv(r"D:\Naresh It Classes\4. September\10- Decision Tree Algorithm\Social_Network_Ads.csv")

x = dataset.iloc[:,[2,3]].values
y = dataset.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.20,random_state=0)

'''
from sklearn.preprocessing import Normalizer
sc = Normalizer()
x_train = sc.fit_transform(x_train)
x_test = sc.transform(x_test)
'''

from sklearn.tree import DecisionTreeClassifier
classifier = DecisionTreeClassifier(criterion='entropy', max_depth=10, random_state=0)
classifier.fit(x_train,y_train)

y_pred = classifier.predict(x_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_pred)
print(cm)

from sklearn.metrics import accuracy_score

ac = accuracy_score(y_test,y_pred)
print(ac)

bias = classifier.score(x_train,y_train)
print(bias) # training set results

variance = classifier.score(x_test,y_test)
print(variance) #testing set results

from sklearn.metrics import classification_report
cr = classification_report(y_test, y_pred)
print(cr)

# Decision Tree - Standard Scalar = 91.25
#               - Normalizer = 0.6
#               - Without = 91.25
# test_size=0.20,random_state=0 = 92.5