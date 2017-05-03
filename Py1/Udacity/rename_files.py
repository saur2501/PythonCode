import os
from string import digits
def rename_files():
    #get file names from a folder
    saved_path = os.getcwd()
    file_list = os.listdir(r"C:\Users\Saurabh\Desktop\Python\photos")
    print(file_list)
    os.chdir(r"C:\Users\Saurabh\Desktop\Python\photos")
    #for each file, rename filename
    for file_name in file_list:
        os.rename(file_name, file_name.translate(str.maketrans('','',digits)))
    os.chdir(saved_path)
rename_files()
