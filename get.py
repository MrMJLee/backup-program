import os
import shutil
from directories import Directories

d = Directories()
def get(searchArg):
    options = []
    paths = d.paths_in_index()
    count = 0

    for x in paths:
        if count ==50:
            break
        if searchArg in x:
            options.append(x)
            count+=1
    if len(options) ==0:
        print "No matching files exist"

    if len(options) ==1:
        path = options[0]
        print "Files Matching %s:" % searchArg
        print path+"\n"
        sourcePath = os.path.join(d.objects, paths[path])
        copyTo = os.path.split(path)[-1]
        copyFile(path,sourcePath,copyTo)

    else:
        print "Files Matching %s:" % searchArg
        option = list(enumerate(options, start=1))
        while(True):
            for index, item in option:
                print index, item

            select = raw_input("\nSelect File Number / 'Q' of quit: ")
            if select.lower() == 'q':
                break
            else:
                try:
                    path =  option[int(select)-1][1]
                    sourcePath = os.path.join(d.objects, paths[path])
                    copyTo = os.path.split(path)[-1]
                    copyFile(path,sourcePath,copyTo)
                    break
                except (IndexError, ValueError):
                    print "Invalid options\n"

def copyFile(path,sourcePath,copyTo):
    if os.path.exists(copyTo):
        ask = raw_input("%s already exists, Overwrite? (y/n) " %path)
        if ask.lower() == 'y':
            shutil.copyfile(sourcePath ,copyTo)
            print path+ " saved successfully"
    else:
        shutil.copyfile(sourcePath ,copyTo)
        print path+ " saved successfully"

