import os
import shutil
from directories import Directories
def restore(destPath=None):
    d = Directories()
    paths = d.paths_in_index()
    options = []
    for x in paths:
        options.append(x)

    for i in range(0,len(options)):
        path =  options[i]
        sourcePath = os.path.join(d.objects, paths[path])
        copyTo = os.path.split(path)[-1]
        if destPath ==None:
            copyFiles(path,sourcePath,copyTo)
        else:
            dest = os.path.join(destPath,copyTo)
            copyFiles(path,sourcePath,dest)


def copyFiles(path,sourcePath,copyTo):
    if os.path.exists(copyTo):
        ask = raw_input("%s already exists, Overwrite? (y/n) " %path)
        if ask.lower() == 'y':
            shutil.copyfile(sourcePath ,copyTo)
            print path+ " saved successfully\n"

    else:
        shutil.copyfile(sourcePath ,copyTo)
        print path+ " saved successfully\n"


