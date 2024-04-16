import os

folder_path = "path/to/your/folder" 

file_list = []  

for file_name in os.listdir(folder_path):
    if file_name.endswith(".pdf"):  
        file_list.append(file_name)

print(file_list)