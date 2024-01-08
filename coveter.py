from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import os

ecg_data  = np.loadtxt('sheng_RP_1.txt')
print(ecg_data)
ecg_data1 = ecg_data[0:199]
for i in range(9):
    ecg_data1 = np.vstack((ecg_data1,ecg_data[(i+1)*200:(i+2)*200-1]))
np.savetxt("Lyn_RP.txt",ecg_data1)
