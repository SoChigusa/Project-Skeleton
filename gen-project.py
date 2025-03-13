import sys
import os
import subprocess
import shutil
if len(sys.argv) <= 1:
    print('Usage: python gen-project.py [Project Name]')
    exit()
else:
    projname=sys.argv[1]

sys_os = sys.platform
if sys_os == 'darwin':
    work_dir = '/Users/SoChigusa/works'
elif sys_os == 'linux' or sys_os == 'linux2':
    work_dir = '/home/sochigusa/works'
else:
    print('MacOS X / Linux is expected')
    exit()

shutil.copytree(work_dir+'/Project-Skeleton/tmp-proj', work_dir+'/'+projname)
os.chdir(work_dir+'/'+projname)
subprocess.run(['git','init'])
subprocess.run(['git','add','*'])
subprocess.run(['git','commit','-a','-m','"First commit"'])
