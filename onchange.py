#!/usr/bin/python

import subprocess
import sys
import time

CHECK_INTERVAL_SECONDS = 1.0

def executeOnChangeAction(action):
    subprocess.Popen(action, shell=True).wait()

def getMd5Sum(filelistgen):
    cmd = subprocess.Popen(
    	'%s|sort|xargs cat|md5sum -|awk \'{print $1}\'' % filelistgen,
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
