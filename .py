import shutil
import os
import time

SECONDS_IN_DAY  = 24 * 60 * 60
src = 'C:/Users/hunte/OneDrive/Desktop/sFiles'

dst = 'C:/Users/hunte/OneDrive/Desktop/rFiles'

now = time.time()
before = now - SECONDS_IN_DAY

def time_since_dump(fname):
    return(os.path.getmtime(fname))

for fname in os.listdir(src):
    src_fname = os.path.join(src,fname)
    if time_since_dump(src_fname) > before:
        dst_fname = os.path.join(dst, fname)
        shutil.move(src_fname, dst_fname)
