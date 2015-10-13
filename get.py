import shutil
import os
from directories import Directories

d = Directories()
def get(pattern):
    paths = d.paths_in_index()
    results = []
    selection = None

    for path in paths:
        if pattern in path:
            results.append(path)

    if len(results) == 0:
        print "\nNo Match"
    elif len(results) == 1:
        selection = results[0]
    else:

        values = [results[x:x + 50] for x in xrange(0, len(results), 50)]
        #print values
        # list each set of fifty results and prompt the user to select a file
        for res in values:
            selection = select_from_list(res)
            if selection == None:
                print "\nInvalid Inputs" # catching invalid inputs and break.
                break

    if selection!= None:
        copy_file(os.path.join(d.objects, paths[selection]), os.path.split(selection)[-1])

# selection from user
def select_from_list(results):
    for path in list(enumerate(results, 1)):
        print "%d:\t%s" % path
    try:
        path_select = int(raw_input("Select File Number:"))
        selection = results[path_select - 1]
        print selection
        return selection

    except (IndexError, ValueError):
        return None

# copy file
def copy_file(tosave, dest):
    if os.path.exists(dest) and not os.path.isdir(dest):
        ask = raw_input("%s already exists, Overwrite? (y/n) " % dest)
        if ask.lower() != 'y':
            return None
    shutil.copyfile(tosave, dest)
    print dest + " saved successfully\n"
