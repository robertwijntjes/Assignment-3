import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import datetime
import sqlite3
import os
import sys
from datetime import timedelta
import time as t
from os import path
from time import strftime
#   LIST OF LIBRARIES USED

conn = sqlite3.connect('Subjects.db')
c = conn.cursor()

modulelist = []
database_mod = {
    'OOP': 'Object-oriented programming (OOP) refers to a type of computer programming (software design) in which programmers define not only the data type of a data structure, but also the types of operations (functions) that can be applied to the data structure.',
    'SFGM' : 'The skills of software engineers are called upon when operational problems are encountered with computer programs and applications.Typical responsibilities include investigating current applications,liaising with users,producing specifications,costing new or modified systems,agreeing proposals,writing new software and operating manuals,testing the product to ensure that it operates satisfactorily,training users,handling support and feedback' }
member_list = ['c14356786']
password_list = ['password']
language_english = ['Username','Password','New Account','Login','Sign-Out','*Passwords are Case Sensitive','CN','Add Module', 'Remove Module','Add Reminder', 'Remove Reminder','My Grades','Save Reminder', 'No Grades Available: Awaiting Response']
language_chinese = ['用户名','密码','新账户','登录','退出','密码区分大小写','英文','添加课程' , '删除课程',' 添加便条  ' ,'删除提醒', '      成绩     ' , '萨沃河提醒', '没有成绩:请等一下儿' ]
dropped_module_list = []
check_count = [0]
check = 0
lan_bool = True
lan_boola = True
lan_boolb = True
User_id = ['holder']
count = 0
#   LIST OF GLOBAL VARIABLES AND LISTS/DICTIONARIES

