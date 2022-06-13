import shutil
import os
import time
from tkinter import *
from tkinter.filedialog import askdirectory

root = Tk()
SECONDS_IN_DAY  = 24 * 60 * 60
src = ""
dst = ""

def pathing():
    path = askdirectory(title='Select Folder') # shows dialog box and return the path
    print(path)
    
def time_since_dump(fname):
    return(os.path.getmtime(fname))


def copy_callback(from_, to, ):
    copy()

        


now = time.time()
before = now - SECONDS_IN_DAY

button1= Button(root, text="Choose your working Directory")

button1.pack()

