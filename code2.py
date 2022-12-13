import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


from sklearn.model_selection import train_test_split
from sklearn import linear_model
train_set,test_set = train_test_split(df,test_size=0.3,random_state=42)
print(f"Rows in trainSet is {len(train_set)}\nRows in testSet is{len(test_set)}\n")


label_train = train_set["Crack length"]
feature_train = train_set.drop(["Crack length"],axis=1)
model = linear_model.LinearRegression()
model.fit(feature_train,label_train)


from sklearn.metrics import mean_squared_error
feature_test=test_set.drop(["Crack length"],axis=1)
label_test=test_set["Crack length"]
label_predict = model.predict(feature_test)
print(np.sqrt(mean_squared_error(label_test,label_predict)))