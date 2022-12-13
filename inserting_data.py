import pandas as pd
import matplotlib.pyplot as plt
import numpy as np 
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import PolynomialFeatures



data=pd.read_csv("C:\\data for project\\617\\Sp 4\\A617_Sp4-12days-DK15-r2_Channels (Measured values)_2.csv", encoding= 'unicode_escape',sep=';')
df=pd.DataFrame(data)

df=df.dropna()

df.astype({"Cycles" : 'int'})
df.astype({"Crack length": 'float'})
df.groupby('Cycles').mean()

print(df)

parameters=df.drop('Crack length',axis=1)
cracklength=df['Crack length']

cycles=df['Cycles']
        
model =linear_model.LinearRegression()
model.fit(parameters,cracklength)


# data2=pd.read_csv("C:\\data for project\\617\\Sp 4\\A617_Sp4-12days-DK15-r2_Channels (Measured values)_2.csv", encoding= 'unicode_escape',sep=';')
# df2=pd.DataFrame(data2)

# df=df.dropna()

# df2.astype({"Cycles" : 'int'})
# df2.groupby('Cycles').mean()

# print(df2)

# parameters2=df2.drop('[Crack length]',axis=1)
# cracklength2=df2['Crack length']
# cycles2=df2['Cycles']
        

predicted_cracklength=model.predict(parameters)

plt.scatter(cycles,cracklength)
plt.show()