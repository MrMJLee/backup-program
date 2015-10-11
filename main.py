import time, sys
from hashfile import createFileSignature
from init import init
from store import store
from listfiles import listfiles
from test import test
from get import get
from restore import restore
from sys import argv
from log import loggerModule

def main():
    # print sys.argv
    if len(argv) >= 2:
        cmd = argv[1].lower()
        if cmd == "init":
            init()
            loggerModule()

        elif cmd == "store":
            if len(argv) >= 3:
                store(argv[2])
            else:
                print "No directory specified for store function"
        elif cmd == "list":
            if len(argv) >= 3:
                listfiles(argv[2])
            else:
                listfiles()
        elif cmd == "restore":
            if len(argv) >=3:
                restore(argv[2])
            else:
                restore()
        elif cmd == "test":
            test()
        elif cmd == "get":
            if len(argv) >= 3:
                get(argv[2])
    else:
        print "No arguments!"


if __name__ == '__main__':
    main()