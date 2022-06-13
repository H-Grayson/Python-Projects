import os
import time
import shutil
from tkinter import filedialog
from tkinter import *

root = Tk()

sec_in_day = 24*60*60

def src_sbutton():
    filename = filedialog.askdirectory()
    print(filename)
    return filename

def target_sbutton():
    filename = filedialog.askdirectory()
    print(filename)
    return filename

src_searchbtn = Button(root, text = "Choose your working directory" )

target_searchbtn = Button(root, text = "Choose the target directory", command = target_sbutton())

src_path = "."

target_path = "../"

  


for filename in os.listdir(src_path):
    if os.path.getmtime(filename) >= (time.time() - sec_in_day): 
        shutil.move(os.path.join(src_path, filename), target_path)  


src_searchbtn.pack()
target_searchbtn.pack()
