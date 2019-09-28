with open('backup.log') as f:
    s = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    if (re.search(br'(?i)error', s)) or (re.search(br'(?i)notice', s)):
        backupLogHasErr = True    
