import os
from directories import Directories

def get():
    d = Directories()

    print os.path.dirname(os.path.abspath(__file__))
    print os.getcwd()
    print d.myArchive
    print d.objects
    print d.index
