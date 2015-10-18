import os
import os.path
from logger import ArchiveLogger
from store import *

d = Directories()
log = ArchiveLogger()

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
                log.log_error("File does not exist: % s" % n)
                errors += 1

        m_paths = "%d Matching files" % matching_paths
        print m_paths
        log.log_info(m_paths)

        num_errors = "%d Errors" % errors
        print num_errors
        log.log_info(num_errors)
    else:
        log.log_error("Index file doesn't exist")


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
            log.log_error("%d file(s) hash values incorrect" % num_wrong)
        else:
            print "All hash values correct"
