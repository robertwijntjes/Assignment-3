from tkinter import *
from PIL import Image, ImageTk


modulelist = ["Chinese","OOP","Operating Systems","Data Communications","SFGM","Alorithms"]
dropped_module_list = []

def main():
    """root = Tk()"""
    w_root = Tk()
    welcome_root(w_root)
    """gui_init(root)"""
    #w_root.mainloop()
    #root.mainloop()

def gui_init(root):
    """ Main Frame """
    w = 500
    h = 500
    x = 50
    y = 100
    root.geometry("%dx%d+%d+%d" % (w,h,x,y))
    root.title('WebCourses')
    """ Logo """
    load = Image.open("webcourses.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(root,image = render)
    img.image = render
    img.place(x=0,y=0)
    """ Modules List """
    """ Current Modules """
    listbox = Listbox(root)
    listbox.insert(END)
    for item in modulelist:
        listbox.insert(END,item)
    listbox.place(x=5,y=100)
    lb = Listbox(root)
    """ Dropped Modules """
    listbox_drop = Listbox(root)
    for item in dropped_module_list:
        listbox_drop.insert(END,item)
    listbox_drop.place(x=5,y=275)

def welcome_root(root):
    """ Welcome Interface """
    root.title("Welcome Menu")
    w = 300
    h = 300
    x = 50
    y = 100
    root.geometry("%dx%d+%d+%d" % (w,h,x,y))
    """ Logo """
    load = Image.open("welcome.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(root,image = render)
    img.image = render
    img.place(x=0,y=0)
    """ Entry Details """
    n_label = Label(root,text = "Username")
    n_label.place(x=80,y=150)
    p_label = Label(root,text = "Password")
    p_label.place(x=80,y=170)
    cs_label = Label(root,text = "Passwords are Case Sensitive",font = ("Purisa",7))
    cs_label.place(x=150,y=190)
    name = Entry(root)
    name.place(x=150,y=150)
    password = Entry(root,show = "*")
    password.place(x=150,y=170)

    


    
    
main()




