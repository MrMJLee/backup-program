import os
import shutil
from directories import Directories

def restore(destPath=None):
    d = Directories()
    paths = d.paths_in_index()

    for path in paths.keys():
        try:
            sourcePath = os.path.join(d.objects, paths[path])
           # print sourcePath
            if destPath is None:
                dest = path
            else:
                dest = os.path.join(destPath, path)
            directory = os.path.join(*os.path.split(dest)[0:-1])
            restoreFiles(dest,sourcePath,directory)
        except IOError:
            print "Invalid Path"
            break

def restoreFiles(dest, sourcePath,directory):
    if not os.path.exists(directory) and not os.path.isdir(directory):
        os.makedirs(directory) # make directory
    if os.path.exists(dest):
        ask = raw_input("%s already exists, Overwrite? (y/n) " %dest)
        if ask.lower() == 'y':
            shutil.copyfile(sourcePath, dest)
            print dest+ " saved successfully\n"
        else:
            print
    else:
        shutil.copyfile(sourcePath ,dest)
        print dest+ " saved successfully\n"