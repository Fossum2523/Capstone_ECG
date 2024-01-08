# Python program to explain os.listdir() method  
    
# importing os module  
import os 
  
# Get the list of all files and directories 
# in the root directory 
path = "/Users/USER/Desktop/capstone6_3/Lyn_RP"
dir_list = os.listdir(path) 
  
print("Files and directories in '", path, "' :")  

for filename in dir_list:
    print(filename)

# print the list 
print(dir_list)