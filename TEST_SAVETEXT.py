import numpy as np
test1=[1,2,3,4]
test2=[2,3,4,5]
test3=[0,0,0,0]
a =np.array( [
1,2,3
])
# np.savetxt('a.txt', a, delimiter=',', fmt='%.2f')
print(a)
b=np.append(a,[1,2])
np.savetxt('a.txt', a)
print(b)

for i in range(4):
    test3[i]=test1[i]-test2[i]

print(test3)
ecg_data = []

if type(ecg_data)==list:
        print(type(ecg_data))

else:
    print("ppppp")
ecg_data = [1,2,3]
ecg_data = np.vstack((ecg_data,[4,5,6]))
ecg_data = np.vstack((ecg_data,[7,8,9]))

if ecg_data.all:
    print(ecg_data)
