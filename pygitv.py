#!/usr/bin/env python3

import subprocess

result = subprocess.run(['git', 'log','-1', '--pretty=%B'], capture_output=True, text=True)
last_commit_message = result.stdout.strip()
print(last_commit_message)
if('-' in last_commit_message):
    
    version=last_commit_message.split('-')[0]
    version=version.replace('v','')
else:
    version='0.0'

version=version.strip()

print(version)