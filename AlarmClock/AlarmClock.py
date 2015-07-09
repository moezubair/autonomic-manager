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
        
        self.volume_slider = Scale(length=140, label='Volume', from_=100, to=0)
        self.volume_slider.pack({"side":"right"})
        self.volume_slider.set(self.volume)

        self.sensor_data = Scale(length=140, label='Noise', from_=100, to=0)
        self.sensor_data.pack({"side":"left"})

        self.alarm_sound = Sound('boom.wav')

        
    def setAlarm(self):
        self.alarm_set = True
        print (self.alarm.get())

    def stopAlarm(self):
        self.alarm_sound.stopSound()
        self.alarm_set = False
        self.alarm_playing = False
        print ("Stop alarm")

    def tick(self):
        self.volume = self.volume_slider.get()
        self.time2 = time.strftime('%H:%M:%S')

        if self.time2 != self.time1:
            self.time1 = self.time2
            self.clock.config(text=self.time2)

        if self.alarm.get() == time.strftime('%H:%M') and self.alarm_set and not self.alarm_playing:
            self.alarm_sound.playSound()
            self.alarm_playing = True

        if self.volume < 100:
            self.volume += 1.0
            self.volume_slider.set(self.volume)
            self.alarm_sound.soundVolume(self.volume/100)

        # calls itself every 200 milliseconds
        # to update the time display as needed
        self.clock.after(200, self.tick)


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack({"side": "bottom"})
        self.volume = 50.0
        self.time1 = ''
        self.alarm_set = False
        self.alarm_playing = False
        self.createWidgets()
        self.tick()
        

root = Tk()
root.title ("Simple Alarm Program")
root.geometry("350x350+300+300")
app = AlarmClock(master=root)
app.mainloop()
root.destroy()


