import shutil as sh
import os

OPTIONS = raw_input('Enter 0 or 1: ')
initial_folder = raw_input('Enter Starting Folder: ')

if OPTIONS == "0":
    for f_ in os.listdir(initial_folder):
        if f_.endswith('gmdx'):
            print f_
            file_name = os.path.join(initial_folder, f_)
            folder_name = file_name.replace(".gmdx", '')
            try:
                os.makedirs(folder_name)
            except WindowsError:
                pass
            sh.move(file_name, folder_name)
            try:
                sh.move(file_name.replace(".gmdx", "_description")+".docx", folder_name)
            except IOError:
                pass

if OPTIONS == "1":
    FILE_NAME = raw_input('Enter a file name to search in subdirectories.')
    SEARCH_TERM = raw_input('Enter a term to search.')
    OUT_DIR = raw_input('Enter a folder to move results to.')
    subdirs = [f_[0] for f_ in os.walk(initial_folder)]
    for sf in subdirs:
        files = os.listdir(sf)
        for f in files:
            if FILE_NAME in f:
                subdirs.remove(sf)
                with open(os.path.join(sf, f)) as fo:
                    for line in fo:
                        if SEARCH_TERM in line:
                            fo.close()
                            try:
                                sh.move(sf, OUT_DIR)
                                break
                            except sh.Error:
                                break
                    
        
