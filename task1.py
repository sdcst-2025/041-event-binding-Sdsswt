import tkinter as tk
import playsound as p



def playsound1(event):
    print(event)
    p.playsound("laser-gun-81720.mp3")
def playsound2(event):
    print(event)
    p.playsound("vintage-car-horn-153264.mp3")
def playsound3(event):
    print(event)
    p.playsound("hood-irony.mp3")

win = tk.Tk()
win.attributes('-topmost',True)

b1 =  tk.Button(win,text="Lazer gun",command="playsound")
b1.bind("<Button>",playsound1)
b1.pack()

b2 =  tk.Button(win,text="Car horn")
b2.bind("<Button>",playsound2)
b2.pack()

b2 =  tk.Button(win,text="Hood irony")
b2.bind("<Button>",playsound3)
b2.pack()

win.mainloop()
