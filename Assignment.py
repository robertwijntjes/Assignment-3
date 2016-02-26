import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Welcome( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.master.title("Welcome Menu")
        self.configure(background='#00b7ea')
        self.pack()
        """ logo """
        load = Image.open("welcome.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self,image = render)
        img.image = render
        img.grid( row = 0, column = 0, columnspan = 2, sticky = W+E+N+S )
        """ Details """
        self.n_label = Label(self,text = "Username", bg = '#00b7ea')
        self.n_label.grid( row = 5, column = 0, columnspan = 2, sticky = W+E+N+S )
        self.p_label = Label(self,text = "Password", bg = '#00b7ea')
        self.p_label.grid( row = 6, column = 0, columnspan = 2, sticky = W+E+N+S )
        self.cs_label = Label(self,text = "*Passwords are Case Sensitive",font = ("Purisa",7), bg = '#00b7ea')
        self.cs_label.grid( row = 7, column = 2, columnspan = 2, sticky = W+E+N+S )
        self.name = Entry(self)
        self.name.grid( row = 5, column = 2, columnspan = 2, sticky = W+E+N+S )
        self.password = Entry(self,show = "*")
        self.password.grid( row = 6, column = 2, columnspan = 2, sticky = W+E+N+S )
        quitButton = Button(self,text = "Quit", bg = '#FFFFFF',command = self.close_window)
        quitButton.grid( row = 8, column = 3, columnspan = 1, sticky = W+E+N+S )
        confirmButton = Button(self,text = "Confirm", bg = '#FFFFFF', command = self.confirm_window )
        confirmButton.grid( row = 8, column = 2, columnspan = 1, sticky = W+E+N+S )

    def close_window(self):
        exit()

    def confirm_window(self):
        newWindow = Main_Menu()

        
class Main_Menu(Frame):     
    def __init__(self):
        root = Tk()
        

    def close_window(self):
        pass
def main(): 
    Welcome().mainloop()

if __name__ == '__main__':
    main()
