__author__ = 'Muhammad Zubair'
from tkinter import *
from tkinter import ttk
import time

class AlarmClock(Frame):

    def createWidgets(self):

        self.clock = Label(font=('courier', 20, 'bold'), bg='black', fg='green')
        self.clock.pack()

        self.alarm = StringVar()
        self.alarm.set("HH:MM")

        self.alarm_entry = Entry()
        self.alarm_entry.pack({"side": "bottom"})  
        self.alarm_entry["textvariable"] = self.alarm

        self.set_alarm = Button(self)
        self.set_alarm["text"] = "Set Alarm"
        self.set_alarm["command"] = self.setAlarm
        self.set_alarm.pack({"side": "bottom"})

        
    def setAlarm(self):
        #timer.set(time)
        print (self.alarm.get())

    def tick(self):
        self.time2 = time.strftime('%H:%M:%S')
        if self.time2 != self.time1:
            self.time1 = self.time2
            self.clock.config(text=self.time2)

        # calls itself every 200 milliseconds
        # to update the time display as needed
        self.clock.after(200, self.tick)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack({"side": "bottom"})
        self.createWidgets()

        self.time1 = ''
        self.tick()
        

root = Tk()
root.title ("Simple Alarm Program")
app = AlarmClock(master=root)
app.mainloop()
root.destroy()