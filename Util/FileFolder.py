import os
# Folder Size in Mb
def folder_size_in_mb(folder_path):
    total_size = 0
    # Iterate through all files and subdirectories in the folder
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # Get the size of each file and add it to the total size
            total_size += os.path.getsize(file_path)
    # Convert total size to MB
    total_size_mb = total_size / (1024 * 1024)
    return total_size_mb

# Folder Size In GB

def folder_size_in_gb(folder_path):
    total_size = 0
    # Iterate through all files and subdirectories in the folder
    for dirpath, _, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            # Get the size of each file and add it to the total size
            total_size += os.path.getsize(file_path)
    # Convert total size to MB
    total_size_gb = total_size /(1024*1024*1024) 
    return total_size_gb

# Count Nuber of Files in the Folder
count_files_in_folder = lambda folder_path: sum([len(files) for _, _, files in os.walk( folder_path)])