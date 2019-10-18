# Lets automate the process of deleting any empty folders from the Downloads folder

import os
import time

time.sleep(245)

# Folders to look into - fl

fl = [
    '/home/gautham/Downloads',
]

def remove_empty_folders(folder_path):
    if os.path.isdir(folder_path):
        if not os.listdir(folder_path):
            return os.rmdir(folder_path)
        else:
            for abp, folder_list, rlp in os.walk(folder_path):
                for each_dir in folder_list:
                    remove_empty_folders(os.path.join(abp, each_dir))

for f in fl :
    remove_empty_folders(f)