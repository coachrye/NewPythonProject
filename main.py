import sys
import os
import errno

MYPATH = "/Users/coachrye/Documents/TheHub/coachrye/"
MY_COMMAND = "touch README.md"
# Uncomment Once Game Time
# if len(sys.argv) > 1:
#     project_name = sys.argv[1]
project_name = "ThisIsMyTestProject"

try:
    os.chdir(MYPATH)
    os.makedirs(project_name)
    os.chdir(MYPATH + project_name)
    os.system(MY_COMMAND)
    
except OSError as e:
    print("folder exists, dude!")
    if e.errno != errno.EEXIST:
        print("something else, dude!")
        raise
