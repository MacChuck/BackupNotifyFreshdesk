import os,time,sys,datetime,re
import mmap

backupLogHasErr = False

with open('backup.log', 'rb', 0) as file, \
    mmap.mmap(file.fileno(), 0, access=mmap.ACCESS_READ) as s:
    if (re.search(br'(?i)error', s)) or (re.search(br'(?i)notice', s)):
        backupLogHasErr = True

if backupLogHasErr:
    print("Found Notice or Error in log file")
