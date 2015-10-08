import os
import os.path
import pickle


class Directories(object):
    """Directories is a class to store directory paths relevant
    to the backup program"""
    def __init__(self):
        super(Directories, self).__init__()
        #Define Archive Location
        self.userDir = os.path.expanduser("~")
        self.myArchive = os.path.join(self.userDir, "myArchive")
        self.objects = os.path.join(self.myArchive, "objects")
        self.index = os.path.join(self.myArchive, "INDEX")
    def path(self, path):
        return os.path.join(self.userDir, path)

    def paths(self, paths):
        path = self.userDir

        for d in paths:
            path = os.path.join(path, d)

        return path

    def paths_in_index(self):
        indices = {}
        if not self.__index_empty():
            indices = pickle.load(open(self.index, "rb"))
        return indices

    def __index_empty(self):
        try:
            if os.path.getsize(self.index) > 0:
                return False
            else:
                return True
        except OSError, e:
            return True
