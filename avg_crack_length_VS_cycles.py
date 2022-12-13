import mysql.connector
import matplotlib.pyplot as plt
import numpy as np


conn=mysql.connector.connect(host="localhost",user="root",password="anuradhaSQL1#",database="crack_lenght")
cur=conn.cursor()

query="select avg(crack_length),cycles from crack_data where cycles !=0 group by cycles ;"
cur.execute(query)
results = cur.fetchall()
conn.close()


avgcracklength=[]
noofcycles=[]
for a in results:
    print(a)
    avgcracklength.append(a[0])
    noofcycles.append(a[1])


# def f(x,a,b,c):
#     return a*x**2+b*x+c

# xlist = np.linspace(-10,10,num=1000)
# ylist =f(xlist,3,1,4)
# plt.figure(num=0,dpi=120)
# plt.plot(xlist,ylist)
# plt.show()

plt.plot(noofcycles,avgcracklength)
plt.show()