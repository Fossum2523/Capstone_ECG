'''from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets

X,y = datasets.make_regression(n_samples=200,n_features=1,n_targets=1,noise=10)

print(X)
print(X[:3,:])

plt.scatter(X,y,linewidths=0.1)
plt.show()

model = LinearRegression()

model.fit(X[:3,:],y[0:3])

predict = model.predict(X[:3,:])  

plt.plot(X[:3,:],predict,c="red")
plt.scatter(X[:3,:],y[0:3])
plt.show()'''

from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from sklearn import datasets
import openpyxl
import numpy
'''X=[[63],[52.45],[49.9],[54],[69.9],[60],[68.4],[60.9],[57],[66.9],[62.7],[64.5],[74.4],[63.09],[54.29],[38.2],[27.39],[66.5],
    [45.59],[54.9],[69.8],[60.5],[44.8],[40.7],[61.9],[60.7],[28.5],[59.4]]
Y=[125,133,123,122,121,118,132,125,124,123,122,116,119,118,130,130,129,133,132,135,135,128,135,133,139,140,132,141]'''


'''X=[[65.8],
 [42.9],
 [31.2],
 [44.6],
 [65. ],
 [61.9],
 [53.7],
 [62.8],
 [59.5],
 [63.5],
 [63.2],
 [51.9],
 [66.1],
 [63.8],
 [64. ],
 [66.1],
 [58. ],
 [49.4],
 [65. ],
 [61.1],
 [42.5],
 [47.8],
 [52.7],
 [52.2],
 [61.2]]
Y=[ 111,
    113,
    119,
    110,
    123,
    111,
    108,
    113,
    113,
    106,
    111,
    113,
    111,
    103,
    111,
    115,
    111,
    113,
    108,
    113,
    131,
    141,
    133,
    126,
    124]'''
'''w = openpyxl.load_workbook('Lyn.xlsx')
# 取得作用中的工作表
ws = wb.active

# 將 Excel 工作表轉為串列
myList = [row for row in ws.values]

# 將串列轉為 NumPy 陣列
myArr = numpy.array(myList)

# 輸出 NumPy 陣列
print(myArr)'''

X=[[63],[52.45],[49.9],[54],[69.9],[60],[68.4],[60.9],[57],[66.9],[62.7],[64.5],[74.4],[63.09],[54.29],[38.2],[27.39],[66.5],
    [45.59],[54.9],[69.8],[60.5],[44.8],[40.7],[61.9],[60.7],[28.5],[59.4],[65.8],
 [42.9],
 [31.2],
 [44.6],
 [65. ],
 [61.9],
 [53.7],
 [62.8],
 [59.5],
 [63.5],
 [63.2],
 [51.9],
 [66.1],
 [63.8],
 [64. ],
 [66.1],
 [58. ],
 [49.4],
 [65. ],
 [61.1],
 [42.5],
 [47.8],
 [52.7],
 [52.2],
 [61.2]]
Y=[ 125,133,123,122,121,118,132,125,124,123,122,116,119,118,130,130,129,133,132,135,135,128,135,133,139,140,132,141,
    111,
    113,
    119,
    110,
    123,
    111,
    108,
    113,
    113,
    106,
    111,
    113,
    111,
    103,
    111,
    115,
    111,
    113,
    108,
    113,
    131,
    141,
    133,
    126,
    124]

plt.scatter(X,Y,linewidths=0.1)
plt.show()

model = LinearRegression()

model.fit(X,Y)

predict = model.predict(X)  

plt.plot(X,predict,c="red")
plt.scatter(X,Y)
plt.show()
