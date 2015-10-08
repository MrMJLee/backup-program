from directories import Directories

d =Directories()
# show what files are in the archive
def listfiles(searchArg=None):
    if searchArg == None:
        print "All Files"
    else:
        print "Files Matching %s:" % searchArg

    indices = d.indices()
    for x in indices:
        if searchArg == None or searchArg in x:
            print x