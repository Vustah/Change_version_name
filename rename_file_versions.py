import sys
import os

old_version = sys.argv[1]
new_version = sys.argv[2]

path = os.getcwd()
for root, directories, files in os.walk(path, topdown=False):
    for name in files:
        if old_version in name:
            old_name = os.path.join(root, name)
            new_name = name.replace(old_version,new_version)
            new_name = os.path.join(root, new_name)
            os.rename(old_name, new_name)
            print(old_name, " --> ", new_name)
