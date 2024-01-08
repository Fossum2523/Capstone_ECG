from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing

ecg_data = np.loadtxt('1000.txt').T
ecg_data1 = np.loadtxt('1001.txt').T
ecg_data = np.vstack((ecg_data,ecg_data1))
# -------------------------------------------------------------
ecg_data1 = np.loadtxt('1100.txt').T
ecg_data = np.vstack((ecg_data,ecg_data1))
ecg_data1 = np.loadtxt('1101.txt').T
ecg_data = np.vstack((ecg_data,ecg_data1))
# -------------------------------------------------------------
ecg_data1 = np.loadtxt('1102.txt').T
ecg_data = np.vstack((ecg_data,ecg_data1))
ecg_data1 = np.loadtxt('1103.txt').T
ecg_data = np.vstack((ecg_data,ecg_data1))
# -------------------------------------------------------------
print(ecg_data )
# print(ecg_data[0,:] )

print('ecg_data shape:',ecg_data.shape)

ecg_label = 0

for i in range(9):
    ecg_label = np.vstack((ecg_label, 0))
print(ecg_label)
for i in range(10):
    ecg_label = np.vstack((ecg_label, 1))
for i in range(10):
    ecg_label = np.vstack((ecg_label, 2))
print(ecg_label)
print(ecg_data.shape)
print(ecg_label.shape)

sklda= LinearDiscriminantAnalysis()

data_2 = sklda.fit_transform(ecg_data, ecg_label)


#########################################LDA
sklda = LinearDiscriminantAnalysis()
data_2 = sklda.fit_transform(ecg_data, ecg_label)
#########################################視覺化
plt.scatter(data_2[:, 0], data_2[:,1],c = ecg_label*2)
plt.show()
#########################################模型參數
transform_matrix = sklda.scalings_
print(transform_matrix.shape)
#########################################將資料轉換到新的平面上
# transform_matrix = np.array(transform_matrix)
transform_data = np.dot(ecg_data,transform_matrix)
plt.scatter(transform_data[:, 0], transform_data[:, 1],c = ecg_label*2)
plt.show()
#########################################求群中心
mean_class = np.zeros((3,2))
count = 0
for i in range(3):
    count = 0
    for j in range(transform_data.shape[0]):
        if ecg_label[j] == i:
            mean_class[i,0] = mean_class[i,0] + transform_data[j,0]
            mean_class[i,1] = mean_class[i,1] + transform_data[j,1]
            count = count + 1
    mean_class[i,0] = mean_class[i,0] / count
    mean_class[i,1] = mean_class[i,1] / count

plt.plot(mean_class[0,0] ,mean_class[0,1], 'or')
plt.plot(mean_class[1,0] ,mean_class[1,1], 'og')
plt.plot(mean_class[2,0] ,mean_class[2,1], 'ob')
print(mean_class)
plt.show()
##########################################測試資料
print(ecg_data)

test_data = ecg_data[0]
test_transform = np.dot(test_data,transform_matrix)
plt.plot(mean_class[0,0] ,mean_class[0,1], 'or')
plt.plot(mean_class[1,0] ,mean_class[1,1], 'og')
plt.plot(mean_class[2,0] ,mean_class[2,1], 'ob')
plt.plot(test_transform[0] ,test_transform[1], 'oy')
plt.show()

print(1)

test_data = ecg_data[1]
test_transform = np.dot(test_data,transform_matrix)
plt.plot(mean_class[0,0] ,mean_class[0,1], 'or')
plt.plot(mean_class[1,0] ,mean_class[1,1], 'og')
plt.plot(mean_class[2,0] ,mean_class[2,1], 'ob')
plt.plot(test_transform[0] ,test_transform[1], 'oy')
plt.show()

print(2)

test_data = ecg_data[2]
test_transform = np.dot(test_data,transform_matrix)
plt.plot(mean_class[0,0] ,mean_class[0,1], 'or')
plt.plot(mean_class[1,0] ,mean_class[1,1], 'og')
plt.plot(mean_class[2,0] ,mean_class[2,1], 'ob')
plt.plot(test_transform[0] ,test_transform[1], 'oy')
plt.show()