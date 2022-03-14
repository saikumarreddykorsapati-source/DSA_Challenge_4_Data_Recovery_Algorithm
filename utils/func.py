from tkinter import *
from tkinter import filedialog
import os
import sys


def browseFiles():
    filepath = filedialog.askopenfilename(initialdir = os.getcwd()+"/assets/", title = "Select a File to perform compression",filetypes = (("all files", "*.*"), ("all files","*.*")))
    if filepath=="":
        sys.exit("\nNo file selected from opened pop up window")
    file = os.path.basename(filepath).split("/")[-1]
    filename = file.split(".")[0]
    # for i in ext:
    #    ext = filename.split(".")[-1]

    print("\nChoosen Input File Path : " + filepath)
    print("\t\n--> Choosen Input File Name : " + filename,end="\n\n")
    # print("\t--> Original File Format : "+ ext,end="\n\n")
    return filepath,filename#,ext

window = Tk()
button_explore = Button(window,text = "Browse Files", command = browseFiles)
window.withdraw()    