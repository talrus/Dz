from tkinter import *
from random import randrange as rnd, choice
import time
# створюємо вікно

class MyFirstGUI:
    COLORS = ['red','orange','yellow','green','blue']

    def __init__(self, master):
        self.master = master
        master.title("Home work Tkinter")
        
        self.text = ""
        self.points = 0
        self.x = rnd(100,700)
        self.y = rnd(100,500)
        self.r = rnd(30,50)
        
        self.canv = Canvas(master, bg = 'white')
        self.canv.pack(fill = BOTH, expand = 1)
        self.ball = self.canv.create_oval(-100,0,0,0)
        self.text = self.canv.create_text(60,20,text="Score: " + str(0), font = 'Arial 20')
        

    def new_ball(self):
        self.canv.delete(self.ball)
        self.x = rnd(100,700)
        self.y = rnd(100,500)
        self.r = rnd(30,50)
        self.ball = self.canv.create_oval(self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r, fill = choice(self.COLORS), width=0)
        self.canv.bind('<Button-1>', self.click)
        self.master.after(1000, self.new_ball)

    def click(self, event):
        if (event.y - self.y)**2 + (event.x - self.x)**2 <= self.r**2:
            self.points += 1
            self.x = -1000
			#видалення круга при кліку
            self.canv.delete(self.text)
            self.canv.delete(self.ball)
            self.text = self.canv.create_text(60,20, text="Score: " + str(self.points), font = 'Arial 20')

root = Tk()
root.geometry('800x600')

main_gui = MyFirstGUI(root)
main_gui.new_ball()
root.mainloop()

#_____________________________________________________
