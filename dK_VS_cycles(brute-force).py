import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import math

conn=mysql.connector.connect(host="localhost",user="root",password="anuradhaSQL1#",database="crack_lenght")
cur=conn.cursor()

query1="select avg(force_val) ,cycles from crack_data where cycles !=0 group by cycles;"
cur.execute(query1)
results1 = cur.fetchall()

query2="select avg(crack_length) ,cycles from crack_data where cycles !=0 group by cycles;"
cur.execute(query2)
results2 = cur.fetchall()
conn.close()

avgcracklength=[]
noofcycles=[]

print(len(results1)," ",len(results2))
if(len(results1)!=len(results2)):
    print("cycles in crack_lenght and load doesnot match")
    exit()


dk_val=[]
cycles=[]
for i in range(0,len(results1)):
    if(results1[i][1]==results2[i][1]):
        P=results1[i][0]
        W=100                         # let width be 100mm
        B= 10                         # let thickness be 10mm
        a=results2[i][0]/W   
        cycle_no =results1[i][1]

        nominator=P*(2+a)*(0.886+4.64*a-13.32*a*a+14.72*a*a*a-5.64*a*a*a*a)
        denominator=B*math.sqrt(W)*math.pow(1-a,1.5)
        if(denominator!=0):
            dk_val.append(nominator/denominator)
            cycles.append(cycle_no)

plt.plot(cycles,dk_val)
plt.show()