class Welcome( Frame ):
    def __init__( self ):
        tk.Frame.__init__(self)
        self.master.title("Welcome Menu")
        self.configure(background='#00b7ea')
        self.master.resizable(width = FALSE,height = FALSE)
        self.pack()
        self.make_gui()
        data = [line.strip() for line in open("C:/Users/robert/Desktop/SFGM Assignment/Assignment/userbase.txt", 'r')]
        for i in data:
            modulelist.append(i)
        #   USED FOR MASTER SETUP AND CALLING THE FUNCTION TO GENERATE THE FRAMES GUI AND ALGORITHMS.

    def make_gui(self):
        counter = 0
        n_account = tk.StringVar()
        user_a = tk.StringVar()
        pass_a = tk.StringVar()
        login_a = tk.StringVar()
        quit_a = tk.StringVar()
        case_a = tk.StringVar()
        toggle_a = tk.StringVar()
        load = Image.open("welcome.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self,image = render)
        img.image = render
        img.grid( row = 0, column = 0, columnspan = 2, sticky = W+E+N+S )
        """ Details """
        self.n_label = Label( self , textvariable = user_a , bg = '#00b7ea' )
        self.n_label.grid( row = 5 , column = 0 , columnspan = 2 , sticky = W+E+N+S )
        self.p_label = Label( self , textvariable = pass_a , bg = '#00b7ea' )
        self.p_label.grid( row = 6 , column = 0 , columnspan = 2 , sticky = W+E+N+S )
        self.cs_label = Label( self , textvariable = case_a , font = ( "Purisa" , 7 ) , bg = '#00b7ea' )
        self.cs_label.grid( row = 7 , column = 2 , columnspan = 2 , sticky = W+E+N+S )
        self.name = Entry( self )
        self.name.grid( row = 5 , column = 2 , columnspan = 2 , sticky = W+E+N+S )
        self.password = Entry( self , show = "*" )
        self.password.grid( row = 6 , column = 2 , columnspan = 2 , sticky = W+E+N+S )
        self.quitButton = Button( self , textvariable = quit_a , bg = '#FFFFFF' , command = self.quit_button )
        self.quitButton.grid( row = 8 , column = 3 , columnspan = 1 , sticky = W+E+N+S )
        self.confirmButton = Button( self , textvariable = login_a , bg = '#FFFFFF' , command = lambda : self.input_check( self.name.get() , self.password.get() , counter ))
        self.confirmButton.grid( row = 8 , column = 2 , columnspan = 1 , sticky = W+E+N+S )
        self.new_account_button = Button( self , textvariable = n_account , bg = '#FFFFFF' , command = lambda : self.new_account( self.name.get() , self.password.get() , counter ))
        self.new_account_button.grid( row = 8 , column = 0 , columnspan = 2 , sticky = W+E+N+S )
        self.lan_button = Button( self , textvariable = toggle_a , command = lambda : self.alt_language( case_a , quit_a , login_a , pass_a , user_a , n_account , toggle_a ))
        self.lan_button.place( x = 200 , y = 0 , height = 25 , width = 50 )
        toggle_a.set( language_english[6] )
        n_account.set( language_english[2] )
        case_a.set( language_english[5] )
        quit_a.set( language_english[4] )
        login_a.set( language_english[3] )
        pass_a.set( language_english[1])
        user_a.set( language_english[0] )
        #   INIT AND DISPLAY ALL GUI WHILE CALLING MANY FUNCTIONS TO IMPLEMENT THEIR USAGE SUCH AS COMPLEX DATABASE SEARCHES AND ALTERNATION OF DATA.
        
    def alt_language(self,case_a,quit_a,login_a,pass_a,user_a,n_account,toggle_a):
        
        global lan_bool
        if(lan_bool):
             n_account.set( language_chinese[0] )
             case_a.set( language_chinese[5] )
             quit_a.set( language_chinese[4] )
             login_a.set( language_chinese[3] )
             pass_a.set( language_chinese[1] )
             user_a.set( language_chinese[2] )
             toggle_a.set( language_chinese[6] )
             lan_bool = False
        else: 
            n_account.set( language_english[2])
            case_a.set( language_english[5] )
            quit_a.set( language_english[4] )
            login_a.set( language_english[3] )
            pass_a.set( language_english[1] )
            user_a.set( language_english[0] )
            toggle_a.set( language_english[6] )
            lan_bool = True
        #   ALTERNATES THE LOGIN FRAMES LANGUAGE WITH THE USAGE OF THE :CN BUTTON
  

    def new_account(self,name,password,counter):
        check = 0
        for item in member_list:
            if(name == item ):
                self.label = Label(self , text = "Account Exists" , bg = '#00b7ea' , font = ("Purisa",7) , fg = 'red')
                self.label.grid( row = 9 , column = 1 , columnspan = 1 , sticky = W+E+N+S )
                break
            if(name != item):
                check = check + 1
                
        if(check == len(member_list)):
            member_list.append( name )
            password_list.append( password )
            self.label = Label(self , text = "Account Created" , bg = '#00b7ea' , font = ("Purisa",7) , fg = '#00ff00')
            self.label.grid( row = 9 , column = 1 , columnspan = 1 , sticky = W+E+N+S )
        print (member_list)
        print (password_list)
        # USED FOR IMPLEMENTING AN ACCOUNT CREATABLE BUTTON AND ADDS THE USERNAME AND PASSWORD TO THE LIST WHICH ARE IN SYNC

    def quit_button(self):
        quit()
        #   SIMPLE QUIT BUTTON

    def input_check(self,name,password,counter):
        for item in member_list:
            if(name == item ):
                for item in password_list:
                    if(password == item):
                        del User_id[0]
                        User_id.append( name )
                        Main_Menu()
                        self.c_label = Label( self , text = "Login Verified" ,  bg = '#00b7ea' , font = ("Purisa",7) , fg = '#00ff00' )
                        self.c_label.grid( row = 9 , column = 2 , columnspan = 2 , sticky = W+E+N+S )
                        break
                    else:
                        print ("Incorrect Password")
                        self.label = Label( self , text ="Incorrect Password/Username" , bg = '#00b7ea', font = ("Purisa",7) , fg = 'red')
                        self.label.grid( row = 9 , column = 2 , columnspan = 2 , sticky = W+E+N+S )

            else:
                print ("Incorrect Username")
                if(counter == 0):
                    self.label = Label( self , text ="Incorrect Password/Username" , bg = '#00b7ea' , font = ("Purisa",7) , fg = 'red')
                    self.label.grid( row = 9 , column = 2 , columnspan = 2 , sticky = W+E+N+S )
                else:
                    counter = counter + 1
    #   CHECKS IF THE PASSWORD WHICH IS IN SYNC WITH THE USERNAME IS CORRECT.IF NOT THEN DROP DOWN DISPLAYS INCORRECT MESSAGE.
                    
        
                    
                

        
class Main_Menu(Frame):     
    def __init__(self):
        new = Tk()
        new.resizable( width = FALSE , height = FALSE )
        name = User_id[0:1]
        new.title( str( name ) )
        new.configure( background = '#00b7ea' )
        """Module Descriptions"""
        description_box = Text( new )
        description_box.place( x = 125 , y = 27 , height = 350 , width = 125 )
        """ Current Modules """
        listbox = Listbox( new )
        listbox.insert( END )
        for item in modulelist:
            listbox.insert( END , item )
        listbox.bind("<Double-Button-1>", lambda event : self.OnDouble( event , description_box ))
        listbox.grid( row = 2 , column = 1 , columnspan = 2 , sticky = W+E+N+S )
        """ Dropped Modules """
        listbox_drop = Listbox( new )
        for item in dropped_module_list:
            listbox_drop.insert( END , item )
        listbox_drop.bind("<Double-Button-1>", lambda event : self.OnNDouble( event , description_box ))
        listbox_drop.grid( row = 3 , column = 1 , columnspan = 2 , sticky = W+E+N+S )
        """ Entry Box """
        signout_button = Button( new , text = "Sign-Out" , command = lambda : self.close_window() )
        signout_button.grid( row = 1, column = 6, columnspan = 1, sticky = W+E+N+S )
        grades_button = Button( new , text = "My Grades" , command  = lambda : self.call_grades(listbox) )
        grades_button.grid( row = 1 , column = 3 , columnspan = 1 ,rowspan = 1 ,sticky = W+E+N+S )
        """ Adding Modules / Delete Modules """
        add_entry = Entry( new )
        add_entry.grid( row = 4 , column = 1 , columnspan = 1 , sticky = W+E+N+S )
        add_module = Button( new , text = "Add Module" , command = lambda : self.add_modules( add_entry.get() , listbox ))
        add_module.grid( row = 5, column = 1, columnspan = 1, sticky = W+E+N+S)
        del_module = Button( new , text = "Delete Module" , command = lambda : self.delete_modules( add_entry.get() , listbox))
        del_module.grid( row = 6, column = 1 , columnspan = 1 , sticky = W+E+N+S )
        add_reminder = Button( new , text = "Add Reminder" , command = lambda : self.add_reminder( add_entry.get() , listbox_drop))
        add_reminder.grid( row = 7 , column = 1 , columnspan = 1 , sticky = W+E+N+S )
        del_reminder = Button(new , text = "Delete Reminder", command = lambda : self.delete_reminder( add_entry.get() , listbox_drop ))
        del_reminder.grid( row = 8 , column = 1 , columnspan = 1 , sticky = W+E+N+S )
        create_file = Button(new , text = "Save Reminder" ,command = lambda : self.createFile(add_entry.get()) )
        create_file.grid(row = 5 , column = 3 , columnspan = 4, rowspan = 4, sticky = W+E+N+S)
        alt_language = Button( new  , text = "CN" , command = lambda : self.alt_lan( alt_language , signout_button , grades_button , add_module , del_module , add_reminder , del_reminder ,create_file))
        alt_language.grid(row = 1 , column = 1 , columnspan = 2, sticky = W+E+N+S)
        #   MAIN MENU FRAME WHERE ALL ENTITIES ARE INIT.


    def createFile(self,text):
        
        dest = 'C:\\Users\\robert\\Desktop\\SFGM Assignment\\Assignment\\Reminders2016-04-18\\'
        date = t.localtime(t.time())
        name =  strftime("%H-%M") + '.txt'
        if not(path.isfile(dest + name)):
            f = open(dest + name,'w')
            f.write(text + ('\n'*30) + 'END OF SCRIPT')
            f.close()
        #   CREATES A FILE IN A PRESET REPO
         
        

    def call_grades( self , box):
        My_Grades()
    #   CALLS THE GRADES CLASS


    def OnDouble( self, event , box ):
        #global count
        widget = event.widget
        selection=widget.curselection()
        value = widget.get(selection[0])
        for i in widget.curselection():
            for i in database_mod.keys():
                if( i == value ):
                    box.delete( '1.0' , END )
                    box.insert( END , database_mod[i] )
                    break
                else:
                    box.delete( '1.0' , END )
        #   DISPLAYS INFO IN THE TEXT BOX WHEN DOUBLE CLICKED ON EITHER SFGM or OOP 
                    
    def OnNDouble(self , event , box):
        global count
        widget = event.widget
        selection = widget.curselection()
        value = widget.get(selection[0])
        nValue = (widget.get(ACTIVE))
        box.delete( '1.0' , END )
        box.insert( END , nValue )
    #   SHOWS INFO FROM THE REMINDERS BOX IN THE TEXT BOX
        
            

    def alt_lan(self,alt_language,signout_button,grades_button,add_module,del_module,add_reminder,del_reminder,cr_file):
        global lan_boola
        print (lan_boola)
        if(lan_boola):
            add_module.configure( text = language_chinese[7] )
            alt_language.configure( text = language_chinese[6] )
            signout_button.configure( text = language_chinese[4] )
            grades_button.configure( text = language_chinese[11] )
            del_module.configure( text = language_chinese[8] )
            add_reminder.configure( text = language_chinese[9] )
            del_reminder.configure( text = language_chinese[10] )
            cr_file.configure(text = language_chinese[12])
            lan_boola = False
        else:
            add_module.configure( text = language_english[7] )
            alt_language.configure( text = language_english[6] )
            signout_button.configure( text = language_english[4] )
            grades_button.configure( text = language_english[11] )
            del_module.configure( text = language_english[8] )
            add_reminder.configure( text = language_english[9] )
            del_reminder.configure( text = language_english[10] )
            cr_file.configure( text = language_english[12])
            lan_boola = True
        #   ALTERNATES THE LANGUAGE WITHIN THE MAIN FILE
        
    def add_reminder( new , text , listbox ):
        utc_datetime = datetime.datetime.utcnow()
        formated_string = utc_datetime.strftime("%Y-%m-%d")
        listbox.insert(0,formated_string + "| " + text )
        
        try:
            os.mkdir("Reminders2016-04-18")
        except:
            print (formated_string + 'File already Exists')
        #   USES EXECPTIONS TO CREATE THE DIRECTORY WHERE THE FILE IS CREATED.

            
    def add_modules( new , text , listbox ):
        listbox.insert( 0 , text )
        modulelist.append( text )
        #   USED FOR ADDING MODULES TO THE MODULE LISTBOX
        
    def delete_reminder( new , text , listbox ):
        pos = 0
        for i in listbox.curselection():
            idx = int(i) - pos
            listbox.delete(idx,idx)
            pos = pos + 1
        #   USED FOR DELETING REMINDERS FROM THE REMINDER LISTBOX
            
    def delete_modules( self , text , listbox ):
        pos = 0
        for i in listbox.curselection():
            idx = int(i) - pos
            listbox.delete(idx,idx)
            pos = pos + 1
        del modulelist[idx]
        #   DELETE MODULES FROM THE MODULE LISTBOX
        

    def close_window( self ):
        quit()


class My_Grades(Frame):     
    def __init__(self):
        grades = Tk()
        grades.resizable( width = FALSE , height = FALSE )
        name = User_id[0:1]
        grades.title( "Grades" )
        grades.configure( background = '#00b7ea' )
        name_label = Label( grades , text = 'Username : ')
        name_label.grid(row = 1 , column = 2 , columnspan = 1, sticky = W+E+N+S )
        grade_label = Label( grades , text = str(name))
        grade_label.grid( row = 1 , column = 3 , columnspan = 1, sticky = W+E+N+S )
        grade_r = Label( grades, text = ' Grades')
        grade_r.grid( row = 1 , column = 1 , columnspan = 1, sticky = W+E+N+S )
        grades_x = Label( grades , text = "No Grades Available: Awaiting Response")
        grades_x.grid( row = 3 , column = 1 , columnspan = 3, sticky = W+E+N+S )
        listbox_grades = Listbox( grades )
        for item in modulelist:
            listbox_grades.insert( END , item + ' :'  )
            listbox_grades.grid( row = 2 , column = 1 , columnspan = 2 , sticky = W+E+N+S )
        change_lan = Button( grades , text = 'CN', command = lambda : self.language_change( name_label , grade_label , grade_r , grades_x ) )
        change_lan.grid( row = 2 , column = 3 , columnspan = 3, sticky = W+E+N+S )
        #   INIT THE GUI

    def language_change(self, name_label , grade_label , grade_r , grades_x):
        global lan_boolb
        print (lan_boolb)
        if(lan_boolb):
            name_label.configure( text = language_chinese[0])
            grade_r.configure( text = language_chinese[11])
            grades_x.configure( text = language_chinese[13])
            lan_boolb = False
        else:
            name_label.configure( text = language_english[0])
            grade_r.configure( text = language_english[11])
            grades_x.configure( text = language_english[13])
            lan_boolb = True
        #   ALTERNATING LANGUAGE

        
        

def main(): 
    Welcome().mainloop()
    #   BEGINS THE LOOP

if __name__ == '__main__':
    main()
    #   CALLS THE MAIN
    
