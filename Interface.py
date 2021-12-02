from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox


    
root = Tk()
root.title("Dictionary")
root.geometry('1090x600')
root['bg']="gold"

data = json.load(open('E:\Coding\PythonProjects\Dictionary\data.json','r'))

def define():
    word=word_given.get()    
    if word in data:
        Label(root, text=data[word], pady=20, bg='Aquamarine').pack()
    elif word.title() in data: 
        Label(root, text=str(data[word.title()]), pady=20, bg='Aquamarine').pack()
    elif word.upper() in data: 
        Label(root, text=str(data[word.upper()]), pady=20, bg='Aquamarine').pack()
    elif len(get_close_matches(word, data.keys()))>0:
        choice= messagebox.askquestion("Ask Question","Did you mean %s instead?"%get_close_matches(word, data.keys())[0])
        if choice=="yes":
            Label(root, text=data[get_close_matches(word, data.keys())[0]], pady=20, bg='Aquamarine').pack()
        elif choice=="no":
            Label(root, text="Word not found! Please re-check it.", pady=20, bg='Aquamarine').pack()
        else:
            Label(root, text="I didn't understand your word.", pady=20, bg='Aquamarine').pack()
    else:
        Label(root, text="Word not found! Please re-check it.", pady=20, bg='Aquamarine').pack()

frame = Frame(root,bg='Cyan')
Label(frame, text="Type Word", font=("Helvetica 15 bold"),bg='Olive').pack(side=LEFT)
word_given = Entry(frame, font=("Helvetica 15 bold"),width="50")
word_given.pack(pady=100)
frame.pack(pady=10)

# Button Creation

printButton = Button(root,text = "Define", command = define)
printButton.pack(padx=20,pady=20)
  

root.mainloop()