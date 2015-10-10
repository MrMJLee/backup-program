import pickle
import os
import os.path
from directories import Directories

def test():
    d = Directories()
    # storing current hash values in a index file as a list
    indices = d.paths_in_index().values()
    # storing current filenames in the object folder as a list
    filenames = os.listdir(d.objects)

    sizeofIndex = len(indices)
    sizeofFiles = len(filenames)
    count = 0;
    #for root, dirs, files in os.walk(d.objects, topdown=False):
     #   for name in files:
     #       print name
     #   for name in dirs:
     #       print name
    if os.path.exists(d.index) and os.path.isfile(d.index):
        if sizeofFiles> 0 and sizeofIndex>0:
            print "filenames in the object folder"
            print "The size of index %d" %sizeofIndex
            print "The size of files in object folder %d" % sizeofFiles
            for name in filenames:
                if name in indices:
                    count+=1
    print count




