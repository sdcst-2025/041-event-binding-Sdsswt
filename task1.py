import tkinter as tk
import playsound as p

def playsound(event):
    print(event)
    p.playsound("animals_dogs_x2_barking_small_001.mp3")


win = tk.Tk()
win.attributes('-topmost',True)
l1 = tk.Label(win,text="This button has an event bound by a command")
l2 = tk.Label(win,text="This button has an event bound by a bind")

b1 =  tk.Button(win,text="Click to play",command="playsound")
b2 =  tk.Button(win,text="Click to play")
b2.bind("<Button>",playsound)


l1.pack()
b1.pack()
l2.pack()
b2.pack()

win.mainloop()
