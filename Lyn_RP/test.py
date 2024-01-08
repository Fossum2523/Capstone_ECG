from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import os 
  
# Get the list of all files and directories 
# in the root directory 
NO_list=["Sheng_RP","Lyn_RP"]
dir_list =[]
path = "/Users/USER/Desktop/capstone6_3/"
for NO in NO_list:
    print(NO)
    dir_list = dir_list +  os.listdir(path+NO)
print(dir_list)
print("Files and directories in '", path, "' :")  

ecg_label_num = 0
stop =0
for NO in NO_list:
    print(NO)
    for filename in os.listdir(path+NO):
        print(filename)
        if filename != "test.py":
            ecg_data  = np.loadtxt("/Users/USER/Desktop/capstone6_3/"+NO+"/"+filename)
            # print(ecg_data)

            if ecg_label_num == 0 and stop ==0:
                stop=1
                ecg_data1 = ecg_data[0:200]
                ecg_label=0
            else:
                ecg_data1 = np.vstack((ecg_data1,ecg_data[0:200]))
                ecg_label = np.vstack((ecg_label, ecg_label_num))
            
            for i in range(9):
                ecg_label = np.vstack((ecg_label, ecg_label_num))
                ecg_data1 = np.vstack((ecg_data1,ecg_data[(i+1)*200:(i+2)*200]))


    ecg_label_num = ecg_label_num +1

print(ecg_data1)
print(ecg_label)

print(ecg_data1.shape)
print(ecg_label.shape)

print(dir_list)

sklda = LinearDiscriminantAnalysis()
data_2 = sklda.fit_transform(ecg_data1, ecg_label)

# plt.scatter(data_2[:, 0], data_2[:,0],c = ecg_label*2)
# plt.show()