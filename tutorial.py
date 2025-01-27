import tkinter as tk

canRun = True

def run(): 
    global screen  
    screen = tk.Tk()
    screen.geometry("300x300")
    screen.mainloop()