from tkinter import *
from tkinter import ttk
from random import randrange as rnd, choice
import time
import threading
import sqlite3

class DB:
    def __init__(self):
        self.conn = sqlite3.connect('records.db')
        self.c = self.conn.cursor()
        self.c.execute(
            '''CREATE TABLE IF NOT EXISTS records(
                id integer primary key,
                player text, 
                score integer)''')
        self.conn.commit()
    
    def insert_data(self, player, score):
        self.c.execute('''INSERT INTO records(player, score) VALUES (?, ?)''', 
            (player, score))
        self.conn.commit()

    

class MyFirstGUI:
    COLORS = ['red','orange','yellow','green','blue']

    def __init__(self, master):
        self.db = db
        self.master = master
        self.master.title("Catch the ball.")
        self.my_initialization()

    def thread(self):
        def wrapper(*args, **kwargs):
            my_thread = threading.Thread(target=self, args = args, kwargs = kwargs)
            my_thread.start()
        return wrapper
    
    def new_round(self):
        #ball and score initialization
        self.points = 0
        self.x = rnd(100,700)
        self.y = rnd(100,500)
        self.r = rnd(30,50)
        
        if self.player: 
            #If play second time
            self.f_show.pack_forget()
            self.f_fon.pack_forget()
            self.f_records.pack_forget()
            self.f_login.pack_forget()
            self.rem_seconds = 59
            self.f_canvas.pack(fill=BOTH, expand = 1)
            self.canv.pack(fill=BOTH, expand = 1)

            self.canv.delete(self.text_score)
            self.canv.delete(self.ball)
            self.canv.delete(self.text_timer)
            self.canv.delete(self.text_color)
            #self.text_score = self.canv.create_text(60,20, text="Score: " + str(self.points), font = 'Arial 20')
            
            
            #threading._shutdown()
        else:
            self.player = self.entry_login.get()
            self.f_fon.pack_forget()
            self.f_login.pack_forget()
        
        self.f_canvas.pack(fill=BOTH, expand = 1)
        self.canv.pack(fill=BOTH, expand = 1)
        self.rem_seconds = 59
        #remember color for the round
        self.round_color = choice(self.COLORS)
        self.ball = self.canv.create_oval(-100,0,0,0)
        #ball and score initialization
        self.points = 0
        self.x = rnd(100,700)
        self.y = rnd(100,500)
        self.r = rnd(30,50)
        #creating text areas
        self.text_score = self.canv.create_text(60,20,text="Score: " + str(0), font = 'Arial 20')
        self.text_color = self.canv.create_text(700,20, text = "Catch "+ self.round_color + " ball." , font = 'Arial 20' )
        self.text_timer = self.canv.create_text(350,20, text = self.rem_seconds, font = 'Arial 20')
        #Starting methods with thread
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
            self.f_canvas.pack_forget()
            self.label_showing['text'] = f"{self.player}, your score : {self.points}"
            self.f_show.pack(fill=BOTH, expand =1)
            self.f_fon.pack(fill=BOTH, expand =1)
            
            

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
                if self.points >= 1 : 
                    self.points -= 1
                self.draw_click()
    
    def saving(self, player, score):
        self.db.insert_data(player, score)
    
    def showing(self):
        self.saving(self.player, self.points)
        self.view_records()
        self.f_fon.pack_forget()
        self.f_records.pack(side = BOTTOM, expand = 1)

    def view_records(self):
        self.db.c.execute('''SELECT player, score FROM records ORDER BY score DESC LIMIT 15''')
        [self.tree.delete(i) for i in self.tree.get_children()]
        [self.tree.insert('', 'end',values=row) for row in self.db.c.fetchall()] 

    def quit(self):
        self.master.destroy() 
    
    def my_initialization(self):
        self.player = ""
        #create frames
        self.f_login = Frame()
        self.f_fon = Frame()
        self.f_canvas = Frame()
        self.f_show = Frame()
        self.f_records = Frame()
        #canvas for the game
        self.canv = Canvas(self.f_canvas, bg='#38658a')
        #canvas for the image
        self.canv_fon = Canvas(self.f_fon)
        self.image_fon = PhotoImage(file ="catch-logo.png")
        self.canv_fon.create_image(350,150, image = self.image_fon)
        self.f_fon.pack(fill=BOTH) 
        self.canv_fon.pack(fill=BOTH)
        #login fields
        self.entry_login = Entry(self.f_login, justify= CENTER)
        self.label_login = Label(self.f_login, text= "Login")
        self.button_login = Button(self.f_login, text = "Login", activebackground = "#555555", width= "18", height = "2", command = self.new_round)
        self.f_login.pack(expand = 1)
        #----------------------------------------
        self.label_login.pack(expand = 1)
        self.entry_login.pack(expand = 1)
        self.button_login.pack(expand = 1)
        #show frame
        self.label_showing = Label(self.f_show, text = 'Finish', font=("Comic Sans MS", 24, "bold"))
        self.button_newgame = Button(self.f_show, text = 'New game', width= "18", height = "2", activebackground = "#555555", command = self.new_round)
        self.button_records = Button(self.f_show, text = 'Records', width= "18", height = "2", activebackground = "#555555", command = self.showing)
        self.button_exit = Button(self.f_show, text = 'Exit', width= "18", height = "2", activebackground = "#555555", command = self.quit)
        self.label_showing.pack(side = TOP, expand = 1)
        self.button_newgame.pack(side = TOP, ) 
        self.button_records.pack(side = TOP, )
        self.button_exit.pack(side = TOP, )
        #records frame
        self.tree = ttk.Treeview(self.f_records, columns =('Player', 'Score'), height = 15, show ='headings')
        self.tree.column('Player', width = 100, anchor = CENTER)
        self.tree.column('Score', width = 100, anchor = CENTER)
        self.tree.heading('Player', text='Player')
        self.tree.heading('Score', text='Score')
        self.tree.pack(fill = BOTH, expand = 1)
    
root = Tk()
root.geometry('800x600')
db = DB()
main_gui = MyFirstGUI(root)

root.mainloop()

#_____________________________________________________
