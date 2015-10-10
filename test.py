import pickle
import os
import os.path
import hashlib
import shutil
from directories import Directories
from init import init
from store import *



def test():
    d = Directories()
    indices = []
    filenames = []
    count = 0;
    #for root, dirs, files in os.walk(d.objects, topdown=False):
     #   for name in files:
     #       print name
     #   for name in dirs:
     #       print name
    if os.path.exists(d.index) and os.path.isfile(d.index):
        # storing current hash values in a index file as a list
        indices = d.paths_in_index()
        # storing current filenames in the object folder as a list
        filenames = os.listdir(d.objects)
        sizeofIndex = len(indices)
        sizeofFiles = len(filenames)
        existFiles = {}
        errorPath = []
        if sizeofFiles> 0 or sizeofIndex>0:
            print "The size of index %d" % sizeofIndex
            print "The size of files in object folder %d" % sizeofFiles
            for n in indices:
                if indices.get(n) in filenames:
                    filenames.remove(indices.get(n))
                    existFiles[n] = indices.get(n)
                    count+=1
                else:
                    errorPath.append(n)
            print "Matching filenames: %d\n" %count
            print "Names of erroneous paths: "
            print '\n'.join(errorPath) + '\n'

        else:
            print "Index file doesn't exist"
            person = raw_input('Would you like to create the index file?: (y/n) ')
            if(person.lower() == 'y'):
                init()
                test()

        contentsWrong = []
        for file in existFiles:
            sig= createFileSignature(file)
            newhashvalue = sig[2]
            if newhashvalue not in existFiles.values():
                contentsWrong.append(sig[0])

        if len(contentsWrong) !=0:
            doesntmatch = [x[0] for x in contentsWrong]
            print "the names of objects that don't match their filename: "
            print '\n'.join(doesntmatch)
        else:
            print "All names of objects match their filename"





