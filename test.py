import pickle
import os
import os.path
from directories import Directories
from init import init

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
        indices = d.paths_in_index().values()
          # storing current filenames in the object folder as a list
        filenames = os.listdir(d.objects)
        sizeofIndex = len(indices)
        sizeofFiles = len(filenames)

        errorPath = []
        if sizeofFiles> 0 or sizeofIndex>0:
            print "The size of index %d" % sizeofIndex
            print "The size of files in object folder %d" % sizeofFiles
            for n in indices:
                if n in filenames:
                    filenames.remove(n)
                    count+=1
                else:
                    errorPath.append(n)
            print "Matching filenames: %d" %count
            print "Names of erroneous paths: ",
            print ', '.join(errorPath)

    else:
        print "Index file doesn't exist"
        person = raw_input('Would you like to create the index file?: (y/n) ')
        if(person.lower() == 'y'):
            init()

    print "\n"





