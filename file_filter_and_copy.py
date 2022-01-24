import os
import shutil


def filter_exist_files(dir_location1=r"C:\Users\user\Pictures", dir_location2=r"C:\Users\user\Pictures2"):
    files_A = set(os.listdir(dir_location1))
    for each in os.listdir(dir_location2):
        if each in files_A:
            files_A.remove(each)
    return files_A


def copy_File(source, destination, files, file_type="jpg"):
    try:
        for each in files:
            if len(each) > len(file_type) and each[-(len(file_type)):] == file_type:
                shutil.copyfile(source+"\\"+each,
                                os.path.join(destination, each))
        return True
    except Exception as err:
        print("failed_due_to ", err)
        return False


source = r"C:\Users\user\Pictures"
destination = r"C:\Users\user\Pictures\\New_folder"
copy_File(source, destination, filter_exist_files())
