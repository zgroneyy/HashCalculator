#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 29 22:15:01 2021

@author: ozgur
    """
import os
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from tkinter import *
from hash_calc import get_digest
import hashlib
import sys 
  
content = ''
file_path = ''


#~~~~ FUNCTIONS~~~~

def open_file():
    global content
    global file_path
    global filename
    filename = askopenfilename()
    infile = open(filename, 'r')
    content = infile.read()
    file_path = os.path.dirname(filename)
    entry.delete(0, END)
    entry.insert(0, file_path)
    return content

def process_file(content):
    print(content)
    
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
  #~~~~~~~~~~~~~~~~~~~


  #~~~~~~ GUI ~~~~~~~~

root = Tk()
root.title('File Hash Calculator')
root.geometry("800x120+250+100")

mf = Frame(root)
mf.pack()


f1 = Frame(mf, width=600, height=250)
f1.pack(fill=X)
f2 = Frame(mf, width=600, height=250)
f2.pack()

file_path = StringVar


Label(f1,text="Select Your File").grid(row=0, column=0, sticky='e')
message = StringVar()
message.set('hi')
l1 = Label(f1,text="-")
l1.grid(row=1, column=0, sticky='e')
def press():
        l1.config(text=get_digest(filename))
        l1.grid(row=1, column=0, sticky='e')
entry = Entry(f1, width=50, textvariable=file_path)
entry.grid(row=0,column=1,padx=2,pady=2,sticky='we',columnspan=25)
Button(f1, text="Browse", command=open_file).grid(row=0, column=27, sticky='ew', padx=8, pady=4)
# Button(f2, text="Process Now", width=32, command=lambda: get_digest(filename)).grid(sticky='ew', padx=10, pady=10)
Button(f2, text="Process Now", width=32, command=press).grid(sticky='ew', padx=10, pady=10)



root.mainloop()



