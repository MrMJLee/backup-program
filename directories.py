import os
import os.path
import pickle


class Directories(object):
    """Directories is a class to store directory paths relevant
    to the backup program"""
    def __init__(self):
        super(Directories, self).__init__()
        #Define Archive Location
        self.program_name = "myArchive"
        self.user_dir = os.path.expanduser("~")
        self.my_archive = os.path.join(self.user_dir, self.program_name)
        self.objects = os.path.join(self.my_archive, "objects")
        self.index = os.path.join(self.my_archive, "INDEX")
        self.logger = os.path.join(self.my_archive, "backup.log")

    def check_myarchive(self):
        if os.path.exists(self.my_archive) and os.path.isdir(self.my_archive):
            return True
        else:
            return False

    def check_log_exists(self):
        if os.path.exists(self.logger) and os.path.isfile(self.logger):
            return True
        else:
            return False

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
