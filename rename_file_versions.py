import sys
import os
from termcolor import colored

old_version = sys.argv[1]
new_version = sys.argv[2]

path = os.getcwd()
current_folder = ""
for root, directories, files in os.walk(path, topdown=True):
    Current_dir = path.split("\\")[-1]
    splitted_root = root.split("\\")
    current_dir_index = splitted_root.index(Current_dir)
    current_folder_new = "\\".join(splitted_root[current_dir_index:])    
    for name in files:
        max_file_length = len(max(files,key=len))
        if old_version in name:
            old_name = os.path.join(root, name)
            new_name_simple = name.replace(old_version,new_version)
            new_name = os.path.join(root, new_name_simple)
            if current_folder_new != current_folder:
                current_folder = current_folder_new
                print("\n-->", colored(current_folder_new,'red', attrs=['bold']))
            try:
                os.rename(old_name, new_name)
            except FileExistsError as e:
                print("---->", colored(new_name_simple+" already exists",attrs=['bold']))
            else:
                spacing = (max_file_length-len(new_name_simple))*" "
                print("---->", name, spacing, "-->", new_name_simple)
