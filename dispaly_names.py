# -*- coding: utf-8 -*-
"""
A little application for displaying a list of character strings,
cycling through them randomly, and closing when all strings
have been displayed on the screen. I made this originally to cycle 
through students' names, hence the class name Display_Names
"""

from random import shuffle
from Tkinter import *
from ttk import Frame


class Display_Names(Frame):
    def __init__(self, parent, names):
        Frame.__init__(self, parent)
        self.parent = parent
        shuffle(names)
        self.names = names
        self.create_myButton()
        self.create_myLabel()
        
    def create_myLabel(self):
        self.myLabel = Label(self.parent,text=self.names[0], font=("Pursia",24))
        self.myLabel.place(anchor=CENTER,relx=.5, rely=.2) 

    def create_myButton(self):
        self.myButton = Button(self.parent,text="NEXT", font=("Pursia", 16),
                               command= self.myButton_command)
        self.myButton.place(anchor=CENTER,relx=.5, rely=.5) 
       
    def myButton_command(self):
        self.myLabel.destroy()
        self.myButton.destroy()
        del self.names[0]
        if len(self.names)==0:
            self.parent.destroy()
        else:
            self.create_myLabel()
            self.create_myButton()

def main(names):
    root = Tk()
    root.geometry('400x400')
    app = Display_Names(root, names)
    root.mainloop()

if __name__ == "__main__":
    names = ['Carol', 'Richard', 'Betty', 'Robert']
    main(names)
