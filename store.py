import pickle
import os
import os.path
import shutil
from logger import ArchiveLogger
from hashfile import createFileSignature
from directories import Directories


# add the specified directory to the archive
d = Directories()
log = ArchiveLogger()


def store(directory):
    # directory_path = d.path(directory)
    directory_path = directory
    indices = d.paths_in_index()

    # print indices

    if os.path.exists(directory_path) and os.path.isdir(directory_path):
        print "Backing up %s" % directory_path
        indices.update(store_files_in_dir(directory_path))
        try:
            pickle.dump(indices, open(d.index, "wb"))
            log.log_info("Index Updated")
        except:
            log.log_error("Index save not successful")
    else:
        log.log_error("Directory %s does not exist!" % directory_path)


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
                try:
                    shutil.copyfile(fullpath, hashFullpath)
                    log.log_info("File %s Copied to %s" % (fullpath, hashFullpath))
                except:
                    log.log_error("File %s copy failed" % fullpath)

        elif os.path.isdir(fullpath):
            signatures.update(store_files_in_dir(fullpath))
    return signatures
