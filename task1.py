
import playsound as p
import tkinter as tk
from tkinter import *

def playsound1(event):
    print(event)
    p.playsound("laser-gun-81720.mp3",block=False)
def playsound2(event):
    print(event)
    p.playsound("vintage-car-horn-153264.mp3",block=False)
def playsound3(event):
    print(event)
    p.playsound("hood-irony.mp3",block=False)
def playsound4(event):
    print(event)
    p.playsound("bobrito-bandito-italian-brainrot.mp3",block=False)

win = tk.Tk()
win.geometry("700x300")
win.attributes('-topmost',block=False)

b1 =  tk.Button(win,text="Lazer gun",command="playsound")
b1.bind("<Button>",playsound1)
b1.pack()

b2 =  tk.Button(win,text="Car horn")
b2.bind("<Button>",playsound2)
b2.pack()

b3 =  tk.Button(win,text="Hood irony")
b3.bind("<Button>",playsound3)
b3.pack()

b4 =  tk.Button(win,text="Italian brain rot")
b4.bind("<Button>",playsound4)
b4.pack()

win.mainloop()