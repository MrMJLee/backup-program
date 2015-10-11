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
    count = 0;
    if os.path.exists(d.index) and os.path.isfile(d.index):
        # storing current hash values in a index file as a list
        indices = d.paths_in_index()
        # storing current filenames in the object folder as a list
        filenames = os.listdir(d.objects)
        sizeofIndex = len(indices)
        sizeofFiles = len(filenames)
        # matching files
        existFiles = {}
        # the names of any erroneous paths that don't have matching files
        errorPath = []
        if sizeofFiles> 0 or sizeofIndex>0:
            print "The size of index %d" % sizeofIndex
            print "The size of files in object folder %d" % sizeofFiles
            for n in indices:
                if indices.get(n) in filenames:
                    #filenames.remove(indices.get(n))
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
    contentsMatch(existFiles)


def contentsMatch(existFiles,objectPath):
        contentsWrong = []
        newhashvalue = []
        for file in existFiles:
            if os.path.isfile(file):
                sig= createFileSignature(file)
                newhashvalue = sig[2]
                print sig
        print newhashvalue
        for newhash in newhashvalue:
            if newhash not in existFiles.values():
                contentsWrong.append(sig[0])


             #if os.path.isdir(file):
             #   contentsMatch(file)
        if len(contentsWrong) !=0:
            doesntmatch = [x for x in contentsWrong]
            print "The names of objects that don't match their filename: "
            print '\n'.join(doesntmatch)
        else:
            print "All names of objects match their filename"





