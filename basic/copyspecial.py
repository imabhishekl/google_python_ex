#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import os
import shutil
import commands

"""Copy Special exercise
"""


# +++your code here+++
# Write functions and modify main() to call them
def get_special_paths(dirs):
    final_res=[]
    for list in os.listdir(dirs):
        res=re.search(r"__(\w+)__",list)
        if res:
            final_res.append(os.path.abspath(os.path.join(dirs,list)))
    return final_res

def copy_to(paths,dir):
    if not os.path.exists(dir):
        os.mkdir(dir)

    for path in paths:
        shutil.copy(path,os.path.join(dir,os.path.basename(path)))

def zip_to(paths, zippath):
    cmd="zip -j " + zippath + " "

    for path in paths:
        cmd += path + " "
    print cmd
    #os.system(cmd)
    status,op = commands.getstatusoutput(cmd)

    if status:
        sys.stderr.write(op)
        return

def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print "usage: [--todir dir][--tozip zipfile] dir [dir ...]";
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]

    tozip = ''
    if args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]

    if len(args) == 0:
        print "error: must specify one or more dirs"
        sys.exit(1)

    final_list = []
    for dirlist in args:
        final_list.extend(get_special_paths(dirlist))

    if todir:
        copy_to(final_list,todir)
    elif tozip:
        zip_to(final_list,tozip)
    else:
        print '\n'.join(final_list)

if __name__ == "__main__":
    main()