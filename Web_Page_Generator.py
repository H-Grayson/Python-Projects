import tkinter
from tkinter import *
import webbrowser

root = Tk()

def bodyCust():
    x = bodyText.get()
    f = open('web_page.html', 'w')
    f.write('<html>\n<body>\n<h1>\n{}\n</h1>\n</body>\n</html>'.format(x))
    f.close()
    webbrowser.open('web_page.html', new=0, autoraise=True)


bodyText = Entry(root)
button1 = Button(root, text="Submit Body", command=bodyCust)


button1.pack()
bodyText.pack()
