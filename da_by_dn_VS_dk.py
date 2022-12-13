import math
import matplotlib.pyplot as plt
import mysql.connector
import numpy as np

conn=mysql.connector.connect(host="localhost",user="root",password="anuradhaSQL1#",database="crack_lenght")
cur=conn.cursor()

query1="select avg(stress) from crack_data where cycles !=0 group by cycles;"
cur.execute(query1)
dk = cur.fetchall()

query2="select avg(crack_length)/cycles from crack_data where cycles !=0 group by cycles;"
cur.execute(query2)
da_by_dn = cur.fetchall()
conn.close()
for i in da_by_dn:
    print(i)

plt.scatter(dk,da_by_dn)
plt.show()