import os
import os.path

from store import *

d = Directories()


def test():
    test_index()
    print
    contentsMatch()



def test_index():
    print "Checking Index:"
    if os.path.exists(d.index) and os.path.isfile(d.index):
        # storing current hash values in a index file as a list
        indices = d.paths_in_index()
        # storing current filenames in the object folder as a list
        filenames = os.listdir(d.objects)

        matching_paths = 0
        errors = 0

        for n in indices:
            if indices.get(n) in filenames:
                matching_paths += 1
            else:
                print "File does not exist: % s" % n
                errors += 1

        print "%d Matching files" % matching_paths
        print "%d Errors" % errors
    else:
        print "Index file doesn't exist"


def contentsMatch():
        # print hash_vals
        print "Checking File Hash Values"
        num_wrong = 0

        for path in os.listdir(d.objects):
            fullpath = os.path.join(d.objects, path)
            if os.path.isfile(fullpath):
                actual_hash = createFileSignature(fullpath)[2]

                if path != actual_hash:
                    print "Error file: %s" % fullpath
                    num_wrong+=1

        if num_wrong !=0:
            print "%d file(s) incorrect" % num_wrong
        else:
            print "All hash values correct"
