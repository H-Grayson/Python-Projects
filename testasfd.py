


from tkinter import *

root = Tk()

def submitBody():
    body = bodytext.get()

bodytext = Entry(root).pack
subButton = Button(root, text= "sub body text", command=submitBody).pack()
