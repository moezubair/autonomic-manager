__author__ = 'Muhammad Zubair'
from tkinter import *
from tkinter import ttk

def setAlarm(time):
    timer.set(time)

root = Tk()
root.title ("Simple Alarm Program")

mainframe = ttk.Frame(root,padding="5 5 12 12")
mainframe.grid(column=0, row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0,weight=1)
mainframe.rowconfigure(0,weight=1)

timer = StringVar()

timer_entry = ttk.Entry(mainframe,width=7,textvariable=timer)
timer_entry.grid(column=2,row=10,sticky=(W,E))
ttk.Label(mainframe, textvariable=timer).grid(column=2, row=2, sticky=(W,E))
ttk.Button(mainframe, text="Set Alarm", command=setAlarm).grid(column=3,row=3,sticky=W)


root.mainloop()