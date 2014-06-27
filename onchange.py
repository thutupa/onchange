#!/usr/bin/python

import subprocess
import sys
import time
import os.path

CHECK_INTERVAL_SECONDS = 1.0

def executeOnChangeAction(action):
    subprocess.Popen(action, shell=True).wait()

MD5COMMAND = None
def getMd5Command():
    global MD5COMMAND
    if not MD5COMMAND:
        if subprocess.Popen('md5 < /dev/null > /dev/null 2>&1', shell=True).wait() == 0:
            MD5COMMAND = 'md5'
        else:
            MD5COMMAND = 'md5sum -'
    return MD5COMMAND

def getMd5Sum(filelistgen):
    if os.path.exists(filelistgen):
        if os.path.isdir(filelistgen):
            filelistgen = 'find %s -type f' % filelistgen
        else:
            filelistgen = 'echo ' + filelistgen

    cmd = subprocess.Popen(
    	('%s|sort|xargs cat| ' + getMd5Command() + ' |awk \'{print $1}\'') % filelistgen,
	shell=True, stdout=subprocess.PIPE)
    md5sum = cmd.stdout.read().strip()
    assert cmd.wait() == 0
    return md5sum

def main():
    action = ' '.join(sys.argv[2:])
    md5sum = ''
    while True:
        newMd5Sum = getMd5Sum(sys.argv[1])
        if md5sum == newMd5Sum:
            time.sleep(CHECK_INTERVAL_SECONDS)
        else:
            executeOnChangeAction(action)
            md5sum = newMd5Sum

if __name__ == '__main__':
    main()
