#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 22:15:01 2021
@descrpt: Select a file, return hash of it. Guarantee integrity of the file. 
@author: ozgur oney
    """
import os
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter.messagebox import showinfo
import hashlib
import sys 
  
content = ''
file_path = ''
filename = ''
#define base
root = Tk()
root.title('File Hash Calculator')
root.geometry("620x150")
root.resizable(0, 0)

#operation when you browse
def open_file():
    global content
    global file_path
    global filename
    filename = askopenfilename()
    file_path = os.path.dirname(filename)
    entry.delete(0, END)
    entry.insert(0, file_path)
    return file_path
#calculate hash of the file
def get_digest(file_path):
    h = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            # Reading is buffered, so we can read smaller chunks.
            chunk = file.read(h.block_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()
#print the hash calculated to the label, if file is properly selected of course.
def press():
    output.delete('1.0', END)
    if (len(file_path)!=0):
        output.insert(END, str(get_digest(filename)))

#pop-up message to warn user to select file
def message():
	if len(file_path)==0:
		showinfo("Message", f"Select file to apply hashing!") 

#when Process button is pressed, we have to do 2 jobs together, so we need a combiner
def combine_funcs(*funcs):
    def combined_func(*args, **kwargs):
        for f in funcs:
            f(*args, **kwargs)
    return combined_func

mf = Frame(root)
mf.pack()

#frames
f1 = Frame(mf, width=450, height=200)
f1.pack(fill=X)
f2 = Frame(mf, width=450, height=200)
f2.pack()
#labels, entry and buttons
l0 = Label(f1,text="Select Your File:")
l0.grid(row = 1, column = 0, sticky = W, padx=5,)
l0.columnconfigure(0, weight=1)
entry = Entry(f1, width=50, textvariable=file_path)
entry.grid(row=2,column=0,sticky=W,columnspan=2, padx=5)
but1 = Button(f1, text="Browse", bg='#40e0d0')
but1.grid(row=2, column=1, sticky=W)
l1 = Label(f1,text="Your hash is:\t", width=12, anchor='w')
l1.grid(row = 4, column = 0, sticky = W)
output = Text(f1, width=75, height=1)
output.grid(row=5, column=0, columnspan=2, padx=5, pady=(0,10))
but2 = Button(f1, text="Process Now", bg='#40e0d0')
but2.grid(row=6, column=0, columnspan=2)
# button clicks
but1.configure(command=open_file)
but2.configure(command=combine_funcs(press, message))
#end
root.mainloop()



