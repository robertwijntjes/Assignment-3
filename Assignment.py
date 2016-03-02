import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

modulelist = ["Chinese","OOP","Operating Systems","Data Communications","SFGM","Alorithms"]
member_list = ['c14356786']
password_list = ['password']
dropped_module_list = []

class Welcome( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.master.title("Welcome Menu")
        self.configure(background='#00b7ea')
        self.pack()
        self.make_gui()
        """ logo """

    def make_gui(self):
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
        quitButton = Button(self,text = "Quit", bg = '#FFFFFF' , command = self.quit_button)
        self.quitButton.grid( row = 8, column = 3, columnspan = 1, sticky = W+E+N+S )
        confirmButton = Button(self,text = "Login", bg = '#FFFFFF',command = lambda : self.input_check(self.name.get(),self.password.get()))
        self.confirmButton.grid( row = 8, column = 2, columnspan = 1, sticky = W+E+N+S )
        

    def quit_button(self):
        exit()

    def input_check(self,name,password):
        for item in member_list:
            if(name == item ):
                for item in password_list:
                    if(password == item):
                        Main_Menu()
                    else:
                        print ("Incorrect Password")

            else:
                print ("Incorrect Username")

                



        
class Main_Menu(Frame):     
    def __init__(self):
        new = Tk()
        new.title("Webcourses")
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


    def drop_module():
        pass

    def add_module():
        pass
         

    def close_window(self):
        pass

class Error_Box(Frame):     
    def __init__(self):
        tk.Frame.__init__(self)
        self.master.title("Error")
        self.pack()
        w = 250
        h = 100
        x = 50
        y = 100
        self.error_msg = Label(self, text = "Incorrect Username/Password Submission")
        self.error_msg.grid( row = 2, column = 1, columnspan = 1, sticky = W+E+N+S )
        self.button = Button(self, text = "Ok")
        self.button.grid(row = 3, column = 1 , columnspan = 1, sticky = W+E+N+S )
        
        
        

        


def main(): 
    """Welcome().mainloop()"""
    Error_Box().mainloop()

if __name__ == '__main__':
    main()
