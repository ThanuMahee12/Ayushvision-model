import os
from os import path,walk,listdir,scandir,mkdir,mkdir,makedirs,rename,remove
from shutil import rmtree,copytree,copy2,move
from datetime import datetime
from openpyxl import Workbook
import csv
import zipfile
import yaml


#File extextension


file_extention=lambda file: path.splitext(file)[1]


# parent folder


file_parent_folder=lambda file:path.dirname(file)


# parent folder name


file_parent_folder_name=lambda file:path.basename(path.dirname(file))


# subfolders name


sub_folders = lambda root_folder: [d for d in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, d))] if os.path.exists(root_folder) else f'{root_folder} does not exist'


# number of subfolders


num_sub_folders = lambda root_folder: len([d for d in os.listdir(root_folder) if os.path.isdir(os.path.join(root_folder, d))]) if os.path.exists(root_folder) else f'{root_folder} does not exist'


# subfolders all_paths 


list_all_subfolders = lambda root_dir: [os.path.join(dp, d) for dp, dn, _ in os.walk(root_dir) for d in dn]


# subfolder paths


subfolders_path = lambda root_dir: [f.path for f in scandir(root_dir) if f.is_dir()]


# number of files in a folder


count_files_in_folder = lambda folder_path: sum([len(files) for _, _, files in walk(folder_path)])



# create new Folder


create_new_folder=lambda folder:mkdir(folder)



# create nested folders


create_new_folders=lambda pathname:makedirs(pathname) if not path.exists(pathname) else "already exsist"



# Delete folder
# 


delete_folders=lambda folder:rmtree(folder) if path.exists(folder) else 'folder not exsist'


# copyfolder


copy_folder= lambda source ,target :copytree(source,target) if path.exists(source) and not path.exists(target) else f"{source} path not exsist or {target} path already exsist"



# file copy


copy_file=lambda file, target_folder: copy2(file, target_folder) if path.exists(file) and path.isfile(file) and path.exists(target_folder) else f"Error: File '{file}' or target folder '{target_folder}' does not exist or is not a file."


# Rename folder


rename_folder=lambda old_name,new_name:rename(old_name,new_name) if path.exists(old_name) and not path.exists(new_name)  else f'{new_name}already here or {old_name} not exsist '


rename_folder_with_exsist=lambda old_name,new_name:move(old_name,new_name) if path.exists(old_name) and path.isdir(old_name) and path.isdir(new_name) else f' {old_name} not exsist or {new_name}{old_name} is not folder'



# rename file


rename_filename=lambda old_path,new_name:rename(old_path,f'{path.dirname(old_path)}//{new_name}{path.splitext(old_path)[1]}') if path.exists(old_path) and not path.exists(new_name)  else f'{new_name}already here or {old_path} not exsist '


# move file


rename_file=lambda old_path,new_path:rename(old_path,new_path) if path.exists(old_path) and  path.exists(path.dirname(new_path))  else f'{path.dirname(new_path)} folder not exsist here or {old_path} not exsist'


# rename with mv


rename_file_mv=lambda old_path,new_path:move(old_path,new_path) if path.exists(old_path) and  path.exists(path.dirname(new_path))  else f'{path.dirname(new_path)} folder not exsist here or {old_path} not exsist'


# Yaml 


# Read


