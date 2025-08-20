

import numpy as np

import matplotlib.pyplot as plt

import pandas as pd

dataset = pd.read_csv(r"D:\Naresh It Classes\August\13\Data.csv") # read dataset

x = dataset.iloc[:,:-1].values  #divide into x-independent and y-dependent
y = dataset.iloc[:,3].values
                                #Has nan values(null)
from sklearn.impute import SimpleImputer
imputer = SimpleImputer()   #uses mean strategy to fill the numerical values
# imputer = SimpleImputer(strategy="median")
# imputer = SimpleImputer(strategy="most_frequent")

imputer = imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])


from sklearn.preprocessing import LabelEncoder     #for converting catogorical to numerical
labelencoder_x = LabelEncoder()

labelencoder_x.fit_transform(x[:,0])   #works without this as well
x[:,0] = labelencoder_x.fit_transform(x[:,0])

labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)


from sklearn.model_selection import train_test_split      #for training and testing the model
# x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.8,test_size=0.2)
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.5)
x_train,x_test,y_train,y_test = train_test_split(x,y,train_size=0.7, random_state=0)



















