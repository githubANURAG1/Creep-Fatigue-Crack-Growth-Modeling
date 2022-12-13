import matplotlib.pyplot as plt
import numpy as np 
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures


# liner regression

# diabetes = datasets.load_diabetes()
# diabetes_X=diabetes.data[:,np.newaxis,2]

# diabetes_X_train = diabetes_X[:-30]
# diabetes_X_test = diabetes_X[-30:]
# diabetes_Y_train =diabetes.target[:-30] 
# diabetes_Y_test =diabetes.target[-30:]

# model =linear_model.LinearRegression()
# model.fit(diabetes_X_train,diabetes_Y_train)

# diabetes_Y_predict=model.predict(diabetes_X_test)


# print("mean squared error is:", mean_squared_error(diabetes_Y_test,diabetes_Y_predict,squared="false"))

# plt.scatter(diabetes_X_test,diabetes_Y_test)
# plt.show()

# print(diabetes_X)



# 2 degree graph 

def f(x,a,b,c):
    return a*x**2+b*x+c

xlist =np.linspace(-10,10,num=101)
ylist =f(xlist,3,1,4)
# plt.scatter(xlist,ylist)
# plt.show()

# print(xlist)

# polynomial regression
x=xlist[-50:]
print(x)
poly_features=preprocessing.PolynomialFeatures(degree=2,inclde_bias=False)
X_poly=poly_features.fit_transform(x)


# model.fit(diabetes_X_train,diabetes_Y_train)

# # diabetes_Y_predict=model.predict(diabetes_X_test)


# # print("mean squared error is:", mean_squared_error(diabetes_Y_test,diabetes_Y_predict,squared="false"))

# plt.scatter(diabetes_X_test,diabetes_Y_test)
# plt.show()

# # print(diabetes_X)