import shutil
import os
import tkinter
from tkinter import *

root = Tk()

def fileDumpFind():
    fileFrom = shutil.which(root)
    src = fileFrom
    print(src)
    fileTo = shutil.which(root)
    dst = fileTo
    files = os.listdir(source)

    for i in files:
        shutil.move(fileFrom+i, fileTo)



fileFrom = Button(root, text='Choose a folder to be scanned daily.')
fileTo = Button(root, text='Choose a folder to receive the copied files.')
fcToggle = Button(root, text='Toggle File check on and off')


fileFrom.pack()
fileTo.pack()
fcToggle.pack()
