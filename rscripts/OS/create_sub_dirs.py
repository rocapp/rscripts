import os

initial_folder = raw_input('Enter Starting Folder: ')

new_sub = ""
subs = []
while new_sub != "0":
    new_sub = raw_input("Enter a new subfolder OR '0'  to quit: ")
    if new_sub != "0":
        subs.append(new_sub)

subdirs = [x[0] for x in os.walk(initial_folder)]
for sf in subdirs:
    for s in subs:
        subpath = os.path.join(os.path.join(initial_folder, sf), s)
        print subpath
        try:
            os.makedirs(subpath)
        except WindowsError:
            pass

