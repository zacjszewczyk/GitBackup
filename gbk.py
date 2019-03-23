#!/usr/bin/python

from sys import exit, argv
from os.path import isdir
from os import chdir, devnull
import subprocess
from time import sleep

# Make sure the user entered a parameter
if (len(argv) <= 1):
    print "Provide a directory."
    sys.exit(1)

target = argv[1]

# Make sure that parameter is a directory
if (not isdir(target)):
    print "Provide a valid directory."
    exit(1)

# Change the working directory
chdir(target)

# We don't want to view the output of most
# of these commands, so set up a pipe to
# /dev/null that we can write the output to
FNULL = open(devnull, 'w')

# Check for git repository in the directory
code = subprocess.call("git status", stdout=FNULL, stderr=FNULL, shell=True)

if (code != 0):
    print "Target a directory with an existing git repo."
    exit(1)

# Now we have a valid target directory, with
# an established git repo. Start monitoring it
while True:
    # Run the "git status" command
    output = subprocess.check_output("git status", shell=True)
    
    # If there are changes to the repo not yet
    # staged for commit, stage and commit them
    if ("Changes not staged for commit" in output):
        code = subprocess.call(["git add .; git commit -m \""+output[output.find("modified:"):].split("\n")[0]+"\""], stdout=FNULL, stderr=FNULL, shell=True)
        if (code != 0):
            print "ERROR staging commit, see repo at ",target
            exit(1)
        code = subprocess.call(["git push"], stdout=FNULL, stderr=FNULL shell=True)
        if (code != 0):
            print "ERROR pushing commit, see repo at ",target
            exit(1)
    sleep(1)

FNULL.close()