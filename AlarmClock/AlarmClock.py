from Tkinter import *
from sound import *
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

        self.stop_alarm = Button(self)
        self.stop_alarm["text"] = "Stop Alarm"
        self.stop_alarm["command"] = self.stopAlarm
        self.stop_alarm.pack({"side":"bottom"})

        self.set_alarm = Button(self)
        self.set_alarm["text"] = "Set Alarm"
        self.set_alarm["command"] = self.setAlarm
        self.set_alarm.pack({"side": "bottom"})    
        
        self.volume_slider = Scale(length=140, label='Volume')
        self.volume_slider.pack({"side":"right"})

        self.sensor_data = Scale(length=140, label='Noise')
        self.sensor_data.pack({"side":"left"})

        self.alarm_sound = Sound('/Users/jorgeconde/Downloads/pygame-1.9.1release/examples/data/boom.wav')

        
    def setAlarm(self):
        #timer.set(time)
        print (self.alarm.get())

    def stopAlarm(self):
        print ("Stop alarm")

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
        self.alarm_set = False
        self.tick()
        

root = Tk()
root.title ("Simple Alarm Program")
root.geometry("350x350+300+300")
app = AlarmClock(master=root)
app.mainloop()
root.destroy()


