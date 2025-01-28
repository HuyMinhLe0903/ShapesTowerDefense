import tkinter as tk
import threading

canRun = True
running = False

def open():
    def run(): 
        global screen  
        global running
        screen = tk.Tk()
        screen.title("Tutorial")
        screen.geometry("410x200")
        running = True
        bigLabel = tk.Label(screen,text = "TUTORIAL",font = ("arial",16,"bold"))
        bigLabel.pack()
        text = tk.Label(screen,
            text = "Hello, Welcome to Shapes Tower Defense\nButton:\nButton 'MODE' for play with other map and gameplay.\nButton 'SET UP TEAM' for edit and manager your team.\nButton 'GACHA' for get random tower and upgrade your team !!!\n",
            font = ("arial",10,"bold")
        )
        text.pack()
        screen.mainloop()
        running = False
    thread = threading.Thread(target = run)
    thread.start()
    return thread