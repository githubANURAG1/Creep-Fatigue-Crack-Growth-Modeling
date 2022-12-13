import xlrd
import matplotlib.pyplot as plt
import numpy as np


loc=("E:\\vscode\\python\\datas\\actual.xlsx");
a=xlrd.open_workbook(loc)
sheet=a.sheet_by_index(0) 

crack_length=[]
cycle_number=[]
stress_intensity=[]
time=[]
da_by_dn=[]

for i in range(2,sheet.nrows):
    crack_length.append(sheet.cell(i,1).value)
    cycle_number.append(sheet.cell(i,2).value)
    stress_intensity.append(sheet.cell(i,5).value)
    val=sheet.cell(i,3).value
    time.append(val/(60*60))
    da_by_dn.append(sheet.cell(i,4).value)


crack_length2=[]
stress_intensity2=[]
da_by_dn2=[]

loc2=("E:\\vscode\\python\\datas\\predict.xlsx");
a2=xlrd.open_workbook(loc2)
sheet2=a2.sheet_by_index(0) 

for i in range(2,sheet.nrows):
    crack_length2.append(sheet2.cell(i,1).value)
    
    stress_intensity2.append(sheet2.cell(i,2).value)
    # val=sheet2.cell(i,3).value
    # time.append(val/(60*60))
    da_by_dn2.append(sheet2.cell(i,3).value)



plt.scatter(cycle_number,stress_intensity2)
plt.xlabel("no of cycles ")
plt.ylabel("stress intensity (MPa/mm^-1/2)")
plt.show()