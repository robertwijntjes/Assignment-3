import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

modulelist = []
member_list = ['c14356786']
password_list = ['password']
language_english = ['Username','Password','New Account','Login','Quit','*Passwords are Case Sensitive']
language_chinese = ['用户名','密码','新账户','登录','出口','密码区分大小写']
dropped_module_list = []
check = 0
lan_bool = True

User_id = ['holder']

class Welcome( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.master.title("Welcome Menu")
        self.configure(background='#00b7ea')
        self.master.resizable(width = FALSE,height = FALSE)
        self.pack()
        self.make_gui()
        """ logo """

    def make_gui(self):
        counter = 0
        n_account = tk.StringVar()
        user_a = tk.StringVar()
        pass_a = tk.StringVar()
        login_a = tk.StringVar()
        quit_a = tk.StringVar()
        case_a = tk.StringVar()
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
        self.quitButton = Button(self,text = "Quit", bg = '#FFFFFF' , command = self.quit_button)
        self.quitButton.grid( row = 8, column = 3, columnspan = 1, sticky = W+E+N+S )
        self.confirmButton = Button(self,text = "Login", bg = '#FFFFFF',command = lambda : self.input_check(self.name.get(),self.password.get(),counter))
        self.confirmButton.grid( row = 8, column = 2, columnspan = 1, sticky = W+E+N+S )
        self.new_account_button = Button(self, textvariable = n_account, bg = '#FFFFFF' ,command = lambda : self.new_account(self.name.get(),self.password.get(),counter ))
        self.new_account_button.grid( row = 8, column = 0, columnspan = 2, sticky = W+E+N+S )
        self.lan_button = Button(self,text = "ENG", command = lambda : self.alt_language(case_a,quit_a,login_a,pass_a,user_a,n_account) )
        self.lan_button.place(x = 220 , y = 0,height = 25, width = 50)
        n_account.set(language_english[0])
        case_a.set(language_english[5])
        quit_a.set(language_english[4])
        login_a.set(language_english[3])
        pass_a.set(language_english[1])
        user_a.set(language_english[2])
        
    def alt_language(self,case_a,quit_a,login_a,pass_a,user_a,n_account):
        
        global lan_bool
        print (lan_bool)
        if(lan_bool):
             n_account.set(language_chinese[0])
             case_a.set(language_chinese[0])
             quit_a.set(language_chinese[0])
             login_a.set(language_chinese[0])
             pass_a.set(language_chinese[0])
             user_a.set(language_chinese[0])
             lan_bool = False
        else: 
            n_account.set(language_english[0])
            case_a.set(language_english[0])
            quit_a.set(language_english[0])
            login_a.set(language_english[0])
            pass_a.set(language_english[0])
            user_a.set(language_english[0])
            lan_bool = True

        
        
            


        

    def new_account(self,name,password,counter):
        check = 0
        for item in member_list:
            if(name == item ):
                self.label = Label(self,text = "Account exists", bg = '#00b7ea', font = ("Purisa",7), fg = 'red')
                self.label.grid(row = 9,column = 1 ,columnspan = 1,sticky = W+E+N+S)
            if(name != item):
                check = check + 1
        if(check == len(member_list)):
            member_list.append(name)
            password_list.append(password)
        print (member_list)
        print (password_list)         

    def quit_button(self):
        quit()

    def input_check(self,name,password,counter):
        for item in member_list:
            if(name == item ):
                for item in password_list:
                    if(password == item):
                        del User_id[0]
                        User_id.append(name)
                        Main_Menu()
                    else:
                        print ("Incorrect Password")
                        self.label = Label(self,text ="Incorrect Password/Username" , bg = '#00b7ea',font = ("Purisa",7), fg = 'red')
                        self.label.grid( row = 9, column = 2, columnspan = 2, sticky = W+E+N+S )

            else:
                print ("Incorrect Username")
                if(counter == 0):
                    self.label = Label(self,text ="Incorrect Password/Username" , bg = '#00b7ea',font = ("Purisa",7), fg = 'red')
                    self.label.grid( row = 9, column = 2, columnspan = 2, sticky = W+E+N+S )
                else:
                    counter = counter + 1
                    
        
                    
                

        
class Main_Menu(Frame):     
    def __init__(self):
        new = Tk()
        """new.resizable(width = FALSE,height = FALSE)"""
        name = User_id[0:1]
        new.title("Username: " + str(name))
        new.configure(background = '#00b7ea')
        """ Current Modules """
        listbox = Listbox(new)
        listbox.insert(END)
        for item in modulelist:
            listbox.insert(END,item)
        listbox.grid( row = 2, column = 1, columnspan = 1, sticky = W+E+N+S )
        lb = Listbox(new)
        """ Dropped Modules """
        listbox_drop = Listbox(new)
        for item in dropped_module_list:
            listbox_drop.insert(END,item)
        listbox_drop.grid( row = 3, column = 1, columnspan = 1, sticky = W+E+N+S )
        """ Entry Box """
        signout_button = Button(new,text = "Sign-Out", command = lambda : self.close_window() )
        signout_button.grid( row = 1, column = 2, columnspan = 1, sticky = W+E+N+S )
        grades_button = Button(new,text = "My Grades" )
        grades_button.grid( row = 1, column = 1, columnspan = 1, sticky = W+E+N+S )
        """ Adding Modules / Delete Modules """
        add_entry = Entry(new)
        add_entry.grid(row = 4, column = 1, columnspan = 1, sticky = W+E+N+S )
        add_module = Button(new,text = "Add Module" , command = lambda : self.add_modules(add_entry.get(),listbox ))
        add_module.grid( row = 5, column = 1, columnspan = 1, sticky = W+E+N+S)
        del_module = Button(new , text = "Delete Module" , command = lambda : self.delete_modules(add_entry.get(),listbox))
        del_module.grid( row = 6, column = 1, columnspan = 1, sticky = W+E+N+S )
        
        
        
    def add_modules(new,text,listbox):
        listbox.insert(0,text)
        print (modulelist)
        
        
    def delete_modules(self,text,listbox):
        pos = 0
        for i in listbox.curselection():
            idx = int(i) - pos
            listbox.delete(idx,idx)
            pos = pos + 1
        

    def close_window(self):
        quit()
        

def main(): 
    Welcome().mainloop()

if __name__ == '__main__':
    main()
