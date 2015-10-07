import os
import os.path
from directories import Directories


def init():
    #Define Archive Location
    d = Directories()

    # check if myArchive directory exists, create it if it doesn't
    if os.path.exists(d.myArchive) and os.path.isdir(d.myArchive):
        print "Archive Directory EXISTS\t %s" % d.myArchive
    else:
        print "Archive Directory CREATED\t %s" % d.myArchive
        os.makedirs(d.myArchive)

    # check if objects directory exists, create it if it doesn't
    if os.path.exists(d.objects) and os.path.isdir(d.objects):
        print "Objects Directory EXISTS\t %s" % d.objects
    else:
        print "Objects Directory CREATED\t %s" % d.objects
        os.makedirs(d.objects)

    # check if INDEX file exists, create it if it doesn't
    if os.path.exists(d.index) and os.path.isfile(d.index):
        print "INDEX file EXISTS\t\t %s" % d.index
    else:
        print "INDEX file CREATED\t\t %s" % d.index
        open(d.index,'w').close()
