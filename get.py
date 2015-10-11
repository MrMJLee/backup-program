import os
import shutil
from directories import Directories

d = Directories()
def get(searchArg):
# show what files are in the archive
    options = []
    paths = d.paths_in_index()
    count = 0
    for x in paths:
        if searchArg in x:
            options.append(x)
        if count ==50:
            break
    if len(options) ==0:
        print "No matching files exist"

    if len(options) ==1:
        path = options[0]
        print "Files Matching %s:" % searchArg
        print path+"\n"
        shutil.copyfile(os.path.join(d.objects, paths[path]) ,os.path.split(path)[-1])
        print path+ " saved successfully"

    else:
        print "Files Matching %s:" % searchArg
        option = list(enumerate(options, start=1))
        while(True):
            for index, item in option:
                print index, item
            select = raw_input("\nSelect a number to save a file: ")
            try:
                path =  option[int(select)-1][1]
                shutil.copyfile(os.path.join(d.objects, paths[path]) ,os.path.split(path)[-1])
                print path + " saved successfully"
                break
            except (IndexError, ValueError):
                print "Invalid options\n"

        # for index, item in option:
        #     if index == select:
        #         path = item
        #         shutil.copyfile(os.path.join(d.objects, paths[path]) ,os.path.split(path)[-1])
        #         print path + " saved successfully"
        #         break






