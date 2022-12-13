import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

conn=mysql.connector.connect(host="localhost",user="root",password="anuradhaSQL1#",database="crack_lenght")
cur=conn.cursor()

query1="select avg(crack_length) from crack_data where cycles !=0 group by cycles;"
cur.execute(query1)
cracklength = cur.fetchall()

query2="select avg(time) from crack_data where cycles !=0 group by cycles;"
cur.execute(query2)
time = cur.fetchall()

conn.close()


# cracklength=[]
# time=[]
# for a in results:
#     print(a)
#     cracklength.append(a[0])
#     time.append(a[1])


# def f(x,a,b,c):
#     return a*x**2+b*x+c

# xlist = np.linspace(-10,10,num=1000)
# ylist =f(xlist,3,1,4)
# plt.figure(num=0,dpi=120)
# plt.plot(xlist,ylist)
# plt.show()

plt.plot(time,cracklength)
plt.show()