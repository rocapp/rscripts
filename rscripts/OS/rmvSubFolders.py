import os
import shutil

OPTIONS = raw_input('Enter an option [0, 2]')
initial_folder = raw_input('Enter Starting Folder: ')
rmv_folder = raw_input('Enter a Folder to Delete: ')

if OPTIONS == "0":
    subdirs = [x[0] for x in os.walk(initial_folder)]
    for sf in subdirs:
        subdirs = [x[0] for x in os.walk(sf)]
        local_rmv_path = os.path.join(os.path.join(initial_folder, sf), rmv_folder)
        if local_rmv_path in subdirs:
            print local_rmv_path
            shutil.rmtree(local_rmv_path)

elif OPTIONS == "2":
    subdirs = [x[0] for x in os.walk(initial_folder)]
    for sf in subdirs:
        sub1 = os.path.join(initial_folder, sf)
        subsubs = [x[0] for x in os.walk(sub1)]
        for s in subsubs:
            subsubsubs = [x[0] for x in os.walk(os.path.join(sub1, s))]
            for t in subsubsubs:
                if t.split("\\").count(rmv_folder) > 1:
                    print t
                    shutil.rmtree(t)
                
