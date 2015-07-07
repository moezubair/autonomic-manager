__author__ = 'Muhammad Zubair'
from tkinter import *
from tkinter import ttk

def setAlarm(time):
    timer.set(time)

root = Tk()
root.title ("Simple Alarm Program")

mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)

timer = StringVar()

ttk.Label(mainframe, textvariable=timer).grid(column=2, row=2, sticky=(W,E))
ttk.Button(mainframe, text="Set Alarm", command=setAlarm).grid(column=3,row=3,sticky=W)

root.mainloop()