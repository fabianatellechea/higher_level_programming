#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1

    if argc == 0:
        print("0 arguments.")
    if argc == 1:
        print("{} argument:".format(argc))
        print("{}: {}".format(argc, sys.argv[1]))
    elif argc > 1:
        print("{} arguments:".format(argc))
        for arg in range(len(sys.argv[1:])):
            print("{}: {}".format(arg + 1, sys.argv[1:][arg]))
