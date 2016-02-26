import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

modulelist = ["Chinese","OOP","Operating Systems","Data Communications","SFGM","Alorithms"]
dropped_module_list = []

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
        self.newWindow = Main_Menu()

        
class Main_Menu(Frame):     
    def __init__(self):
        new = Tk()
        new.title("Welcome" """ Entered name goes here """)
        new.configure(background = '#00b7ea')
        w = 500
        h = 500
        x = 50
        y = 100
        new.geometry("%dx%d+%d+%d" % (w,h,x,y))
        """ Modules List """
        """ Current Modules """
        listbox = Listbox(new)
        listbox.insert(END)
        for item in modulelist:
            listbox.insert(END,item)
        listbox.place(x=5,y=100)
        lb = Listbox(new)
        """ Dropped Modules """
        listbox_drop = Listbox(new)
        for item in dropped_module_list:
            listbox_drop.insert(END,item)
        listbox_drop.place(x=5,y=275)

        
        

        

    def close_window(self):
        pass
def main(): 
    Welcome().mainloop()

if __name__ == '__main__':
    main()
