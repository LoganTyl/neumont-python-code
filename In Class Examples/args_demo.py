import sys

# print(sys.argv)
# print(sys.argv[3])
# print()

import getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "a:b:c", ["add=", "delete="])
    # looks at index 1; short arguments use one dash, long arguments use two; 
    # short arguments with colons must have an argument afterwards
    # if argument given to non-colon, will be args, not c
except getopt.GetoptError:
    print("usage: py args_demo.py -a arg1 -b arg2 -c --add arg3 --delete arg4")
    sys.exit()

print(opts)
print(args)

