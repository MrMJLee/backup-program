from directories import Directories

d =Directories()
# show what files are in the archive
def listfiles(searchArg=None):
    if searchArg == None:
        print "All Files"
    else:
        print "Files Matching %s:" % searchArg

    paths = d.paths_in_index()
    for x in paths:
        if searchArg == None or searchArg in x:
            print x