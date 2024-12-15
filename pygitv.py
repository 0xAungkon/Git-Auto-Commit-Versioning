#!/usr/bin/env python3

import subprocess
import sys

def return_next_version():
    result = subprocess.run(['git', 'log','-1', '--pretty=%B'], capture_output=True, text=True)
    last_commit_message = result.stdout.strip()
    if('-' in last_commit_message):
        
        version=last_commit_message.split('-')[0]
        version=version.replace('v','')
    else:
        version='0.0'

    version=version.strip()

    try:
        version=float(version)
    except ValueError:
        version=0.0

    version=str(version)
    try:
        is_asked_for_next_v=sys.argv[1]
    except:
        is_asked_for_next_v=False
    if(is_asked_for_next_v=='-rel'):
        version_pre=int(version.split('.')[0])+1
        version_post=int(version.split('.')[1])
    else:
        version_pre=int(version.split('.')[0])
        version_post=int(version.split('.')[1])+1
    version=str(version_pre)+'.'+str(version_post)
    return version

commit_msg=input('Enter Commit Message: ')
version=return_next_version()
commit_msg=version+' - '+commit_msg
subprocess.run(['git', 'add', '.'])
subprocess.run(['git', 'commit', '-m', commit_msg])
print(commit_msg)