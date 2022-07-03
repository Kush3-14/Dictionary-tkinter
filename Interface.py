
from random import randrange
from tkinter import *
from os import getcwd
import json
from difflib import get_close_matches
from tkinter import messagebox




def clearFrame(frame):
    for f in frame.winfo_children():
        f.destroy()

def createEditText(master, **kwargs):
    return Entry(master=master, **kwargs)

def createFrame(master, **kwargs):
    return Frame(master=master, **kwargs)

def createButton(master, **kwargs):
    return Button(master, **kwargs)

def createLabel(master, **kwargs):
    return Label(master, **kwargs)

def displayResult(words):
    clearFrame(display_frame)
    for word in words:
        createLabel(display_frame, text=str(word).strip("[]"), font=("Helvetica 10 bold"), bg='Aquamarine').pack(anchor=W, padx=50)
    display_frame.pack(fill=X, pady=20, padx=20)

def main():
    frame = createFrame(root, bg='Cyan')
    createLabel(frame, text="Enter Word", font=("Helvetica 15 bold")).pack(side=LEFT, padx=5, pady=5)
    # create Entry text
    word_given = createEditText(frame, font=("Helvetica 13 bold"))
    word_given.pack(side=LEFT, padx=5, pady=5, fill=X, expand=True)
    # create save Button
    createButton(frame, text = "Define", command = lambda:define(word_given)).pack(side=RIGHT, padx=5)
    #add everything to frame
    frame.pack(fill=X, pady=20, padx=20)

def define(word_given):
    global error_label
    word=word_given.get()   

    # check if error_label is been initialized
    if error_label is not None: error_label.destroy()
    if word in data:
        # display dictionary result
        displayResult(data[word])
    elif word.title() in data: 
        displayResult(data[word.title()])
    elif word.upper() in data: 
        displayResult(data[word.upper()])
    elif len(get_close_matches(word, data.keys()))>0:
        #get closest word match list
        matches = get_close_matches(word, data.keys())
        # randomly choose from the list
        match = matches[randrange(len(matches))]
        choice = messagebox.askquestion("Ask Question","Did you mean %s instead?"%match)
        if choice=="yes":
            displayResult(data[match])
        elif choice=="no":
            error_label = createLabel(root, text="Word not found! Please re-check it.", pady=20, bg='orange')
            error_label.pack()
        else:
            error_label = createLabel(root, text="I didn't understand your word.", pady=20, bg='lime')
            error_label.pack()
    else:
        error_label = createLabel(root, text="Word not found! Please re-check it.", pady=20, bg='red')
        error_label.pack()

root = Tk()
root.title("Dictionary")
root.geometry('1090x600')
root['bg']="gold"
data = json.load(open(getcwd()+'\data.json','r'))
display_frame = createFrame(root, bg='Aquamarine')
error_label = None
main()
root.mainloop()
