from tkinter import *
from random import randrange as rnd, choice
import time
import threading
import sqlite3


class Player:
    def __init__(self):
        pass
        


class MyFirstGUI:
    COLORS = ['red','orange','yellow','green','blue']

    def __init__(self, master):
        
        self.master = master
        self.master.title("Catch the ball.")
        #create frames
        self.f_login = Frame(master)
        self.f_fon = Frame(master)
        self.f_canvas = Frame(master)
        #canvas for the game
        self.canv = Canvas(self.f_canvas, bg='#38658a')
        #canvas for the image
        self.canv_fon = Canvas(self.f_fon)
        self.image_fon = PhotoImage(file ="catch-logo.png")
        self.canv_fon.create_image(350,150, image = self.image_fon)
        self.f_fon.pack(fill=BOTH) 
        self.canv_fon.pack(fill=BOTH)
        #login fields
        self.entry_login = Entry(self.f_login)
        self.entry_password = Entry(self.f_login, show ='*')
        self.label_login = Label(self.f_login, text= "Login")
        self.label_password = Label(self.f_login, text ="password")
        self.button_login = Button(self.f_login, text = "Login", activebackground = "#555555", width= "18", height = "2", command = self.new_round)
        self.f_login.pack(expand = 1)
        #self.f_canvas.pack(fill=BOTH, expand = 1)
        #self.canv.pack(fill=BOTH,expand = 1)
        self.label_login.pack(expand = 1)
        self.entry_login.pack(expand = 1)
        self.label_password.pack(expand = 1)
        self.entry_password.pack(expand = 1)
        self.button_login.pack(expand = 1)

              
    def thread(self):
        def wrapper(*args, **kwargs):
            my_thread = threading.Thread(target=self, args = args, kwargs = kwargs)
            my_thread.start()
        return wrapper

    def greatings(self):
        pass

    def new_round(self):
        self.f_fon.pack_forget()
        self.f_login.pack_forget()
        self.f_canvas.pack(fill=BOTH, expand = 1)
        self.canv.pack(fill=BOTH,expand = 1)
        self.rem_seconds = 59
        #remember color for the round
        self.round_color = choice(self.COLORS)
        self.ball = self.canv.create_oval(-100,0,0,0)
        #creating text areas
        self.text_score = self.canv.create_text(60,20,text="Score: " + str(0), font = 'Arial 20')
        self.text_color = self.canv.create_text(700,20, text = "Catch "+ self.round_color + " ball." , font = 'Arial 20' )
        self.text_timer = self.canv.create_text(350,20, text = self.rem_seconds, font = 'Arial 20')
    
        self.points = 0
        self.x = rnd(100,700)
        self.y = rnd(100,500)
        self.r = rnd(30,50)
        
        self.new_ball()
        self.our_timer()
    

    @thread
    def new_ball(self):
        
        self.canv.delete(self.ball)
        self.x = rnd(100,700)
        self.y = rnd(100,500)
        self.r = rnd(30,50)
        #Choice color for the ball
        self.color = choice(self.COLORS)
        self.ball = self.canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = self.color, width=0)
        self.canv.bind('<Button-1>', self.click)
        
        self.master.after(700, self.new_ball)
        

    @thread
    def our_timer(self):
        if self.rem_seconds >= 1:
            self.rem_seconds -= 1
            self.canv.delete(self.text_timer)
            self.text_timer = self.canv.create_text(350,20, text = self.rem_seconds, font = 'Arial 20')
            self.master.after(1000, self.our_timer)
        else : 
            pass

    #work in few places
    def draw_click(self):
        self.x = -1000
        #deleting ball for click 
        self.canv.delete(self.text_score)
        self.canv.delete(self.ball)
        self.text_score = self.canv.create_text(60,20, text="Score: " + str(self.points), font = 'Arial 20')

    
    
    def click(self, event):
        if (event.y - self.y)**2 + (event.x - self.x)**2 <= self.r**2:
            if self.round_color == self.color:
                self.points += 1
                self.draw_click()
                
            else:
                self.points -= 1
                self.draw_click()
    
    
    
root = Tk()
root.geometry('800x600')

main_gui = MyFirstGUI(root)

root.mainloop()

#_____________________________________________________
