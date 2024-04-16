import os

folder_path = "path/to/your/folder"  # Replace with the actual folder path

file_list = []  # List to store the file names

for file_name in os.listdir(folder_path):
    if file_name.endswith(".pdf"):  # Filter for PDF files (optional)
        file_list.append(file_name)

print(file_list)