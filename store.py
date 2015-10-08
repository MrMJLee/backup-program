import pickle
import os
import os.path
import shutil

from hashfile import createFileSignature
from directories import Directories


# add the specified directory to the archive
d = Directories()


def store(directory):
    # directory_path = d.path(directory)
    directory_path = directory
    indices = d.paths_in_index()

    # print indices

    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        print "Backing up %s" % directory_path
        indices.update(store_files_in_dir(directory_path))
        pickle.dump(indices, open(d.index, "wb"))
    else:
        print "Directory %s does not exist!" % directory_path


# return the hash values of files in given directory
def store_files_in_dir(directory_path):
    names = os.listdir(directory_path)

    signatures = {}

    for n in names:
        fullpath = os.path.join(directory_path, n)
        if os.path.isfile(fullpath):
            # print fullpath
            sig = createFileSignature(fullpath)
            hashValue = sig[2]

            signatures[fullpath] = hashValue
            hashFullpath = os.path.join(d.objects, hashValue)

            if os.path.exists(hashFullpath):
                print "%s backup EXISTS" % fullpath
            else:
                print "%s backed CREATED" % fullpath
                shutil.copyfile(fullpath, hashFullpath)
        elif os.path.isdir(fullpath):
            signatures.update(store_files_in_dir(fullpath))
    return signatures
