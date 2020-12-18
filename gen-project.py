import sys
import os
import subprocess
import shutil
if len(sys.argv) <= 1:
    print('Usage: python gen-project.py [Project Name]')
    exit()
else:
    projname=sys.argv[1]
shutil.copytree('/Users/sochigusa/works/Project-Skeleton/tmp-proj', '/Users/SoChigusa/works/'+projname)
os.chdir('/Users/SoChigusa/works/'+projname)
subprocess.run(['git','init'])
subprocess.run(['git','add','*'])
subprocess.run(['git','commit','-a','-m','"First commit"'])
