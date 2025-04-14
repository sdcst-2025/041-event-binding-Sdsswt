import playsound as p
import tkinter as tk
from tkinter import *

def playsound1(event):
    p.playsound("laser-gun-81720.mp3", block=False)

def playsound2(event):
    p.playsound("vintage-car-horn-153264.mp3", block=False)

def playsound3(event):
    p.playsound("hood-irony.mp3", block=False)

def playsound4(event):
    p.playsound("bobrito-bandito-italian-brainrot.mp3", block=False)

def playsound5(event):
    p.playsound("pk-fire.mp3", block=False)

def playsound6(event):
    p.playsound("monkey-scream-6407.mp3", block=False)

win = tk.Tk()
win.geometry("700x400")
win.attributes('-topmost', True)

carhorn_original = PhotoImage(file="horn.png")
carhorn_small = carhorn_original.subsample(4, 4)  

# Buttons
b1 = tk.Button(win, text="Laser Gun")
b1.bind("<Button>", playsound1)
b1.pack()

b2 = tk.Button(win, image=carhorn_small)
b2.bind("<Button>", playsound2)
b2.pack()

b3 = tk.Button(win, text="Hood irony")
b3.bind("<Button>", playsound3)
b3.pack()

b4 = tk.Button(win, text="Italian brain rot")
b4.bind("<Button>", playsound4)
b4.pack()

b5 = tk.Button(win, text="pk-fire")
b5.bind("<Button>", playsound5)
b5.pack()

b6 = tk.Button(win, text="monkey")
b6.bind("<Button>", playsound6)
b6.pack()

win.mainloop()