def yamlread(filename):
    config=0
    with open(filename, 'r',encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config


# write


def ymalwrite(data,filename):
    with open(filename, 'w',encoding='utf-8') as yaml_file:
        yaml.dump(data, yaml_file,allow_unicode=True)


# subfolder to root folder mv


move_files_to_root = lambda root_folder, subfolder: [move(path.join(subfolder, file), root_folder) for file in listdir(subfolder)]


# Join filename


join_path=lambda *pathname:path.join(*pathname)


# Relative path


rel_path=lambda pathname,root:path.relpath(pathname,root)


# Remove File


remove_a_file=lambda filename:remove(filename) if path.exists(filename) else print('file not found')


# Relpace path


replace_path=lambda pathname,replace_root,root:path.join(replace_root,path.relpath(pathname,root))


# write open file txt


newfile=lambda filename,mode='w',encoding='utf-8': open(filename,mode,encoding=encoding)


# read File data


readfile=lambda filename,mode='r',readline=False:open(filename,mode).read() if not readline else open(filename,mode).readlines()


# clear file


def clearfile(filename):
    with open(filename,'w'):
        pass


# subfolder file count 


def get_subfolder_file_counts(root_folder):
    subfolder_file_counts = {}
    for subfolder in listdir(root_folder):
        subfolder_path = path.join(root_folder, subfolder)
        if path.isdir(subfolder_path):
            file_count = len(listdir(subfolder_path))
            subfolder_file_counts[subfolder] = file_count
    return subfolder_file_counts



# Empty Folder name


def find_empty_subfolders(root_folder):
    empty_subfolders = []
    for subfolder in listdir(root_folder):
        subfolder_path = path.join(root_folder, subfolder)
        if path.isdir(subfolder_path) and not listdir(subfolder_path):
            empty_subfolders.append(subfolder)
    return empty_subfolders


# save csv file 


def save_to_csv_filedetails(data,colums=[],csv_filename=None,save_folder=None):
    date_time_obj = datetime.now()
    count=0
    csv_filename =csv_filename if csv_filename!=None else date_time_obj.strftime("_%Y_%m_%d_%H_%M_%S")
    if  not data or not isinstance(colums,list) or len(colums)<0:
        raise Exception("list type data colums are required ")
    if csv_filename.find(".csv") ==-1:
       csv_filename=f'{csv_filename}.csv'
    filpath=path.join(save_folder,csv_filename) if save_folder!=None else csv_filename
    with open(filpath, 'a', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(colums)
        for datai in data:
            row=[]
            if isinstance(datai,dict):
                for col in colums:
                    d=' '
                    try:
                        d=datai.get(col)
                    except:
                        d=' '
                    row.append(d)
            else:
                row=datai
            csv_writer.writerow(row)
            count=count+1
    return count



# save the excel file


def save_to_excel(colums=[],data=[],root_folder=None,excel_filename=None):
    date_time_obj = datetime.now()
    count=0
    excel_filename =excel_filename if excel_filename!=None else date_time_obj.strftime("_%Y_%m_%d_%H_%M_%S")
    if  not data or not isinstance(colums,list) or len(colums)<0:
        raise Exception("list type data colums are required ")
    if excel_filename.find(".xlsx") ==-1:
       excel_filename=f'{excel_filename}.xlsx'
    filpath= path.join(root_folder,excel_filename) if root_folder==None else excel_filename
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(colums)

    for datai in data:
        row=[]
        if isinstance(datai,dict):
            for col in colums:
                d=' '
                try:
                    d=datai.get(col)
                except:
                     d=' '
                row.append(d)
        else:
            row=datai
        sheet.append(row)
        count=count+1
    workbook.save(filpath)
    return count


# All files in a folder


def file_paths(rootfolder):
    paths=[]
    if not path.exists(rootfolder):
        raise Exception("folder Not Found")
    for root,dirs,files in walk(rootfolder):
        for file in files:
            paths.append([join_path(root,file),root,file])
    return paths


# copy folder stucture


def copy_folder_stucture(base,target):
   if not path.exists(target):
        mkdir(target)
   for root,dirs,files in walk(base):
        relpath=path.relpath(root,base)
        new_folder=path.join(target,relpath)
        if not path.exists(new_folder):
             makedirs(new_folder)
print('created')


# total files in a folder


def count_of_folder(root):
    total=0
    for root,dirs,files in walk(root):
        total=total+len(files)
    return total
    


# folder size 


# in mb


def folder_size_in_mb(folder_path):
    total_size = 0
    # Iterate through all files and subdirectories in the folder
    for dirpath, _, filenames in walk(folder_path):
        for filename in filenames:
            file_path = path.join(dirpath, filename)
            # Get the size of each file and add it to the total size
            total_size += path.getsize(file_path)
    # Convert total size to MB
    total_size_mb = total_size / (1024 * 1024)
    return total_size_mb


# in kb


def folder_size_in_kb(folder_path):
    total_size = 0
    # Iterate through all files and subdirectories in the folder
    for dirpath, _, filenames in walk(folder_path):
        for filename in filenames:
            file_path = path.join(dirpath, filename)
            # Get the size of each file and add it to the total size
            total_size += path.getsize(file_path)
    # Convert total size to MB
    total_size_kb = total_size /1024 
    return total_size_kb


# in GB


def folder_size_in_gb(folder_path):
    total_size = 0
    # Iterate through all files and subdirectories in the folder
    for dirpath, _, filenames in walk(folder_path):
        for filename in filenames:
            file_path = path.join(dirpath, filename)
            # Get the size of each file and add it to the total size
            total_size += path.getsize(file_path)
    # Convert total size to MB
    total_size_gb = total_size /(1024*1024*1024) 
    return total_size_gb


# create dataTime


def createTimelist(image_paths):
     file_create_details=[]
     for image_path in image_paths:
          creation_timestamp=path.getctime(image_path)
          createdate=datetime.fromtimestamp(creation_timestamp)
          file_create_details.append([image_path,createdate.strftime("%c"), 
                             createdate.strftime("%B"),
                             createdate.strftime("%Y %B"),
                             createdate.strftime("%d/%m/%Y"),
                             createdate.strftime("%I:%M:%S")+" "+createdate.strftime("%p")
                             ])
     return file_create_details


# Zip Subfolders

def zip_subfolders(directory,zipFolder=None):
    # Get the list of subfolders in the directory
    subfolders = [f for f in listdir(directory) if path.isdir(path.join(directory, f))]

    # Iterate over each subfolder
    for subfolder in subfolders:
        subfolder_path = path.join(directory, subfolder)
        zip_folder_dir=path.join(directory,'zips') if zipFolder==None else zipFolder
        if not path.exists(zip_folder_dir):
            makedirs(zip_folder_dir)
        zip_filename = path.join(zip_folder_dir,f"{subfolder}.zip")

        # Create a new ZIP file for the subfolder
        with zipfile.ZipFile(zip_filename, "w") as zipf:
            # Add all files in the subfolder to the ZIP file
            for root, _, files in walk(subfolder_path):
                for file in files:
                    file_path = path.join(root, file)
                    zipf.write(file_path, path.relpath(file_path, subfolder_path))

        print(f"Subfolder '{subfolder}' zipped successfully to '{zip_filename}'")


